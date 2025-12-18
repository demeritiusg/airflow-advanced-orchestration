from datetime import datetime, timedelta
from typing import Dict, List

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup

DEFUALT_ARGS = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "reties": 2,
    "retry_delay": timedelta(minutes=10),
}


def create_domain_dag(
    *,
    dag_id: str,
    schedule: str,
    start_date: datetime,
    tags: List[str],
    datesets: List[Dict],
    sla_minutes: int = 60,
    ) -> DAG:
    
    with DAG(
        dag_id=dag_id,
        default_args={**DEFUALT_ARGS, "sla": timedelta(minutes=sla_minutes)},
        schedule_interval=schedule,
        start_date=start_date,
        catchup=False,
        max_active_runs=1,
        tags=tags,       
    ) as dag:
        
        start = EmptyOperator(task_id="start")
        end = EmptyOperator(task_id="end")
        
        for dataset in datasets:
            dataset_name = dataset["name"]
            
            with TaskGroup(group_id=f"process_{dataset_name}") as tg:
                extract = EmptyOperator(task_id=f"extract_{dataset_name}")
                transform = EmptyOperator(task_id=f"transform_{dataset_name}")
                load = EmptyOperator(task_id=f"load_{dataset_name}")
                
                extract >> transform >> load
                
            start >> tg >> end
            
        return dag
