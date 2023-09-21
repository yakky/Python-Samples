from enum import Enum
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class ResponseModel(BaseModel):
    model_name: ModelName
    message: str


app = FastAPI()


@app.get("/models/")
async def get_models() -> list[str]:
    return [model.value for model in ModelName]


@app.get("/models/{model_name}", response_model=ResponseModel)
async def get_model(model_name: ModelName) -> Any:
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
