import pandas as pd
import pandas_gbq
import os

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

