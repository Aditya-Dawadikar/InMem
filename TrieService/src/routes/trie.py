from fastapi import APIRouter
from fastapi import HTTPException, Response, status
from database.Setup import init
from typing import Optional

from models.trie import (InsertDataRequest)

router = APIRouter(
    tags=["Trie Router"]
)

db = init()

@router.get("/")
async def fetch_trie():
    """
        This endpoint returns all the key-value pairs stored in the database
        -------------------------------------------
        Input:
            None
        -------------------------------------------
        Output:
            response_list `list`:
                List of key value pairs
    """
    op_status, data = db.describe(verbosity = False)
    if op_status != 1:
        raise HTTPException(status_code=500, detail=data)
    
    response_list = []
    for key,value in data.items():
        response_list.append(
            {
                "key": key,
                "value": value
            }
        )
    
    return {
        "success": True,
        "message": """Successfully fetched all keys""",
        "data": response_list
    }

@router.get("/search")
async def search_trie(
                        key:str=None,
                        prefix: Optional[bool]=True
                      ):
    """
        This endpoint returns all the key-value pairs that match
        the give query
        -------------------------------------------
        Input:
            key `str`:
                The key string to be matched with the records
            prefix `bool`:
                If True then perform prefix search
                If False then perform exact string matching
                Default: True
        -------------------------------------------
        Output:
            response_list `list`:
                List of key value pairs matching the input key
    """

    if key is None:
        return HTTPException(status_code=403, detail= f"""Invalid key "{key}" """)
    
    op_status= data = None
    if prefix:
        op_status, data = db.search_by_prefix(key_string=key)
    else:
        op_status, data = db.search(key_string=key)

    if op_status == -1:
        raise HTTPException(status_code=404, detail=data)
    if op_status == -2:
        raise HTTPException(status_code=403, detail=data)

    response_object = None
    
    if prefix:
        response_object = []
        for key,value in data.items():
            response_object.append(
                {
                    "key": key,
                    "value": value
                }
            )
        return {
            "success": True,
            "message": f"""Successfully found matches for key "{key}" """,
            "data": response_object
        }

    response_object = {"key":key,"value":data}
    return {
        "success": True,
        "message": f"""Successfully found key "{key}" """,
        "data": response_object
    } 

@router.post("/insert")
async def insert_trie(req_body: InsertDataRequest):
    """
        This endpoint insert a key-value pair in the database
        -------------------------------------------
        Input:
            req_body `InsertDataRequest`:
                key: key for the record
                value: value of the record 
                    Union[string, dictionary, list]
        -------------------------------------------
        Output:
            success_message
    """

    op_status,data = db.insert(key_string=req_body.key,
              value=req_body.value)

    if op_status!=1:
        return HTTPException(status_code = 403, detail=data)
    
    return {
        "success": True,
        "message": f"Successfully inserted data for key {req_body.key}",
        "data": {"key":req_body.key, "value":data}
    }

@router.delete("/delete")
async def delete_key(key:str):
    """
        This endpoint deletes a key-value pair from the database
        -------------------------------------------
        Input:
            key `str`:
                key for the record to be deleted
        -------------------------------------------
        Output:
            success_message
    """

    op_status,data = db.delete(key)

    if op_status==-1:
        return HTTPException(status_code = 404, detail=data)
    
    return {
        "success": True,
        "message": f"Successfully deleted data for key {key}",
        "data": {"key":key, "action":data}
    }
