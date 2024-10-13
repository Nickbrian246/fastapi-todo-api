from typing import Callable, Any
from prisma.errors import PrismaError, UniqueViolationError,RecordNotFoundError
from functools import wraps
from fastapi import HTTPException, status

def authErrorHandler(callback: Callable[..., Any]):
    @wraps(callback)
    async def wrapper(*args, **kwargs):
        try:
            return await callback(*args, **kwargs)
        except UniqueViolationError as e:
            # Error específico de violación de unicidad
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=f"{e}"
            )
        except RecordNotFoundError as e:
            # Error específico de record not found
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Record not found"
            )
        except PrismaError as e:
            # Manejo de otros errores de Prisma
            print({"prisma errores":e})
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Database error occurred."
            )
        except HTTPException as e:
                raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"{e.detail}"
            )
        except Exception as e:
            print({"error from decorator":e})
            # Manejo de errores generales
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred."
            )
    return wrapper