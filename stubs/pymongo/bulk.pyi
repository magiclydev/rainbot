from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

from pymongo.collation import Collation
from pymongo.collection import Collection
from pymongo.errors import (BulkWriteError as BulkWriteError,
                            ConfigurationError as ConfigurationError,
                            InvalidOperation as InvalidOperation,
                            OperationFailure as OperationFailure)
from pymongo.pool import SocketInfo
from pymongo.write_concern import WriteConcern


_DELETE_ALL: int = ...
_DELETE_ONE: int = ...
_BAD_VALUE: int = ...
_UNKNOWN_ERROR: int = ...
_WRITE_CONCERN_ERROR: int = ...
_COMMANDS: Tuple[str, str, str] = ...
_UID: str = ...
_UCODE: str = ...
_UERRMSG: str = ...
_UINDEX: str = ...
_UOP: str = ...

class _Run(object):
    def __init__(self, op_type: int) -> None: ...
    def index(self, idx: int) -> int: ...
    def add(self, original_index: int, operation: Dict[str, Any]) -> None: ...

class _Bulk(object):
    def __init__(self, collection: Collection, ordered: bool, bypass_document_validation: bool) -> None: ...
    def add_insert(self, document: Dict[str, Any]) -> None: ...
    def add_update(
        self,
        selector: Dict[str, Any],
        update: Dict[str, Any],
        multi: bool = ...,
        upsert: bool = ...,
        collation: Optional[Collation] = ...) -> None: ...
    def add_replace(
        self,
        selector: Dict[str, Any],
        replacement: Dict[str, Any],
        upsert: bool = ...,
        collation: Optional[Collation] = ...) -> None: ...
    def add_delete(self, selector: Dict[str, Any], limit: int, collation: Optional[Collation] = ...) -> None: ...
    def gen_ordered(self) -> _Run: ...
    def gen_unordered(self) -> _Run: ...
    def execute_command(
        self,
        sock_info: SocketInfo,
        generator: Iterator[_Run],
        write_concern: WriteConcern) -> Dict[str, Any]: ...
    def execute_no_results(self, sock_info: SocketInfo, generator: Iterator[_Run]) -> None: ...
    def execute_legacy(self, sock_info: SocketInfo, generator: Iterator[_Run], write_concern: WriteConcern) -> None: ...
    def execute(self, write_concern: WriteConcern) -> Union[Dict[str, Any], None]: ...

class BulkUpsertOperation(object):
    def __init__(self, selector: Dict[str, Any], bulk: _Bulk, collation: Collation) -> None: ...
    def update_one(self, update: Dict[str, Any]) -> None: ...
    def update(self, update: Dict[str, Any]) -> None: ...
    def replace_one(self, replacement: Dict[str, Any]) -> None: ...

class BulkWriteOperation(object):
    def __init__(self, selector: Dict[str, Any], bulk: _Bulk, collation: Collation) -> None: ...
    def update_one(self, update: Dict[str, Any]) -> None: ...
    def update(self, update: Dict[str, Any]) -> None: ...
    def replace_one(self, replacement: Dict[str, Any]) -> None: ...
    def remove_one(self) -> None: ...
    def remove(self) -> None: ...
    def upsert(self) -> BulkUpsertOperation: ...

class BulkOperationBuilder(object):
    def __init__(self, collection: Collection, ordered: bool = ..., bypass_document_validation: bool = ...) -> None: ...
    def find(self, selector: Dict[str, Any], collation: Optional[Collation] = ...) -> BulkWriteOperation: ...
    def insert(self, document: Dict[str, Any]) -> None: ...
    def execute(self, write_concern: Optional[WriteConcern] = ...) -> Union[Dict[str, Any], None]: ...
