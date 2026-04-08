from fastapi import FastAPI
from app.env import EmailTriageEnv
from app.models import Action

app = FastAPI()
env = EmailTriageEnv(task="medium")


@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return env.state