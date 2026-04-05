from env import HospitalEnv

env = HospitalEnv()

# Try: easy / medium / hard
state = env.reset("hard")

for i in range(10):

    # Simple smart decision
    if state["critical_patients"] > 0:
        action = "MOVE_TO_ICU"
    else:
        action = "ALLOCATE_BED"

    state, reward = env.step(action)
    print("Step:", i)
    print("State:", state)
    print("Reward:", reward)
    print("------")