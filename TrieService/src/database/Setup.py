import json
from database.Trie import Trie
from database.DocumentStore import DocumentStore
from database.constants import (KEY_VALUE_STORE,
                                DOCUMENT_STORE,
                                CACHE_SIZE,
                                CACHE_EXPIRATION)
from exceptions.errors import (ResourceNotFoundError,
                               BadRequestError)
from cache.Cache import Cache
from fastapi import HTTPException

DB_RECORD_FILE = "database/db_records.json"

def init_db(db_mode):
    db = None
    if db_mode == KEY_VALUE_STORE:
        db = Trie()
    elif db_mode == DOCUMENT_STORE:
        db = DocumentStore()
    return db

def initialize_all_tries(DB_REFERENCES):
    with open(DB_RECORD_FILE) as json_file:
        db_records = json.load(json_file)
        db_list = db_records["db_list"]
        
        for record in db_list:
            db_name = record["db_name"]
            db_mode = record["db_mode"]
            root = init_db(db_mode)
            
            DB_REFERENCES[db_name] = {
                                        "root":root,
                                        "db_mode": db_mode,
                                        "cache": Cache(
                                            db_name=db_name,
                                            max_items=CACHE_SIZE,
                                            expiration=CACHE_EXPIRATION
                                        )
                                    }
            
            if db_mode == DOCUMENT_STORE:
                if record.get("enforce_schema") is True:
                    DB_REFERENCES[db_name]["enforce_schema"] = True
                    DB_REFERENCES[db_name]["schema"] = record.get("schema")

            print(f"Successfully initialized ROOT for database {db_name}. Root: {root}")

def get_db(DB_REFERENCES, db_name, db_mode=KEY_VALUE_STORE):
    db = DB_REFERENCES.get(db_name)

    if db is None:
        raise ResourceNotFoundError(f"""Database "{db_name}" not found""")
    
    if db_mode == db["db_mode"]:
        return db["root"]
    
    err_msg = f"""Requested database "{db_name}" does not support {db_mode} mode."""
    
    raise BadRequestError(err_msg)

def get_cache(DB_REFERENCES, db_name):
    db = DB_REFERENCES.get(db_name)

    if db is None:
        raise ResourceNotFoundError(f"""Database "{db_name}" not found""")
    
    return db["cache"]

def get_schema(DB_REFERENCES, db_name):
    db = DB_REFERENCES.get(db_name)
    
    if db is None:
        raise ResourceNotFoundError(f"""Database "{db_name}" not found""")
    
    return {
        "enforce_schema": db.get("enforce_schema"),
        "schema": db.get("schema")
    }
