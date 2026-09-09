from fastapi import FastAPI

from app.db.session import engine


app = FastAPI()


@app.get("/health")
def health_check():
    with engine.connect():
        return {"status": "ok"}