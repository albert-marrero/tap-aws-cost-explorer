"""Stream type classes for tap-aws-cost-explorer."""

import datetime
from pathlib import Path
from typing import Optional, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_aws_cost_explorer.client import AWSCostExplorerStream

class CostAndUsageWithResourcesStream(AWSCostExplorerStream):
    """Define custom stream."""
    name = "cost"
    primary_keys = []
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("time_period_start", th.StringType),
        th.Property("time_period_end", th.StringType),
        th.Property("metric_name", th.StringType),
        th.Property("amount", th.StringType),
        th.Property("amount_unit", th.StringType),
    ).to_dict()

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects."""
        next_page = True

        while next_page:
            response = self.conn.get_cost_and_usage(
                TimePeriod={
                    'Start': self.config.get("start_date"),
                    'End': self.config.get("end_date", datetime.date.today() - datetime.timedelta(days=1))
                },
                Granularity=self.config.get("granularity"),
                Metrics=self.config.get("metrics"),
            )
            next_page = response.get("NextPageToken")

            for row in response.get("ResultsByTime"):
                for k, v in row.get("Total").items():
                    yield {
                        "time_period_start": row.get("TimePeriod").get("Start"),
                        "time_period_end": row.get("TimePeriod").get("End"),
                        "metric_name": k,
                        "amount": v.get("Amount"),
                        "amount_unit": v.get("Unit")
                    }
