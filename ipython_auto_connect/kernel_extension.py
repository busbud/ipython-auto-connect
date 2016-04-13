import connector


def load_ipython_extension(ipython):
    ipython.push(connector.connect_databases() or {})
    ipython.push(connector.connect_bigquery() or {})

def unload_ipython_extension(ipython):
    ipython.drop_by_id(connector.db_connections or {})
    connector.close_databases()

    ipython.drop_by_id(connector.bq_connections or {})
    connector.close_bigquery()
