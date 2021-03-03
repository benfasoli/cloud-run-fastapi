from fastapi import FastAPI, Response, status

from .routers import example


app = FastAPI(
    title="Cloud Run FastAPI template",
    description="A starter template for FastAPI backends for Google Cloud Run deployments",
    version="0.1.0",
    docs_url='/',
    openapi_url='/openapi.json',
    redoc_url=None
)


@app.get('/health',
         summary='Verify API is healthy')
async def health():
    """Returns a response code of 200 if API is online."""
    return Response(status_code=status.HTTP_200_OK)


app.include_router(example.router, tags=['example'])
