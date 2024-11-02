from pydantic import BaseModel

class DeviceSchema(BaseModel):
    device_id: int
    device_name: str
    description: str

    class Config:
        orm_mode = True