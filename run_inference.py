import os
from openai import OpenAI
from env.environment import HospitalEnv

client = OpenAI(api_key=os.getenv("HF_TOKEN"))

def run():
    env = HospitalEnv()
    obs = env.reset()
    total = 0

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": str(obs)}]
        )

        action_output = response.choices[0].message.content

        action = type("Action", (), {
            "action_type": "text",
            "output": action_output
        })

        obs, reward, done, _ = env.step(action)
        total += reward.score

        if done:
            break

    print("Final Score:", total)

if __name__ == "__main__":
    run()