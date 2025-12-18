# Advanced Airflow Orchestration Platform
## Purpose of This Project

This project is designed to demonstrate expert-level Apache Airflow usage beyond simple scheduling. It focuses on dynamic DAGs, cross-pipeline dependencies, sensors, failure isolation, and operational scalability.

Where Project 1 proves end-to-end data platform design, Project 2 proves orchestration mastery.

## Business Problem

As data platforms grow, teams encounter:

- Hundreds of similar pipelines with copy‑pasted DAGs
- Tight coupling between pipelines
- Cascading failures and unclear ownership
- Poor observability across domains

The goal is to build an orchestration layer that:

- Scales to many datasets without code duplication
- Clearly models dependencies across pipelines
- Is resilient to partial failures
- Is easy for teams to extend safely

## High-Level Architecture

Airflow as a Control Plane

- Dynamic DAG factory generates pipelines per dataset
- Sensors coordinate cross‑DAG and external dependencies
- TaskGroups enforce consistent structure
- Custom operators encapsulate cloud interactions

No business logic lives in DAGs — orchestration only.

## Core Features Demonstrated
### 1. Dynamic DAG Generation

- DAGs created from YAML / Python config
- One codebase → many pipelines
- Standardized schedules, retries, and SLAs

### 2. Cross‑DAG Dependencies

- ExternalTaskSensor usage
- Upstream/downstream domain boundaries
- Explicit dependency contracts

### 3. Failure Isolation & Recovery

- Partial retries at task level
- Domain‑scoped failure handling
- Safe backfills without global re‑runs

### 4. Observability

- Clear naming conventions
- TaskGroup‑based visualization
- SLA miss detection and alert hooks

### Example Use Case

- Orders pipeline depends on Customers pipeline
- Customers ingestion completes first
- Orders DAG waits using ExternalTaskSensor
- Failure in Orders does not block Customers