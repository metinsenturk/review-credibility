import os
import urllib
from sqlalchemy import create_engine, exc
from credible.config import get_config


def connect_to_sqlite(name=None):
    """
    Local Sqlite3 database connector.
    """
    if name is None:
        name = 'db'
    sqlite_filepath = os.path.join(os.pardir, f'{name}.sqlite3')
    engine = create_engine('sqlite:///{}'.format(sqlite_filepath))

    return engine

def connect_to_methini():
    """
    Azure SQL server database connector.
    """
    config = get_config()
    con = config['con']

    # db params
    params = urllib.parse.quote_plus(
        "Driver={driver};Server={server};Database={db};\
            Uid={uid};Pwd={pwd};Encrypt=yes;TrustServerCertificate=no;\
                Connection Timeout=30;".format(
            driver=con['driver'],
            server=con['server'],
            db=con['database'],
            uid=con['uid'],
            pwd=con['pwd']
        )
    )

    # db connect
    try:
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        engine.connect()

        return engine
    except exc.DBAPIError as ex:
        raise ex
