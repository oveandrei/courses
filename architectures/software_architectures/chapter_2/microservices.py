from fastapi import FastAPI
import requests
import uvicorn
import threading

# We will create 2 different microservices
microservice1 = FastAPI()
microservice2 = FastAPI()

# Microservice 1 is the User microservice
@microservice1.get("/user/{id}")
def get_user(id: int):
    return {"id": id, "name": "Alice"}

# Microservice 2 is the Orders microservice getting the id of the user from the microservice 1.
@microservice2.get("/order/{id}")
def get_order(id: int):
    user = requests.get(f"http://localhost:8000/user/{id}")
    return {"order_id": id, "user": user.json()}


# In order to simulate this from 1 file we will have to use threading on different ports to make both 'microservices' servers to run(Separate Threads)
def run_microservice1():
    uvicorn.run(microservice1, host="127.0.0.1", port=8000) # this will run on port 8000

def run_microservice2():
    uvicorn.run(microservice2, host="127.0.0.1", port=8001) # this will run on port 8001


if __name__ == "__main__":
    # Assign Threads
    t1 = threading.Thread(target=run_microservice1) 
    t2 = threading.Thread(target=run_microservice2)

    # Start Threads
    t1.start()
    t2.start()

    t1.join()
    t2.join()

# Now if we will go on http://localhost:8001/order/1 we will see the json output  "order_id": 1, user{ id: 1, name: Alice} <- from http://localhost:8000/user/1 - Our other microservice

