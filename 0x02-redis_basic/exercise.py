#!/usr/bin/env python3
"""
we are caching using redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    this class is a caching blueprint
    """
    def __init__(self):
        """
        this method is an initialization
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        this is a storing function
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
