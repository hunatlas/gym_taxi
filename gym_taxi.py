import gym
import pickle

env = gym.make("Taxi-v3", render_mode="human")

pickle_in = open("taxi_policy", "rb")
policy = pickle.load(pickle_in)
pickle_in.close()

state = env.reset()[0]
rewards = 0
for step in range(1000):
    if step % 10 == 0:
        print(f'{step}/1000 steps')
    action = policy[state]
    new_state, reward, done, _, _ = env.step(action)
    rewards += reward
    state = new_state
    if done:
        print(f'Round over, rewards: {rewards}')
        state = env.reset()[0]
env.close()

print(f'Simulation over, rewards: {rewards}')