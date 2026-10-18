# TransportLive

Pipeline temps reel de surveillance des retards du transport public.

## Architecture
- Source : MBTA API (Boston) - GTFS Static + GTFS Realtime
- Ingestion : Redpanda + Spark Structured Streaming
- Stockage : Delta Lake (Medallion : Bronze, Silver, Gold)
- Transformation : dbt
- Qualite : Great Expectations + dbt tests
- Orchestration : Apache Airflow
- Visualisation : Streamlit

## Donnees
- GTFS Static : horaires theoriques (~24 MB, 2-4x/an)
- GTFS Realtime : retards temps reel (~1 MB, toutes les 30s)