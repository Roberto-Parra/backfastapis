from asyncio import Handle
from fastapi import FastAPI
import json
import os

app = FastAPI()

'''@app.get('/')
def mensaje():
    return {"Hello":"Mundo"}

@app.get('/login')
def mensaje():
    return "Ingrese sus datos"'''

'''@app.get('/users/{user_id}')
def mensaje(user_id):
    return f"Ingrese sus datos, el id del usuario es: {user_id}"'''

def handle(data=None) -> dict:
    event = json.loads(os.environ['REQ'])
    print(event)
    return {"result":"Mensaje recibido"}

if __name__ == "__main__":
    handle()