from sqlalchemy import create_engine

class Record:
    _keys = None
    _values = None

    def __init__(self, keys, values):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def __repr__(self):
        pass

    def __getitem__(self, key):
        pass

    def __getattribute__(self, name):
        pass

class RecordCollection:
    _rows = None

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __len__(self):
        pass


def submit_query(conn, fetch_all, query, **params):
    pass