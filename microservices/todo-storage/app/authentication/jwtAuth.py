import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.getenv("JWT_SECRET_KEY") or "None"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 60
security = HTTPBearer()


def create_access_token(data: dict):
  to_encode = data.copy()
  expiration = datetime.now(timezone.utc) + \
      timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
  to_encode.update({"exp": expiration})
  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
  try:
    print(credentials)
    payload = jwt.decode(credentials.credentials,
                         SECRET_KEY, algorithms=[ALGORITHM])
    print(payload)
    return payload
  except JWTError:
    raise HTTPException(status_code=403, detail="Invalid token")
