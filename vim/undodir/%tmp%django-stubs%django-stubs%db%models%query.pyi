Vim�UnDo� �U���@����z�ϣ��а�P���grV�   �           i                       a��    _�                     >   i    ����                                                                                                                                                                                                                                                                                                                                                             a�    �   =   ?   �      r    def bulk_update(self, objs: Iterable[_T], fields: Sequence[str], batch_size: Optional[int] = ...) -> None: ...5�_�                     >        ����                                                                                                                                                                                                                                                                                                                                                             a��     �               �   import datetime   from typing import (       Any,       Collection,   	    Dict,       Generic,       Iterable,       Iterator,   	    List,       MutableMapping,       Optional,       Reversible,       Sequence,   
    Sized,   
    Tuple,   	    Type,       TypeVar,   
    Union,       overload,   )       from django.db import models   $from django.db.models import Manager   'from django.db.models.base import Model   Ofrom django.db.models.expressions import Combinable as Combinable  # noqa: F401   /from django.db.models.expressions import F as F   =from django.db.models.query_utils import Q as Q  # noqa: F401   6from django.db.models.sql.query import Query, RawQuery       6_T = TypeVar("_T", bound=models.Model, covariant=True)   &_Row = TypeVar("_Row", covariant=True)   '_QS = TypeVar("_QS", bound="_QuerySet")       Nclass _QuerySet(Generic[_T, _Row], Collection[_Row], Reversible[_Row], Sized):       model: Type[_T]       query: Query       def __init__(           self,   2        model: Optional[Type[models.Model]] = ...,   %        query: Optional[Query] = ...,   #        using: Optional[str] = ...,   7        hints: Optional[Dict[str, models.Model]] = ...,       ) -> None: ...       @classmethod   ,    def as_manager(cls) -> Manager[Any]: ...   !    def __len__(self) -> int: ...   #    def __bool__(self) -> bool: ...   K    def __class_getitem__(cls: Type[_QS], item: Type[_T]) -> Type[_QS]: ...   1    def __getstate__(self) -> Dict[str, Any]: ...   V    # Technically, the other QuerySet must be of the same type _T, but _T is covariant   B    def __and__(self: _QS, other: _QuerySet[_T, _Row]) -> _QS: ...   A    def __or__(self: _QS, other: _QuerySet[_T, _Row]) -> _QS: ...   [    # IMPORTANT: When updating any of the following methods' signatures, please ALSO modify   .    # the corresponding method in BaseManager.   D    def iterator(self, chunk_size: int = ...) -> Iterator[_Row]: ...   I    def aggregate(self, *args: Any, **kwargs: Any) -> Dict[str, Any]: ...   9    def get(self, *args: Any, **kwargs: Any) -> _Row: ...   :    def create(self, *args: Any, **kwargs: Any) -> _T: ...       def bulk_create(   _        self, objs: Iterable[_T], batch_size: Optional[int] = ..., ignore_conflicts: bool = ...       ) -> List[_T]: ...   q    def bulk_update(self, objs: Iterable[_T], fields: Sequence[str], batch_size: Optional[int] = ...) -> int: ...   v    def get_or_create(self, defaults: Optional[MutableMapping[str, Any]] = ..., **kwargs: Any) -> Tuple[_T, bool]: ...       def update_or_create(   O        self, defaults: Optional[MutableMapping[str, Any]] = ..., **kwargs: Any       ) -> Tuple[_T, bool]: ...   R    def earliest(self, *fields: Any, field_name: Optional[Any] = ...) -> _Row: ...   P    def latest(self, *fields: Any, field_name: Optional[Any] = ...) -> _Row: ...   *    def first(self) -> Optional[_Row]: ...   )    def last(self) -> Optional[_Row]: ...   c    def in_bulk(self, id_list: Iterable[Any] = ..., *, field_name: str = ...) -> Dict[Any, _T]: ...   7    def delete(self) -> Tuple[int, Dict[str, int]]: ...   /    def update(self, **kwargs: Any) -> int: ...   !    def exists(self) -> bool: ...   Q    def explain(self, *, format: Optional[Any] = ..., **options: Any) -> str: ...       def raw(           self,           raw_query: str,           params: Any = ...,   5        translations: Optional[Dict[str, str]] = ...,   #        using: Optional[str] = ...,       ) -> RawQuerySet: ...   p    # The type of values may be overridden to be more specific in the mypy plugin, depending on the fields param   o    def values(self, *fields: Union[str, Combinable], **expressions: Any) -> _QuerySet[_T, Dict[str, Any]]: ...   u    # The type of values_list may be overridden to be more specific in the mypy plugin, depending on the fields param       def values_list(   R        self, *fields: Union[str, Combinable], flat: bool = ..., named: bool = ...        ) -> _QuerySet[_T, Any]: ...   f    def dates(self, field_name: str, kind: str, order: str = ...) -> _QuerySet[_T, datetime.date]: ...       def datetimes(   c        self, field_name: str, kind: str, order: str = ..., tzinfo: Optional[datetime.tzinfo] = ...   .    ) -> _QuerySet[_T, datetime.datetime]: ...   #    def none(self: _QS) -> _QS: ...   "    def all(self: _QS) -> _QS: ...   @    def filter(self: _QS, *args: Any, **kwargs: Any) -> _QS: ...   A    def exclude(self: _QS, *args: Any, **kwargs: Any) -> _QS: ...   9    def complex_filter(self, filter_obj: Any) -> _QS: ...       def count(self) -> int: ...   E    def union(self: _QS, *other_qs: Any, all: bool = ...) -> _QS: ...   ;    def intersection(self: _QS, *other_qs: Any) -> _QS: ...   9    def difference(self: _QS, *other_qs: Any) -> _QS: ...       def select_for_update(   k        self: _QS, nowait: bool = ..., skip_locked: bool = ..., of: Sequence[str] = ..., no_key: bool = ...       ) -> _QS: ...   ;    def select_related(self: _QS, *fields: Any) -> _QS: ...   >    def prefetch_related(self: _QS, *lookups: Any) -> _QS: ...   B    def annotate(self: _QS, *args: Any, **kwargs: Any) -> _QS: ...   ?    def alias(self: _QS, *args: Any, **kwargs: Any) -> _QS: ...   :    def order_by(self: _QS, *field_names: Any) -> _QS: ...   :    def distinct(self: _QS, *field_names: Any) -> _QS: ...   :    # extra() return type won't be supported any time soon       def extra(           self,   /        select: Optional[Dict[str, Any]] = ...,   )        where: Optional[List[str]] = ...,   *        params: Optional[List[Any]] = ...,   *        tables: Optional[List[str]] = ...,   0        order_by: Optional[Sequence[str]] = ...,   5        select_params: Optional[Sequence[Any]] = ...,   !    ) -> _QuerySet[Any, Any]: ...   &    def reverse(self: _QS) -> _QS: ...   2    def defer(self: _QS, *fields: Any) -> _QS: ...   1    def only(self: _QS, *fields: Any) -> _QS: ...   :    def using(self: _QS, alias: Optional[str]) -> _QS: ...       @property   "    def ordered(self) -> bool: ...       @property       def db(self) -> str: ...   G    def resolve_expression(self, *args: Any, **kwargs: Any) -> Any: ...   -    def __iter__(self) -> Iterator[_Row]: ...   2    def __contains__(self, x: object) -> bool: ...       @overload   .    def __getitem__(self, i: int) -> _Row: ...       @overload   4    def __getitem__(self: _QS, s: slice) -> _QS: ...   1    def __reversed__(self) -> Iterator[_Row]: ...       'class RawQuerySet(Iterable[_T], Sized):       query: RawQuery       def __init__(           self,   (        raw_query: Union[RawQuery, str],   2        model: Optional[Type[models.Model]] = ...,   %        query: Optional[Query] = ...,   !        params: Tuple[Any] = ...,   5        translations: Optional[Dict[str, str]] = ...,           using: str = ...,   7        hints: Optional[Dict[str, models.Model]] = ...,       ) -> None: ...   !    def __len__(self) -> int: ...   +    def __iter__(self) -> Iterator[_T]: ...   #    def __bool__(self) -> bool: ...       @overload   ,    def __getitem__(self, k: int) -> _T: ...       @overload   -    def __getitem__(self, k: str) -> Any: ...       @overload   ;    def __getitem__(self, k: slice) -> RawQuerySet[_T]: ...       @property   '    def columns(self) -> List[str]: ...       @property       def db(self) -> str: ...   +    def iterator(self) -> Iterator[_T]: ...       @property   1    def model_fields(self) -> Dict[str, str]: ...   E    def prefetch_related(self, *lookups: Any) -> RawQuerySet[_T]: ...   a    def resolve_model_init_order(self) -> Tuple[List[str], List[int], List[Tuple[str, int]]]: ...   A    def using(self, alias: Optional[str]) -> RawQuerySet[_T]: ...       QuerySet = _QuerySet[_T, _T]       class Prefetch(object):   r    def __init__(self, lookup: str, queryset: Optional[QuerySet] = ..., to_attr: Optional[str] = ...) -> None: ...   1    def __getstate__(self) -> Dict[str, Any]: ...   2    def add_prefix(self, prefix: str) -> None: ...   =    def get_current_prefetch_to(self, level: int) -> str: ...   E    def get_current_to_attr(self, level: int) -> Tuple[str, str]: ...   I    def get_current_queryset(self, level: int) -> Optional[QuerySet]: ...       pdef prefetch_related_objects(model_instances: Iterable[_T], *related_lookups: Union[str, Prefetch]) -> None: ...   hdef get_prefetcher(instance: Model, through_attr: str, to_attr: str) -> Tuple[Any, Any, bool, bool]: ...       "class InstanceCheckMeta(type): ...   5class EmptyQuerySet(metaclass=InstanceCheckMeta): ...5��