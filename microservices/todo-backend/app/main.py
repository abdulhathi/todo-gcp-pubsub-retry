import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api import todo
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Todo API",
              description="Backend for Todo list with firestore + pub/sub",
              version="1.0.0")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


app.include_router(todo.router, prefix="/api/todos", tags=["Todos"])


@app.get("/health")
def health():
  return {"status": "ok"}

# Startup event


# Shutdown event