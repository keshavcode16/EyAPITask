from typing import Any, Dict, List, Union
from app.api.v1 import schemas
from app.config import settings
from app.logs.log_handler import LibLogger
from fastapi import APIRouter, Response, status
import multiprocessing
from datetime import datetime


router: APIRouter = APIRouter()
logger: LibLogger = LibLogger()



def sum_lists(inputList):
    try:
        res = 0
        for ele in inputList:
            res += ele
        return res
    except Exception as err:
        logger.error(f"Error evaluating sum of list: {str(err)}")
        return None


@router.post("/addition",
    summary="Addition on Lists of integers",
    description="Addition on Lists of integers response as list",
    response_model=schemas.ResponseSchema,
)
async def lists_of_integers_addition(
    request_data: schemas.InputListSchema,
    response: Response
):
    """
    Addition of List containing list of integers
    """
    try:
        request_data: Dict = request_data.dict()
        batchid = request_data.get('batchid', None)
        input_List = request_data.get('payload', [])
        started_at = datetime.utcnow().isoformat()    
        with multiprocessing.Pool() as pool:
            results = pool.map(sum_lists, input_List)
            
        if any(r is None for r in results):
            raise ValueError("Error in processing some input lists.")
        
        completed_at = datetime.utcnow().isoformat()
        logger.info(f"Processed batch {batchid} successfully.")
        
        response.status_code = status.HTTP_200_OK
        return  {
            "batchid": batchid,
            "response": results,
            "status": "complete",
            "started_at": started_at,
            "completed_at": completed_at
        }
    except Exception as error:
        logger.error(f"Error in processing error")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": str(error)}
