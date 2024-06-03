import sys

sys.path.append(".")

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates
import uvicorn

from routers.auth import auth
template = Jinja2Templates(directory="templates")

app = FastAPI()

origins = {
    "http://localhost:3000",
    "http://localhost:3000/reg"
}
app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)


app.include_router(auth.router)




if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True,)
