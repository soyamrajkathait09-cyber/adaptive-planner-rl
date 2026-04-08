from fastapi import FastAPI
import numpy as np

app = FastAPI()

# ---- ENVIRONMENT ----
class AdaptivePlannerEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.time = 0
        self.energy = 100
        self.tasks = [
            {"deadline": 5, "done": 0, "priority": 2},
            {"deadline": 8, "done": 0, "priority": 1},
        ]
        return self._get_state()

    def _get_state(self):
        return [
            self.time,
            self.energy,
            self.tasks[0]["deadline"],
            self.tasks[1]["deadline"],
            sum(t["done"] for t in self.tasks),
        ]

    def step(self, action):
        reward = 0

        # ---- ACTION LOGIC ----
        if action == 0 and self.tasks[0]["done"] == 0:
            self.tasks[0]["done"] = 1
            reward += 10

        elif action == 1 and self.tasks[1]["done"] == 0:
            self.tasks[1]["done"] = 1
            reward += 8

        elif action == 2:
            reward -= 2

        elif action == 3:
            self.energy = min(100, self.energy + 15)
            reward += 3

        # ---- TIME + ENERGY ----
        self.time += 1
        self.energy -= 5

        # ---- LOW ENERGY PENALTY ----
        if self.energy < 20:
            reward -= 3

        # ---- DONE CONDITION ----
        done = self.time >= 12

        return self._get_state(), reward, done


# ---- INIT ENV ----
env = AdaptivePlannerEnv()


# ---- API ENDPOINTS (OPENENV FORMAT) ----

@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "observation": state
    }


@app.post("/step")
def step(action: int):
    state, reward, done = env.step(action)
    return {
        "observation": state,
        "reward": reward,
        "done": done,
        "info": {}
    }
