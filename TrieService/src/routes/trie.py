import traceback
from fastapi import APIRouter
from fastapi import HTTPException
from typing import Optional
from database.Setup import get_db, get_cache
from main import DB_REFERENCES
from exceptions.errors import (
    InternalServerError,
    ValidationError,
    ResourceNotFoundError,
    BadRequestError
)
from exceptions.http_exceptions import (BadRequestException,
                                        ResourceNotFoundException,
                                        InternalServerErrorException)

from models.trie import (InsertDataRequest)

router = APIRouter(
    tags=["Key Value Store Router"]
)

@router.get("/{db_name}")
async def fetch_trie(db_name:str):
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
    try:
        db = get_db(DB_REFERENCES, db_name)

        op_status, data = db.describe(verbosity = False)
        if op_status != 1:
            raise Exception("Some error occured while fetching records")
        
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
    except ResourceNotFoundError as e:
        raise ResourceNotFoundException(str(e)) from e
    except BadRequestError as e:
        raise BadRequestException(str(e)) from e
    except Exception as e:
        print(traceback.format_exc())
        raise InternalServerErrorException(str(e))

@router.get("/{db_name}/search")
async def search_trie(
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
    try:
        db = get_db(DB_REFERENCES, db_name)

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
            raise ResourceNotFoundError(data)
        if op_status == -2:
            raise BadRequestError(data)

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
    except ResourceNotFoundError as e:
        raise ResourceNotFoundException(str(e)) from e
    except BadRequestError as e:
        raise BadRequestException(str(e)) from e
    except Exception as e:
        print(traceback.format_exc())
        raise InternalServerError(str(e))

@router.post("/{db_name}/insert")
async def insert_trie(db_name: str,
                    req_body: InsertDataRequest):
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
    try:
        db = get_db(DB_REFERENCES, db_name)

        db_value = {}

        schema_config = get_schema(DB_REFERENCES, db_name)
        if schema_config.get("enforce_schema") is True:
            if schema_config.get("schema") is not None:
                validate_data(schema_config.get("schema"), req_body)
                db_value = serialize_data(schema_config.get("schema"), req_body)
        else:
            db_value = req_body.value

        op_status,data = db.insert(key_string=req_body.key,
                value=db_value)

        if op_status!=1:
            raise BadRequestError(data)

        # Set Cache
        cache = get_cache(DB_REFERENCES, db_name)
        cache.set_cache_item(req_body.key, data)

        return {
            "success": True,
            "message": f"Successfully inserted data for key {req_body.key}",
            "data": {"key":req_body.key, "value":data}
        }
    except ResourceNotFoundError as e:
        raise ResourceNotFoundException(str(e)) from e
    except Exception as e:
        print(traceback.format_exc())
        raise InternalServerErrorException(str(e))

@router.delete("/{db_name}/delete")
async def delete_key(db_name: str,
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
    try:
        db = get_db(DB_REFERENCES, db_name)

        op_status,data = db.delete(key)

        if op_status==-1:
            raise ResourceNotFoundError(data)

        # Remove from Cache
        cache = get_cache(DB_REFERENCES, db_name)
        cache.delete_cache_item(key)

        return {
            "success": True,
            "message": f"Successfully deleted data for key {key}",
            "data": {"key":key, "action":data}
        }
    except ResourceNotFoundError as e:
        raise ResourceNotFoundException(str(e))
    except Exception as e:
        print(traceback.format_exc())
        raise InternalServerErrorException(str(e))
