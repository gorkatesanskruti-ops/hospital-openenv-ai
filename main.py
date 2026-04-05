from env import HospitalEnv

env = HospitalEnv()
state = env.reset()

for i in range(5):
    state, reward = env.step("ALLOCATE_BED")
    print(state, reward)