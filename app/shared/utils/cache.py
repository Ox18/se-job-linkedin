from django.core.cache import cache

def set(key, value, timeout=None):
    cache.set(key, value, timeout)

def get(key):
    return cache.get(key)

def delete(key):
    cache.delete(key)