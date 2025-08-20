from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import health, ponds  # you can add measures later

app = FastAPI(
    title="Aquatrade API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])               # e.g. GET /health
app.include_router(ponds.router, prefix="/ponds", tags=["Ponds"]) # GET/POST /ponds

@app.get("/")
def read_root():
    return {"message":"Welcome to Aquatrade API","version":"0.1.0","docs":"/docs","health":"/health"}
