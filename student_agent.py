# Remember to adjust your student ID in meta.xml
from Game2048Env import Game2048Env
from UCTMCTS import UCTNode, UCTMCTS

def get_action(state, score):
    env = Game2048Env(state.copy(), score)
    uct_mcts = UCTMCTS(env, iterations=50, exploration_constant=1.41, rollout_depth=10)
    root = UCTNode(state.copy(), env.score)
    for _ in range(uct_mcts.iterations):
        uct_mcts.run_simulation(root)
    best_action, visit_distribution = uct_mcts.best_action_distribution(root)
    return best_action
