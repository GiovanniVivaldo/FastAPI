from fastapi import APIRouter

user = APIRouter()

@user.get('/users/')
def get_users():
    return {"Get"}

@user.get('/users/{id}')
def get_users():
    return {"Get"}

@user.post('/users/')
def create_users():
    return {"crear"}

@user.put('/users/{id}')
def update_users():
    return {"modificar"}

@user.delete('/users/{id}')
def delete_users():
    return {"eliminar"}
