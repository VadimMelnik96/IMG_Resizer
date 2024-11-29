from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: str
    image_url: str | None = None
