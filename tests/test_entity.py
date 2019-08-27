class TestTable:

    def __init__(self):
        self.id = None
        self.code = None


DDLCOMMAND = """
    CREATE TABLE TestTable (
    id        INTEGER      CONSTRAINT pk_role PRIMARY KEY,
    code      INTEGER
    );
    """
