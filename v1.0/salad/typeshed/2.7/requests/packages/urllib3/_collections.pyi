# Stubs for requests.packages.urllib3._collections (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from collections import MutableMapping

class RLock:
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...

class RecentlyUsedContainer(MutableMapping):
    ContainerCls = ...  # type: Any
    dispose_func = ...  # type: Any
    lock = ...  # type: Any
    def __init__(self, maxsize=..., dispose_func=...) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def __len__(self): ...
    def __iter__(self): ...
    def clear(self): ...
    def keys(self): ...

class HTTPHeaderDict(dict):
    def __init__(self, headers=..., **kwargs) -> None: ...
    def __setitem__(self, key, val): ...
    def __getitem__(self, key): ...
    def __delitem__(self, key): ...
    def __contains__(self, key): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    values = ...  # type: Any
    get = ...  # type: Any
    update = ...  # type: Any
    iterkeys = ...  # type: Any
    itervalues = ...  # type: Any
    def pop(self, key, default=...): ...
    def discard(self, key): ...
    def add(self, key, val): ...
    def extend(*args, **kwargs): ...
    def getlist(self, key): ...
    getheaders = ...  # type: Any
    getallmatchingheaders = ...  # type: Any
    iget = ...  # type: Any
    def copy(self): ...
    def iteritems(self): ...
    def itermerged(self): ...
    def items(self): ...
    @classmethod
    def from_httplib(cls, message, duplicates=...): ...