# Remember to adjust your student ID in meta.xml
from Game2048Env import Game2048Env
import random

def get_action(state, score):
    print(type(state))
    # env = Game2048Env()

    return random.choice([0, 1, 2, 3]) # Choose a random action
    
    # You can submit this random agent to evaluate the performance of a purely random strategy.
