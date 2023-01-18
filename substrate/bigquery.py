import pandas as pd
import pandas_gbq
import os
from google.cloud import bigquery

from google.auth import _helpers
import google.auth.compute_engine

project_id = os.getenv('gcp_project_id')
project_vm_sa_email = os.getenv('gcp_project_vm_sa_email')

pandas_gbq.context.project = project_id
pandas_gbq.context.credentials = google.auth.compute_engine.Credentials(service_account_email=project_vm_sa_email)

def to_gbq(df, tbl, if_exists='append'):
  pandas_gbq.to_gbq(df, tbl, if_exists=if_exists)

def read_gbq(txt):
  return pandas_gbq.read_gbq(txt, progress_bar_type=None)

def delete_table(tbl):
  client = bigquery.Client()
  client.delete_table(tbl, not_found_ok=True)

def rename_table(old_name, new_name, dataset = 'roger', proj = 'parity-data-infra-evaluation'):
  client = bigquery.Client()
  query_job = client.query(f"ALTER TABLE `{proj}.{dataset}.{old_name}` RENAME TO `{new_name}`;")

def remove_dups(table_name, dataset = 'roger', proj = 'parity-data-infra-evaluation'):
  client = bigquery.Client()
  query_job = client.query(f"CREATE OR REPLACE TABLE `{proj}.{dataset}.{table_name}_deduped` AS SELECT DISTINCT * FROM `{proj}.{dataset}.{table_name}`;")
  # Rename original talbe
  rename_table(table_name, f"{table_name}_copy")
  rename_table(f"{table_name}_deduped", table_name)


def view_table_expriation(table_name, dataset = 'roger', proj = 'parity-data-infra-evaluation'):
  client = bigquery.Client()
  table = client.get_table(f"{proj}.{dataset}.{table_name}")
  try:
    assert table.expires is None
    print("Table has no expiration.")
  except:
    print("Table expires {table.expires}.")
