from fastapi import FastAPI
from app.api.v1.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='To-do List')

app.include_router(api_router,prefix='/v1')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

