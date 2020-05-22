import os


class Config:

    @staticmethod
    def get_ddb_table() -> str:
        return os.environ.get("DDB_TABLE_NAME")

    @staticmethod
    def alias_length() -> int:
        return int(os.environ.get("ALIAS_LENGTH"))

    @staticmethod
    def alias_retry() -> int:
        return int(os.environ.get('ALIAS_RETRY'))
