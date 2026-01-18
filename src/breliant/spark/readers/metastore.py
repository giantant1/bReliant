"""
Create Spark DataFrame from table in Metastore
"""

from breliant.models import Field
from breliant.spark.readers import Reader


class MetastoreReader(Reader):
    """Reader for tables/views from Spark Metastore

    Parameters
    ----------
    table : str
        Table name in spark metastore
    """

    table: str = Field(default=..., description="Table name in spark metastore")

    def execute(self) -> Reader.Output:
        self.output.df = self.spark.table(self.table)
