from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/print/{text}")
async def read_item(text: str):
    return {"text": text}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    