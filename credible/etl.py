
from contextlib import contextmanager


class Etl:
    def __init__(self, Base, Session, engine):
        """
        Custom etl wrapper for SqlAlchemy. Implements Basic ETL operations for tables.
        """
        self.Base = Base
        self.Session = Session
        self.engine = engine

    def create_all(self, drop_all=True):
        """
        Create all tables.
        """
        if drop_all:
            self.Base.metadata.drop_all(bind=self.engine)
        self.Base.metadata.create_all(bind=self.engine)

    def insert(self, obj_list, batch_size=-1):
        """
        Insert function.
        """
        if batch_size == -1:
            with self.session_scope() as session:
                session.add_all(obj_list)
        else:
            # todo: divide obj_list into batches, insert in loop.
            pass

    def bulk_insert(self, mapper, mappings, *args):
        """
        Bulk insert wrapper of SqlAlchemy.
        """

        with self.session_scope() as session:
            if issubclass(mappings[0].__class__, self.Base):
                session.bulk_save_objects(mappings)
            else:
                session.bulk_insert_mappings(mapper, mappings, *args)

    @contextmanager
    def session_scope(self):
        """
        Effective usage of session for an operation. Use `with` scope.
        """
        session = self.Session()

        try:
            yield session
            session.commit()
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            session.close()
