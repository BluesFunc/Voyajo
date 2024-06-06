import sys

sys.path.append(".")

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers.auth import auth
from routers.admin import admin
from routers.distributing import distributing

app = FastAPI()

origins = {
    "*",
  
}
app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)


app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(distributing.router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
