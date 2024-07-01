from fastapi import FastAPI
from web.routes import film

app = FastAPI()

app.include_router(film.router)


@app.get("/health")
async def root():
    return {"message": "SEX"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
