#!/usr/bin/env python3
"""
we are caching using redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: bytes,
            fn: Optional[Callable] = None) -> Optional[Union[
                str, bytes, int, float]]:
        """
        we are getting from redis
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        converting bytes into str directly
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        converting bytes to int
        """
        return self.get(key, fn=int)
