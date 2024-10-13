from typing import TypedDict, TypeVar, Generic
T = TypeVar('T')
M = TypeVar('M')

class ApiSuccessResponseWithMetaData(TypedDict, Generic[T, M]):
    data: T
    metaData: M

class ApiSuccessResponseAccessToken(TypedDict):
    access_token:str