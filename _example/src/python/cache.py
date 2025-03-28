from __future__ import annotations

from functools import wraps


def cache_factory():
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(data, predicate):
            key = (id(predicate), tuple(data))
            if key in cache:
                print(f"{data},{predicate}: Cache hit")
                return cache[key]

            cache[key] = [item for item in data if predicate(item)]
            return cache[key]

        return wrapper

    return decorator

cache = cache_factory()

@cache
def itrany(data, predicate):
    for item in data:
        if predicate(item):
            return True


print(itrany([1, 2, 3], lambda x: x % 2 == 0))
print(itrany([1, 2, 3], lambda x: x % 2 == 0)) # cache hit
print(itrany([1, 2, 4], lambda x: x % 2 == 0))
