⚠️ DEPRECATED ⚠️ This connector is now built in to [opsdroid core](https://opsdroid.readthedocs.io/en/stable/database/redis). This repository only exists for backward compatibility and will be removed.

# opsdroid database redis

A database module for [opsdroid](https://github.com/opsdroid/opsdroid) to persist memory in a [redis database](https://redis.io/).

## Requirements

You need to install the aioredis library to use this database with opsdroid.

Run the following command in the command line:

`pip install aioredis`

## Configuration

```yaml
databases:
  - name: redis
    host:       "my host"     # (optional) default "localhost"
    port:       "12345"       # (optional) default "6379"
    database:   "7"           # (optional) default "0"
```
