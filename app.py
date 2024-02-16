from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/print/{text}")
async def read_item(text: str):
    return {"text": text}

