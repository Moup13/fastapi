from fastapi import FastAPI

from app.auth.base_config import auth_backend, fastapi_users
from app.auth.schemas import UserRead, UserCreate

from app.operations.router import router as router_operation

app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)