# Download and Install FASTAPI
"""pip install fastapi uvicorn """
from fastapi import FastAPI
from auth import model_auth
from insert.userr import user_router
from insert.category import category_router
from insert.order import order_router
from insert.product import product_router
from update.update_userss import user_update
from delete.user import user_delete
# run fastapi
"""uvicorn main:app --reload"""

app = FastAPI()
app.include_router(model_auth)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(order_router)
app.include_router(product_router)
app.include_router(user_update)
app.include_router(user_delete)




@app.get("/")
async def intro():
    return {
        "message": "This is landing page!"
    }


@app.get("/test")
async def test1():
    return {
        "message": "Hello! "
    }


@app.get("/test2")
async def test2():
    return {
        "message": "Group -> N37. Hello"
    }


@app.get("/test3/{id}")
async def user_id(id: int):
    return {
        "Massage": f"This is user - {id}"
    }
