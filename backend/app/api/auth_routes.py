from fastapi import APIRouter, HTTPException

from app.models.user_model import (
    UserSignup,
    UserLogin
)

from app.database.mongodb import (
    users_collection
)

from app.auth.password_handler import (
    hash_password,
    verify_password
)

from app.auth.jwt_handler import (
    create_access_token
)

router = APIRouter()


@router.post("/signup")
async def signup(user: UserSignup):

    existing_user = users_collection.find_one({
        "email": user.email
    })

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = hash_password(
        user.password
    )

    users_collection.insert_one({

        "name": user.name,
        "email": user.email,
        "password": hashed_password

    })

    return {
        "message": "Signup successful"
    }


@router.post("/login")
async def login(user: UserLogin):

    existing_user = users_collection.find_one({
        "email": user.email
    })

    if not existing_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    valid_password = verify_password(
        user.password,
        existing_user["password"]
    )

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token({
        "email": existing_user["email"]
    })

    return {
        "token": token,
        "message": "Login successful"
    }