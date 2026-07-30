"""
etl_metrics.py

Tracks execution metrics for ETL pipelines.
"""

from datetime import datetime
from time import perf_counter


class ETLMetrics:
    """
    Stores and calculates ETL execution metrics.
    """

    def __init__(self, pipeline_name: str):
        self.pipeline_name = pipeline_name

        self.start_time = None
        self.end_time = None

        self.generated = 0
        self.valid = 0
        self.rejected = 0
        self.duplicates = 0
        self.loaded = 0

    def start(self):
        """Start ETL execution tracking."""

        self.start_time = datetime.now()
        self._timer = perf_counter()

    def finish(self):
        """Finish ETL execution tracking."""

        self.end_time = datetime.now()

        self.execution_time = (
            perf_counter() - self._timer
        )

    def success_rate(self):
        """Calculate successful loading percentage."""

        if self.generated == 0:
            return 0

        return (
            self.loaded / self.generated
        ) * 100

    def rejection_rate(self):
        """Calculate rejected record percentage."""

        if self.generated == 0:
            return 0

        return (
            self.rejected / self.generated
        ) * 100

    def print_report(self):
        """Print ETL execution report."""

        print("\n====================================")
        print("ETL EXECUTION REPORT")
        print("====================================")

        print(
            f"Pipeline        : {self.pipeline_name}"
        )

        print(
            f"Start Time      : {self.start_time}"
        )

        print(
            f"End Time        : {self.end_time}"
        )

        print(
            f"Execution Time  : "
            f"{self.execution_time:.2f} seconds"
        )

        print("------------------------------------")

        print(
            f"Generated       : {self.generated}"
        )

        print(
            f"Valid           : {self.valid}"
        )

        print(
            f"Rejected        : {self.rejected}"
        )

        print(
            f"Duplicates      : {self.duplicates}"
        )

        print(
            f"Loaded          : {self.loaded}"
        )

        print("------------------------------------")

        print(
            f"Success Rate    : "
            f"{self.success_rate():.2f}%"
        )

        print(
            f"Rejection Rate  : "
            f"{self.rejection_rate():.2f}%"
        )

        print("====================================")