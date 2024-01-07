from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def status():
    return {"messge": "ok from uvicorn server"}

@app.get("/status")
def next_app():
    return {"message": "from nextjs api"}

@app.get("/api/status")
def next_app_route():
    return {"message": "from nextjs api"}


