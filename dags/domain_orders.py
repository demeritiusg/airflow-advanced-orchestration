from datetime import datetime
from factory.dynamic_dag_factory import create_domain_dag


ORDERS_DATASETS = [
{
"name": "orders",
"source": "s3://raw/orders",
"destination": "s3://curated/orders",
}
]


orders_dag = create_domain_dag(
dag_id="domain_orders",
schedule="0 2 * * *",
start_date=datetime(2024, 1, 1),
tags=["orders", "domain"],
datasets=ORDERS_DATASETS,
sla_minutes=45,
)