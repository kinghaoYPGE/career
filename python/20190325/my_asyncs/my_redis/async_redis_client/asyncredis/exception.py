# -*- coding:utf-8 -*-


class RedisError(Exception):
    pass


class ConnectionError(RedisError):
    pass


class ResponseError(RedisError):
    pass
