from FASTAPI import FastAPI # type: ignore
from database import engine, Base
import routes.user # type: ignore
from routes.task import router as task_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(routes.user.router)
app.include_router(task_router)

@app.get("/")
def home():
    return {"message": "Backend running clean"}