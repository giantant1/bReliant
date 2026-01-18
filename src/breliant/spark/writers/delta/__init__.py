"""
This module is the entry point for the breliant.spark.writers.delta package.

It imports and exposes the DeltaTableWriter and DeltaTableStreamWriter classes for external use.

Classes:
    DeltaTableWriter: Class to write data in batch mode to a Delta table.
    DeltaTableStreamWriter: Class to write data in streaming mode to a Delta table.
"""

from breliant.spark.writers.delta.batch import BatchOutputMode, DeltaTableWriter
from breliant.spark.writers.delta.scd import SCD2DeltaTableWriter
from breliant.spark.writers.delta.stream import DeltaTableStreamWriter

__all__ = ["DeltaTableWriter", "DeltaTableStreamWriter", "SCD2DeltaTableWriter", "BatchOutputMode"]
