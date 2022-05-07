"""AWSCostExplorer tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_aws_cost_explorer.streams import (
    CostAndUsageWithResourcesStream,
)
STREAM_TYPES = [
    CostAndUsageWithResourcesStream,
]


class TapAWSCostExplorer(Tap):
    """AWSCostExplorer tap class."""
    name = "tap-aws-cost-explorer"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "access_key",
            th.StringType,
            required=True,
            description="Your AWS Account Access Key."
        ),
        th.Property(
            "secret_key",
            th.StringType,
            required=True,
            description="Your AWS Account Secret Key."
        ),
        th.Property(
            "session_token",
            th.StringType,
            description="Your AWS Account Session Token if required for authentication."
        ),
        th.Property(
            "start_date",
            th.StringType,
            required=True,
            description="The start date for retrieving Amazon Web Services cost."
        ),
        th.Property(
            "end_date",
            th.DateTimeType,
            description="The end date for retrieving Amazon Web Services cost."
        ),
        th.Property(
            "granularity",
            th.StringType,
            required=True,
            description="Sets the Amazon Web Services cost granularity to \
                        MONTHLY or DAILY , or HOURLY."
        ),
        th.Property(
            "metrics",
            th.ArrayType(th.StringType),
            required=True,
            description="Which metrics are returned in the query. Valid \
                        values are AmortizedCost, BlendedCost, \
                        NetAmortizedCost, NetUnblendedCost, \
                        NormalizedUsageAmount, UnblendedCost, and \
                        UsageQuantity."
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
