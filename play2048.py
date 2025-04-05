from Game2048Env import Game2048Env
from student_agent import get_action

if __name__ == "__main__":
    env = Game2048Env()
    state = env.reset()
    # env.render()

    round_no, done = 0, False
    while not done:
        action = get_action(env.board.copy(), env.score)
        state, reward, done, _ = env.step(action)
        round_no += 1
        print("Round No.:", round_no, "Current score:", env.score)
        # env.render(action=action)  # Display the updated game state

    print("Game over, final score:", env.score)
