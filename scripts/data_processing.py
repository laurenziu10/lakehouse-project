import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyspark.sql import SparkSession
from delta import DeltaTable

# Funktion zum Speichern als Parquet
def save_as_parquet(df, filename):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)
    print(f"Data saved as Parquet: {filename}")

# Funktion zum Speichern als Delta
def save_as_delta(df, filename):
    spark = SparkSession.builder.appName("DeltaExample").getOrCreate()
    df_spark = spark.createDataFrame(df)
    df_spark.write.format("delta").save(filename)
    print(f"Data saved as Delta: {filename}")

# Beispiel DataFrame erstellen
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Daten als Parquet speichern
save_as_parquet(df, 'data/example.parquet')

# Daten als Delta speichern
save_as_delta(df, 'data/example_delta')
