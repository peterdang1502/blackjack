import numpy as np
from hand import Hand
from game import Game
from constants import *

np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)

states = []
hard_values = list(range(4, 21))
soft_values = list(range(13, 21))
split_values = list(range(4, 21, 2))
split_values.append(12) # pocket aces
player_hand_values = hard_values + soft_values + split_values
for value in player_hand_values:
    for dealer_card in CARD_RANKS:
        states.append([value, dealer_card])

# goal state
states.append([21])
goal_state = states[-2]

# bust state
states.append([22])
bust_state = states[-1]

NUM_OF_RANKS = len(CARD_RANKS)
start_of_soft_values = len(hard_values) * NUM_OF_RANKS
start_of_split_values = start_of_soft_values + len(soft_values) * NUM_OF_RANKS

def get_state_index(dealer_hand: Hand, player_hand: Hand):
    dealer_card = dealer_hand.get_cards()[1]
    dealer_rank_index = CARD_RANKS.index(dealer_card.get_rank())
    player_hand_value = player_hand.get_hand_value()
    player_can_split = player_hand.get_can_split()
    player_has_soft_ace = player_hand.has_soft_ace()
    
    curr_state_index = -3
    if player_hand_value == 21:
        curr_state_index = -2
    elif player_hand_value > 21:
        curr_state_index = -1
    elif player_can_split:
        curr_state_index = start_of_split_values + (split_values.index(player_hand_value) if not player_has_soft_ace else len(split_values) - 1) * NUM_OF_RANKS + dealer_rank_index
    elif player_has_soft_ace:
        curr_state_index = start_of_soft_values + (soft_values.index(player_hand_value) * NUM_OF_RANKS) + dealer_rank_index
    else:
        curr_state_index = hard_values.index(player_hand_value) * NUM_OF_RANKS + dealer_rank_index
    
    return curr_state_index


actions = [STAND, HIT, DOUBLE_DOWN, SPLIT]

q_table = np.zeros((len(states), len(actions)))

learning_rate = 1
discount_factor = 1
exploration_prob = 0.1
epochs = 10000000

game = Game()
for epoch in range(epochs):
    game_state = game.deal_cards()
    while game_state != IN_PLAY:
        game.return_discard()
        game_state = game.deal_cards()

    dealer_hand = game.get_player_hand(0)
    player_hand = game.get_player_hand(1)

    curr_state_index = get_state_index(dealer_hand, player_hand)
    curr_state = states[curr_state_index]
    
    while curr_state != goal_state and curr_state != bust_state:
        possible_actions = actions[:]
        if not player_hand.get_can_split():
            possible_actions.remove(SPLIT)
        if player_hand.return_num_cards() > 2:
            possible_actions.remove(DOUBLE_DOWN)

        if np.amax(q_table[curr_state_index]) == 0 or np.random.rand() < exploration_prob:
            action_index = np.random.randint(0, len(possible_actions))
        else:
            action_index = np.argmax(q_table[curr_state_index][0:len(possible_actions)])
        
        action = actions[action_index]
            
        game.player_action(action)

        next_state_index = get_state_index(game.get_player_hand(0), game.get_player_hand(1))
        next_state = states[next_state_index]

        reward = 0
        player_state = game.get_player_hand(1).get_state()
        if player_state == IN_PLAY or player_state == STAND:
            next_hand_value = next_state[0]
            reward = next_hand_value / 21
            if next_state == goal_state:
                reward = 1
            
            if player_state == STAND:
                next_state = goal_state
    
        q_table[curr_state_index, action_index] += learning_rate * (reward + discount_factor * np.max(q_table[next_state_index]) - q_table[curr_state_index, action_index])

        curr_state = next_state

    game.return_discard()
    learning_rate = 1 / (1 + 0.1 * epoch)

for i in range(len(states)):
    best = np.argmax(q_table[i])
    if np.amax(q_table[i]) != 0:
        print(states[i], actions[best])
    else:
        print(states[i], "NO BEST ACTION")