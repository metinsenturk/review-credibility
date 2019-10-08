import urllib
from sqlalchemy import create_engine, exc
from .config import get_config


def connect_to_methini():
    config = get_config()
    password = config['mssql_password']

    # db params
    params = urllib.parse.quote_plus(
        r"Driver={SQL Server};"
        r"Server=tcp:methini.database.windows.net,1433;"
        r"Database=YelpDB;Uid=methini-admin@methini;"
        r"Pwd=" + password + ";Encrypt=yes;"
        r"TrustServerCertificate=no;Connection Timeout=30;"
    )

    # db connect
    try:
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        engine.connect()

        return engine
    except exc.DBAPIError as ex:
        raise ex
