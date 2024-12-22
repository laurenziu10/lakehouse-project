import pandas as pd
from pyspark.sql import SparkSession
import pyarrow.parquet as pq
from delta import DeltaTable

# Funktion zum Laden von CSV-Daten und Speichern als Parquet
def load_and_save_as_parquet(csv_file, parquet_file):
    # Lade CSV-Datei in ein DataFrame
    df = pd.read_csv(csv_file)
    
    # Speichere als Parquet
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_file)
    print(f"Data loaded and saved as Parquet: {parquet_file}")

# Funktion zum Laden von CSV-Daten und Speichern als Delta
def load_and_save_as_delta(csv_file, delta_file):
    # Lade CSV-Datei in ein DataFrame
    df = pd.read_csv(csv_file)
    
    # Erstelle Spark-Session
    spark = SparkSession.builder.appName("DataLoadExample").getOrCreate()
    
    # Speichere als Delta
    df_spark = spark.createDataFrame(df)
    df_spark.write.format("delta").save(delta_file)
    print(f"Data loaded and saved as Delta: {delta_file}")

# Beispiel für das Laden von Daten und Speichern
csv_file = 'data/Amazon Sale Report.csv'
parquet_file = 'data/sample_data.parquet'
delta_file = 'data/sample_data_delta'

load_and_save_as_parquet(csv_file, parquet_file)
load_and_save_as_delta(csv_file, delta_file)
