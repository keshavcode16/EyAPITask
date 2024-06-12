from typing import Optional, List
from pydantic import BaseModel



class InputListSchema(BaseModel):
    batchid: Optional[str] 
    payload: Optional[List[List[int]]]
    
    
class ResponseSchema(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str
