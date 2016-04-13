"""
Module that looks for database and bigquery connection info in the env vars, creates connections to those
databases and loads them into the IPython environment.

DATABASE CONNECTIONS
This module uses sqlalchemy to create the connections so it has support for all the database types that
sqlalchemy supports. It looks for all env vars that end in "_DATABASE_URI", creates a connection with that
connection string and loads it under the first part of the env var with the suffix "_db" (for example
PROD_DATABASE_URI will get created and inserted under "prod_db")

BIGQUERY CONNECTIONS
Similarly, this module creates connections to bigquery using the bigquery-python package. Each connection
requires 3 env vars: "ENV_NAME_BQ_KEY", "ENV_NAME_BQ_EMAIL", "ENV_NAME_BQ_PROJECT" and will load the
client under "env_name_bq".
"""

import os


# SQL databases

db_connections = None

def connect_databases(suffix='_db', env_suffix='_DATABASE_URI'):
    global db_connections
    db_configs = {
        k[:-1 * len(env_suffix)]: v
        for k, v in os.environ.items()
        if k.endswith(env_suffix)
    }

    if db_configs:
        from sqlalchemy import create_engine
        db_connections = {
            k.lower() + suffix: create_engine(v).connect()
            for k, v in db_configs.items()
        }

    return db_connections

def close_databases():
    global db_connections
    [v.close() for k, v in db_connections.items()]
    db_connections = None


# BigQuery connections

bq_connections = None

def connect_bigquery(suffix='_bq', env_suffix='_BQ'):
    global bq_connections
    bq_configs = {
        k[:-1 * len(env_suffix + '_EMAIL')]: v
        for k, v in os.environ.items()
        if k.endswith(env_suffix + '_EMAIL')
    }

    if bq_configs:
        from bigquery import get_client
        bq_connections = {
            k.lower() + suffix: get_client(
                os.environ.get(k + env_suffix + '_PROJECT'),
                service_account=email,
                private_key=os.environ.get(k + env_suffix + '_KEY'))
            for k, email in bq_configs.items()
        }

    return bq_connections

def close_bigquery():
    global bq_connections
    bq_connections = None
