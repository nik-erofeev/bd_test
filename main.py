import uvicorn
from fastapi import FastAPI

from routers.handlers import router

app = FastAPI(title="Test", version="1.1")


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
