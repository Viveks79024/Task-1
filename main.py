from fastapi import FastAPI
from routers.interaction import router

app = FastAPI(title="AI CRM HCP Module")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI CRM Backend Running"}