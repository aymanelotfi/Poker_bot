from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate

class HeuristicPlayer(BasePokerPlayer):

    def declare_action(self, valid_actions, hole_card, round_state):
        community_card = round_state['community_card']
        win_rate = estimate_hole_card_win_rate(nb_simulation=100, nb_player=2, hole_card=gen_cards(hole_card), community_card=gen_cards(community_card))

        if win_rate > 0.7:
            # Bet/Raise if win rate is high
            action, amount = valid_actions[2]['action'], valid_actions[2]['amount']['max']
        elif win_rate > 0.4:
            # Call if win rate is moderate
            action, amount = valid_actions[1]['action'], valid_actions[1]['amount']
        else:
            # Fold if win rate is low
            action, amount = valid_actions[0]['action'], 0

        return action, amount

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass
