from fastapi import HTTPException
from starlette import status


class AlreadyExistsHTTPException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=msg)


class NotFoundHTTPException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=msg)
