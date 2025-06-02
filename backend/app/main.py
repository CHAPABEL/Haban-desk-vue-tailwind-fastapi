from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.routes.auth import router as auth_router
from app.routes.login import router as login_router
from app.routes.tasks import router as tasks_router

from app.database import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    public_paths = ['/', '/reg', '/auth/login', '/login', '/openapi.json', '/docs', '/redoc']

    if any(request.url.path.startswith(path) for path in public_paths) or request.url.path.startswith('/static'):
        return await call_next(request)

    auth_header = request.headers.get('Authorization')
    if not (auth_header and auth_header.startswith('Bearer ') and len(auth_header) > 7):
       return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Not authenticated"})

    return await call_next(request)

app.include_router(auth_router)
app.include_router(login_router)
app.include_router(tasks_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)