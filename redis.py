import json
import time
import aioredis

from datetime import date, datetime
from opsdroid.database import Database


class RedisDatabase(Database):
    async def connect(self, opsdroid):
        host = self.config["host"] if "host" in self.config else "localhost"
        port = self.config["port"] if "port" in self.config else "6379"
        database = self.config["database"] if "database" in self.config else 0
        self.client = await aioredis.create_connection(
            (host, port), db=database)

    async def put(self, key, data):
        data = self.convert_object_to_timestamp(data)
        await self.client.execute('SET', key, json.dumps(data))

    async def get(self, key):
        data = await self.client.execute('GET', key, encoding="utf-8")

        if data:
            return self.convert_timestamp_to_object(json.loads(data))

        return None

    @staticmethod
    def convert_object_to_timestamp(data):
        for k, value in data.items():
            if isinstance(value, (datetime, date)):
                value = '::'.join([
                    type(value).__name__,
                    '%d' % time.mktime(value.timetuple())
                ])
                data[k] = value
        return data

    @staticmethod
    def convert_timestamp_to_object(data):
        for k, value in data.items():
            value_type = value.split('::', 1)[0]
            timestamp = int(value.split('::', 1)[1])
            if value_type == 'datetime':
                value = datetime.fromtimestamp(timestamp)
            elif value_type == 'date':
                value = date.fromtimestamp(timestamp)
            data[k] = value
        return data
