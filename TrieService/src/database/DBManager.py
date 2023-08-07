import json
from datetime import timezone
import datetime
import threading

DB_RECORD_FILE = f"database/db_records.json"

# Secure file lock for concurrent writes 
file_lock = threading.Lock()

def get_timestamp():
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp

def create_database(db_name, db_mode="key-value-store"):
    """
        Registers a new database by securing a file lock
        -------------------------------------------
        Error Codes:
            1: Success
            -1: Some error occured
            -2: Invalid Input
    """
    new_db_record = {
        "db_name": db_name,
        "db_mode": db_mode,
        "db_status": "active",
        "created_at": get_timestamp()
    }
    db_version = None
    with file_lock:
        with open(DB_RECORD_FILE, 'r+') as json_file:
            db_records = json.load(json_file)
            db_version = db_records["version"]
            db_records["db_list"].append(new_db_record)
            
            json_data = json.dumps(db_records, indent=4)
            print(json_data)
            
            json_file.seek(0)
            json_file.truncate()
            
            json_file.write(json_data)

    return 1, {**new_db_record, "version": db_version}

def get_database_list():
    """
        Returns the database records
        -------------------------------------------
    """
    with open(DB_RECORD_FILE) as json_file:
        db_records = json.load(json_file)
        return db_records

def delete_database(db_name:str):
    """
        Deletes a database by securing a file lock
        -------------------------------------------
        Error Codes:
            1: Success
            -1: Some error occured
            -2: Invalid Input
    """
    with file_lock:
        with open(DB_RECORD_FILE, 'r+') as json_file:
            db_records = json.load(json_file)
            
            db_found = False
            new_db_list = []
            for db in db_records["db_list"]:
                if db["db_name"] != db_name:
                    new_db_list.append(db)
                elif db["db_name"] == db_name:
                    db_found = True
            
            if not db_found:
                return -2, f"Database with name {db_name} not found"

            db_records["db_list"] = new_db_list
            json_data = json.dumps(db_records, indent=4)
            print(json_data)
            
            json_file.seek(0)
            json_file.truncate()
            
            json_file.write(json_data)

    return 1, "Successfully Deleted database"

def change_database_status(db_name: str):
    """
        Updates a database status by securing a file lock
        -------------------------------------------
        Error Codes:
            1: Success
            -1: Some error occured
            -2: Invalid Input
    """
    with file_lock:
        with open(DB_RECORD_FILE, 'r+') as json_file:
            db_records = json.load(json_file)
            db_list = db_records["db_list"]
            
            db_found = False
            db_object = None
            for i in range(len(db_list)):
                if db_list[i]["db_name"] == db_name:
                    if db_list[i]["db_status"] == "active":
                        db_list[i]["db_status"] = "disabled"
                    else:
                        db_list[i]["db_status"] = "active"
                    
                    db_found = True
                    db_object = db_list[i]
                    break
            
            if not db_found:
                return -2, f"Database with name {db_name} not found"
                
            db_records["db_list"] = db_list
            json_data = json.dumps(db_records, indent=4)
            print(json_data)
            
            json_file.seek(0)
            json_file.truncate()
            
            json_file.write(json_data)

    return 1, db_object
