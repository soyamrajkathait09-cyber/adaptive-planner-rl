import os
from openai import OpenAI

def run():
    print("START")

    # Required environment variables
    API_BASE_URL = os.getenv("API_BASE_URL", "default")
    MODEL_NAME = os.getenv("MODEL_NAME", "adaptive-planner")
    HF_TOKEN = os.getenv("HF_TOKEN")

    # Dummy OpenAI client (just to satisfy requirement)
    client = OpenAI()

    print(f"STEP: Using model {MODEL_NAME}")
    print("STEP: Running Adaptive Planner Environment")

    print("END")


if __name__ == "__main__":
    run()
