from typing import Optional

from pydantic import BaseModel, EmailStr


class VendedorSchemas(BaseModel):
    id: Optional[int] = None
    identificado: str 
    usuario_id: Optional[int]

    class Config:
        orm_mode = True
