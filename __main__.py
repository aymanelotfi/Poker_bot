from pypokerengine.api.game import setup_config, start_poker
from fish_player import FishPlayer
from heuristic_player import HeuristicPlayer
config = setup_config(max_round=2, initial_stack=100, small_blind_amount=5)
config.register_player(name="p1", algorithm=FishPlayer())
config.register_player(name="p2", algorithm=HeuristicPlayer())
game_result = start_poker(config, verbose=1)