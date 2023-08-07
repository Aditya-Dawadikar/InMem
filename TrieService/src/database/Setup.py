import json
from database.Trie import Trie
from fastapi import HTTPException

DB_RECORD_FILE = "database/db_records.json"

def init():
    trie = Trie()
    return trie

def initialize_all_tries(DB_REFERENCES):
    with open(DB_RECORD_FILE) as json_file:
        db_records = json.load(json_file)
        db_list = db_records["db_list"]
        
        for record in db_list:
            db_name = record["db_name"]
            root = init()
            DB_REFERENCES[db_name] = root

            print(f"Successfully initialized Trie for database {db_name}. Root: {root}")

def get_db(DB_REFERENCES, db_name):
    db = DB_REFERENCES.get(db_name)
    if db is None:
        raise HTTPException(status_code=404, detail= f"""Database "{db_name}" not found""")
    
    return db
