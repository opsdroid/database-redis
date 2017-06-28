# opsdroid database redis

A database module for [opsdroid](https://github.com/opsdroid/opsdroid) to persist memory in a [redis database](https://redis.io/).

## Requirements

None.

## Configuration

```yaml
databases:
  mongo:
    host:       "my host"     # (optional) default "localhost"
    port:       "12345"       # (optional) default "6379"
    database:   "7"           # (optional) default "0"
```

## License

GNU General Public License Version 3 (GPLv3)