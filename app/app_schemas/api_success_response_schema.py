from typing import TypedDict, TypeVar, Generic
T = TypeVar('T')
M = TypeVar('M')

class ApiSuccessResponseWithMetaData(TypedDict, Generic[T, M]):
    data: T
    metaData: M
class ApiSuccessResponse(TypedDict, Generic[T]):
    data: T


class ApiSuccessResponseAccessToken(TypedDict):
    access_token:str