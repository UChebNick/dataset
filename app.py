import fastapi
from fastapi import FastAPI
import uvicorn
from fastapi.responses import FileResponse
app = fastapi.FastAPI()



@app.get("/my_data")
def check_admin():
    return FileResponse(path="my_data.npy")

@app.get("/my_targets")
def check_admin():
    return FileResponse(path="my_targets.npy")

uvicorn.run(app, host='0.0.0.0', port=5000)