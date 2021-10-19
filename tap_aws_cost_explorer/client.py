"""Custom client handling, including AWSCostExplorerStream base class."""

import boto3

from singer_sdk.streams.core import Stream
from singer_sdk.tap_base import Tap


class AWSCostExplorerStream(Stream):
    """Stream class for AWSCostExplorer streams."""
    def __init__(self, tap: Tap):
        super().__init__(tap)
        self.conn = boto3.client(
            'ce',
            aws_access_key_id=self.config.get("access_key"),
            aws_secret_access_key=self.config.get("secret_key"),
        )
