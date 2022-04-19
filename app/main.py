from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def mensaje():
    return {"Hello":"Mundo"}

@app.get('/login')
def mensaje():
    return "Ingrese sus datos"

@app.get('/users/{user_id}')
def mensaje(user_id):
    return f"Ingrese sus datos, el id del usuario es: {user_id}"