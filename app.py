from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, "Portfolio-Chatbot")
sys.path.append(module_dir)

import Chatbot

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Chatbot.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=10000)