from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from config import PORT

from exceptions.http_exceptions import add_http_exception_handlers

from database.Setup import initialize_all_tries
from database.Cleanup import kill_cache_threads

app = FastAPI()

# Initialize Registered DBs and Cache
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
from routes.auth import router as auth_router

app.include_router(db_manager_router, prefix="/manage-db")
app.include_router(trie_router, prefix="/key-value-store")
app.include_router(document_store_router, prefix="/document-store")
app.include_router(auth_router, prefix="/auth")

add_http_exception_handlers(app)

@app.on_event("shutdown")
async def on_shutdown():
    kill_cache_threads(DB_REFERENCES)

if __name__=="__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=PORT,
                reload=True)