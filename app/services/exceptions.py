from fastapi import HTTPException
from starlette import status


class AlreadyExistsHTTPException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=msg if msg else "Document with specified id already exists",
        )