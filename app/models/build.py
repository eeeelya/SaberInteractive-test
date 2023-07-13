from pydantic import BaseModel


class BuildName(BaseModel):
    name: str
