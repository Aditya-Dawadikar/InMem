from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from config import PORT

from database.Setup import initialize_all_tries

app = FastAPI()

DB_REFERENCES = {}
initialize_all_tries(DB_REFERENCES)

@app.get("/ping")
def ping():
    return JSONResponse(
        content={
            "success": True,
            "message":"Successfully Reached Server",
            "data": None,
            },
        status_code=200
    )

from routes.db_manager import router as db_manager_router
from routes.trie import router as trie_router
from routes.document_store import router as document_store_router

app.include_router(db_manager_router, prefix="/manage-db")
app.include_router(trie_router, prefix="/key-value-store")
app.include_router(document_store_router, prefix="/document-store")

if __name__=="__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=PORT,
                reload=True)