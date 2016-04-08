# Module that looks for database and bigquery connection info in the env vars, creates connections to those
# databases and loads them into the IPython environment.
#
# DATABASE CONNECTIONS
# This module uses sqlalchemy to create the connections so it has support for all the database types that
# sqlalchemy supports. It looks for all env vars that end in "_DATABASE_URI", creates a connection with that
# connection string and loads it under the first part of the env var with the suffix "_db" (for example
# PROD_DATABASE_URI will get created and inserted under "prod_db")
#
# BIGQUERY CONNECTIONS
# Similarly, this module creates connections to bigquery using the bigquery-python package. Each connection
# requires 3 env vars: "ENV_NAME_BQ_KEY", "ENV_NAME_BQ_EMAIL", "ENV_NAME_BQ_PROJECT" and will load the
# client under "env_name_bq".


from sqlalchemy import create_engine
from bigquery import get_client
import os
import re

db_connections = {}

def load_ipython_extension(ipython):
    db_connections = {k[:-1 * len("_DATABASE_URI")].lower() + "_db":create_engine(v).connect() for k, v in os.environ.items() if k.endswith("_DATABASE_URI")}

    ipython.push(db_connections, interactive=True)
    bigquery_envs = [x[:x.index("_BQ_EMAIL")] for x in os.environ.keys() if "_BQ_EMAIL" in x]
    bigquery_connections = {}

    for env in bigquery_envs:
        key = os.environ[env + "_BQ_KEY"]
        email = os.environ[env + "_BQ_EMAIL"]
        project = os.environ[env + "_BQ_PROJECT"]

        bigquery_connections[env.lower() + "_bq"] = get_client(project, service_account=email, private_key=key)
    ipython.push(bigquery_connections, interactive=True)


def unload_ipython_extension(ipython):
    print "Closing Connections"
    [v.close() for k, v in db_connections.items()]
