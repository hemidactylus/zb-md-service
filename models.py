from pydantic import BaseModel
from typing import List

class BundleRequest(BaseModel):
    zb_api_key: str
