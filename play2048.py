from Game2048Env import Game2048Env
from student_agent import get_action

if __name__ == "__main__":
    env = Game2048Env()
    state = env.reset()
    # env.render()

    done = False
    while not done:
        action = get_action(env.board, env.score)
        state, reward, done, _ = env.step(action)
        # env.render(action=action)  # Display the updated game state

    print("Game over, final score:", env.score)
    