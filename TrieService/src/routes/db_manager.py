from fastapi import APIRouter
from fastapi import HTTPException, Response, status
from database.DBManager import (
    create_database,
    delete_database,
    change_database_status,
    get_database_list
)
from models.db_manager import (CreateNewDB)


router = APIRouter(
    tags=["Database Management Router"]
)
@router.get("/")
def get_database_records():
    """
        API to fetch all the registered databases
        -------------------------------------------
        Input:
            None
        Output:
            A list of all registered databases
    """
    db_records =  get_database_list()
    response_object = {
        "success": True,
        "message": "Successfully fetched all registered databases",
        "data": db_records,
    }
    return response_object

@router.post("/create")
def create_new_db(input_db: CreateNewDB):
    """
        API to register a new database
        -------------------------------------------
        Input:
            input_db `CreateNewDB`
                db_name `str`:
                    name of the db
                db_mode `str`:
                    string representing either the db should be
                    key-value-store or document-based 
        Output:
            new_database_object `json`
    """
    op_status, db_object = create_database(
        db_name=input_db.db_name,
        db_mode=input_db.db_mode
    )
    
    if op_status == 1:
        return {
            "success": True,
            "message": "Successfully registered new database",
            "data": db_object
        }
    else:
        raise HTTPException(status_code=500,
                            detail="Some error occured while registering database")

@router.put("/change-status")
def change_db_status(db_name:str):
    """
        API to activate/disable database
        -------------------------------------------
        Input:
            None
        Output:
            updated_db_object `json`
    """
    op_status, db_object = change_database_status(db_name)
    
    if op_status == 1:
        return {
            "success": True,
            "message": "Successfully changed database status",
            "data": db_object
        }
    elif op_status == -2:
        return HTTPException(status_code=404,
                             detail={
                                "success": False,
                                "message": db_object,
                                "data": None
                             })
    else:
        raise HTTPException(status_code=500,
                            detail="Some error occured while changing database status")

@router.delete("/delete")
def delete_db_record(db_name:str):
    """
        API to delete a registered database
        -------------------------------------------
        Input:
            db_name `str`:
                name of the database to be deleted
        Output:
            success_message
    """
    op_status, db_object = delete_database(db_name)
    
    if op_status==1:
        return {
            "success": True,
            "message": f"Successfully deleted database with name {db_name}",
            "data": None
        }
    elif op_status == -2:
        raise HTTPException(status_code=404,
                                detail={
                                "success": False,
                                "message": db_object,
                                "data": None
                            })
    else:
        raise HTTPException(status_code=500,
                            detail="Some error occured while deleting database")
