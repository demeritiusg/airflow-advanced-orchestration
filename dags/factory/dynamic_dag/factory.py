from datetime import datetime, timedelta
from typing import Dict, List

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup

DEFUAKLT_ARGS = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "reties": 2,
    "retry_delay": timedelta(minutes=10),
}

