# Supply Chain ETL Pipeline

An end-to-end ETL pipeline for supply chain analytics. Built around the DataCo Smart Supply Chain dataset, this project ingests raw order and shipment data, transforms it into a clean analytical schema, and serves it to a Power BI dashboard for delivery performance analysis.

This is a learning project I'm building toward a fall data engineering co-op. I'm developing it in versions — v1 ships a working local pipeline, and each subsequent version adds a layer of production-grade infrastructure (cloud storage, orchestration, data quality, deployment).

## Current status: v1 (in progress)

Local pipeline running on a single CSV. Manual runs.

- [ ] Extract: load DataCo CSV
- [ ] Transform: clean and reshape with pandas
- [ ] Load: write to SQLite
- [ ] Dashboard: Power BI connected to SQLite

## Roadmap

- **v1 (current):** Local CSV → Python ETL → SQLite → Power BI
- **v2:** Migrate to PostgreSQL, ingest from AWS S3, add logging + config + pytest
- **v3:** Add weather API as second source, refactor into a star schema, orchestrate with Airflow
- **v4:** Incremental loads, data quality monitoring, deployment

## Tech stack

- Python 3.14
- pandas
- SQLAlchemy + SQLite
- Power BI

## Data source

[DataCo Smart Supply Chain](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) — ~180K supply chain transactions with order, shipment, delivery, customer, and product information.

The CSV is not committed to this repo. Download it from Kaggle and place it in `data/raw/`.

## How to run it

> Setup instructions will be finalized once v1 is complete.

```bash
git clone https://github.com/U-Ekene/supply-chain-etl-pipeline-project.git
cd supply-chain-etl-pipeline-project
python -m venv .venv
source .venv/Scripts/activate    # Windows Git Bash
pip install -r requirements.txt
python -m src.pipeline
```

## Project structure

```
supply-chain-etl-pipeline-project/
├── src/              # ETL code (extract, transform, load, pipeline)
├── sql/              # Schema definitions
├── notebooks/        # Exploration
├── dashboards/       # Power BI files
├── data/             # Raw and processed data (gitignored)
├── db/               # SQLite database (gitignored)
├── docs/             # Architecture diagrams
└── tests/            # Test suite (added in v2)
```

## Architecture

Architecture diagram will be added once v1 is complete. For v1, the flow is:

`DataCo CSV → Python ETL (pandas) → SQLite → Power BI dashboard`

## Notes

This README will grow as the project develops. Implementation notes, decisions, and things I run into will be logged here as I hit them.