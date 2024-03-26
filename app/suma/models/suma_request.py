from typing import Optional
from pydantic import BaseModel

class SumaRequest(BaseModel):
  num_1: int
  num_2: int
