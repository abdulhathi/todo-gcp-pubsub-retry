from fastapi import APIRouter
from app.authentication.jwtAuth import create_access_token

router = APIRouter()


@router.get("/login")
def login():
  token = create_access_token({"user": "admin"})
  return {"access_token": token, "token_type": "brearer"}
