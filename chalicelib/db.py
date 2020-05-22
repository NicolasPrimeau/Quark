from abc import ABCMeta, abstractmethod
from dataclasses import asdict
from typing import Optional

import boto3
import botocore

from chalicelib.config import Config
from chalicelib.items import Alias


class DBClient(metaclass=ABCMeta):

    @abstractmethod
    def put_new_redirect(self, item: Alias) -> bool:
        pass

    @abstractmethod
    def get_redirect(self, alias: str) -> Optional[Alias]:
        pass


class DDBClient(DBClient):

    def __init__(self):
        self._table = boto3.resource('dynamodb').Table(Config.get_ddb_table())

    def put_new_redirect(self, item: Alias):
        try:
            self._table.put_item(Item=asdict(item), ConditionExpression='attribute_not_exists(alias)')
            return True
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
                raise
            return False

    def get_redirect(self, alias: str) -> Optional[Alias]:
        response = self._table.get_item(Key={'alias': alias})
        print(response)
        return Alias(**response['Item']) if response['Item'] else None
