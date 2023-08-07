from fastapi import APIRouter
from fastapi import HTTPException, Response, status
from database.Setup import get_db, get_cache
from database.constants import DOCUMENT_STORE
from typing import Optional
from main import DB_REFERENCES

from models.trie import (InsertDocumentRequest)

router = APIRouter(
    tags=["Document Store Router"]
)

@router.get("/{db_name}")
async def fetch_documents(db_name:str):
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
    db = get_db(DB_REFERENCES, db_name, DOCUMENT_STORE)

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
        "message": """Successfully fetched all documents""",
        "data": response_list
    }

@router.get("/{db_name}/search")
async def search_documents(
                        db_name: str,
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
    db = get_db(DB_REFERENCES, db_name, DOCUMENT_STORE)

    if key is None:
        return HTTPException(status_code=403, detail= f"""Invalid key "{key}" """)
    
    op_status= data = None
    if prefix:
        op_status, data = db.search_by_prefix(key_string=key)
    else:
        # Look-up cache
        cache = get_cache(DB_REFERENCES, db_name)
        cache_response = cache.get_cache_item(key)
        if cache_response is not None:
            # increment query frequency for Cache Hit
            cache.increment_query_frequency(key)
            op_status=1
            data = cache_response
        else:
            op_status, data = db.search(key_string=key)

            # Set Cache
            cache.set_cache_item(key, data)

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

@router.post("/{db_name}/insert")
async def insert_document(db_name: str,
                    req_body: InsertDocumentRequest):
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
    db = get_db(DB_REFERENCES, db_name, DOCUMENT_STORE)

    op_status,document_id, data = db.insert(value=req_body.value)

    if op_status!=1:
        return HTTPException(status_code = 403, detail=data)

    # Set Cache
    cache = get_cache(DB_REFERENCES, db_name)
    cache.set_cache_item(document_id, {**data})

    return {
        "success": True,
        "message": f"Successfully inserted data.",
        "data": {**data}
    }

@router.delete("/{db_name}/delete")
async def delete_document(db_name: str,
                    key:str):
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
    db = get_db(DB_REFERENCES, db_name, DOCUMENT_STORE)

    op_status,data = db.delete(key)

    if op_status==-1:
        return HTTPException(status_code = 404, detail=data)

    # Remove from Cache
    cache = get_cache(DB_REFERENCES, db_name)
    cache.delete_cache_item(key)

    return {
        "success": True,
        "message": f"Successfully deleted data for key {key}",
        "data": {"key":key, "action":data}
    }
