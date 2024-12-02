import uvicorn
from fastapi import FastAPI

from routers.cat import cats_router
from routers.mission import missions_router

app = FastAPI()

app.include_router(cats_router)
app.include_router(missions_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app")
