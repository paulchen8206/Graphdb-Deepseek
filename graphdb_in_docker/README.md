# Memgraph in Docker Playground

This project contains notebooks and sample datasets for learning graph databases with Memgraph, Cypher, and GQLAlchemy.

## Overview

- Run Memgraph Platform in Docker
- Connect from Python and Jupyter
- Practice graph modeling and Cypher queries with sample CSV data

## Project Files

- `notebook/1-Memgraph-Cypher.ipynb`
- `notebook/2-Memgraph-GqlAlchemy.ipynb`
- `notebook/3-Memgraph-ORE Data.ipynb`
- `notebook/4-Memgraph-Langchain.ipynb`
- `notebook/5-Memgraph-GqlAlchemy.ipynb`
- `data/movies.csv`
- `data/ratings.csv`
- `requirements.txt`

## Requirements

- Docker
- Jupyter Notebook
- Python 3.9+

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Quick Start

1. Start Memgraph Platform:

```bash
docker run -it -p 7687:7687 -p 7444:7444 -p 3000:3000 memgraph/memgraph-platform:2.4.0
```

2. Open Memgraph Lab:

- http://localhost:3000

3. Start Jupyter in this folder:

```bash
jupyter notebook
```

4. Open notebooks in order from `notebook/`.

## Loading Sample Data

If you need the CSV files inside the running container, copy them from the `data/` folder:

```bash
docker ps
docker cp data/movies.csv <CONTAINER_ID>:movies.csv
docker cp data/ratings.csv <CONTAINER_ID>:ratings.csv
```

## Learning Focus

- Graph modeling with nodes and relationships
- Cypher query language fundamentals
- Python integration using GQLAlchemy
- Graph workflows and experimentation in notebooks

## Optional Reading

- https://aws.amazon.com/nosql/graph/
- https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/
- https://db-engines.com/en/ranking
