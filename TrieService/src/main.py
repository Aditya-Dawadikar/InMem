from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from config import PORT

from routes.trie import router as trie_router
from routes.db_manager import router as db_manager_router

app = FastAPI()

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

app.include_router(trie_router, prefix="/database")
app.include_router(db_manager_router, prefix="/manage-db")

if __name__=="__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=PORT,
                reload=True)