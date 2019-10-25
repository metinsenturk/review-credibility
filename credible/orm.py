from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker

from connectors import connect_to_sqlite

@contextmanager
def session_scope():
    """
    Effective usage of session for an operation. Use `with` scope.
    """
    engine = connect_to_sqlite()
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    try:
        yield session
        session.commit()
    except Exception as ex:
        session.rollback()
        raise ex
    finally:
        session.close()