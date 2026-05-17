from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class JWTBearer(HTTPBearer):

    async def __call__(
        self,
        request: Request
    ):

        credentials = await super().__call__(request)

        if credentials:

            try:

                payload = jwt.decode(
                    credentials.credentials,
                    SECRET_KEY,
                    algorithms=[ALGORITHM]
                )

                return payload

            except JWTError:

                raise HTTPException(
                    status_code=403,
                    detail="Invalid token"
                )