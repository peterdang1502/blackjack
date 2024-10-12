In May 2023, I embarked on a cruise to Alaska. The sights were amazing, but the cruise activities - mainly geared for people of different ages than mine - were lackluster. There was an exception: the casino. I have only ever played online poker, and the only game I knew how to play in that casino was Blackjack. After refamiliarizing myself with the rules, I sat down with $100 and watched as it dwindled away whenever I stand or hit to my own whims. Defeated and broke, I googled about playing blackjack, and I came across blackjack charts. A set of the most optimal strategies for each hand of cards, it must be the thing I need to win my $100 back and then some. Couple days after, I sat down at the table with another $100, but this time I have the charts memorized in my head. Even with strategies guiding my way, the house always wins in the end. $200 down in the hole, the seeds for this project sowed in my mind.

Obviously trying to find an optimal strategy for Blackjack now is just reinventing the wheel. That is not the purpose of this project. This is just me, teaching myself again some Object Oriented Programming, while also teaching myself Machine Learning. More specifically, this project contains a playable 1-player blackjack game on the command line (very unfleshed out), as well as using this blackjack game as a foundation to use Q-learning (reinforcement learning) to attempt to teach my program to come up with optimal strategies. Ideally afterwards, I use the strategies it learned to play some simulation games and end up with a win rate, which eventually and ideally I would like to increase with each revision of my Q-learning code. I documented below my process, as well as the troubles I ran into while doing this:


For Q-learning, there are states and actions. There is a starting state, an action that moves you to a new state, and a goal state that you want to reach. Each state-action pair is assigned a Q-value, which is basically a value representing how much you want to perform that action in that state. This Q-value is determined by a couple factors: learning rate (how much a new Q-value will override an old one), reward (how good is the next move basically), and discount factor (importance of future rewards). Q-values for each state-action pair is reevaluated whenever at that state, that action is performed. I will attach a formula somehow

First, my state consists of three cards, and the states are every possible combination of:\
    - The player cards (every possible combination of two cards)\
    - The face up dealer card\
This is because as a player, this is the only information you are given when the hands are dealt.

The actions are STAND, HIT, DOUBLE DOWN, SPLIT (have not implemented SURRENDER)

Some initial problems:\
    - There is no absolute 'win' in blackjack, when given only the initial 3 card info. There is no state where you can reach and reap a reward of absolute 1. Since the game isn't decided until the dealer plays their hands.\
    - Therefore, rewards are not deterministic, but stochastic:\
        - Instead of always trying to win in blackjack, I converted to learning how to minimize your chances of losing.\
        - This implies trying to achieve the highest hand value possible (21). This is the best case scenario of either you PUSH with the dealer or you WIN.\
        - Therefore, the reward function will reward 0 if your hand busts, and any hand value between 4 (lowest possible hand value) and 21 can be assigned a reward from 0 to 1 (lower end exclusive, higher end inclusive)\
        - Note for future implementation: blackjack dealers have to stand at HARD 17, so rewards should be rewarded heavier with hand values over 17

After implementing my states, they do not work. Since HIT and DOUBLE DOWN adds a card, your hand now has 3 cards, which is not an existing state. I switched to another solution (inspired by the charts which is kinda cheating):\
    - Each state is a total hand value, plus the dealer's face up card.\
    - There are 3 possible types of hand values:\
        - Soft hand values (has an Ace that counts as 11): values 13 to 20\
        - Hard hand values (no Ace that counts as 11): values 4 to 20\
        - Splittable hands (pocket cards): values 4 to 20, but in steps of 2\
    - Two additional states:\
        - Goal state (hand value of 21)\
        - Bust state (any hand value over 21)

The new states do work, and I've implemented the program to play games, using the charts I've produced to play the optimal decision for every hand it gets, or if there is no optimal decision, it picks a random one.\
Currently, it produces a win-rate (exclusing player and/or dealer blackjacks) of ~30-40%. There are two paths we can take for our learning model right now:\
    - Continue finetuning the learning rate, discount factor, and exploration probability to get a better winning rate
    - Change the learning model. Instead of playing a million random hands, for each hand and dealer upcard, play a million times using different random actions and compile the result to get the optimal decision.

Either way, I need to really optimize the learning process because for 1 million epochs, it takes ~30 minutes to run.

Minor problem:\
    - If the action chosen is stand, I need to end the learning episode because if a player stands, that's their final hand value  (SOLVED) \
    - Janky solution: if you stand, imma move you to the goal state but I won't reevaluate your rewards with the goal state in mind, which should end the learning episode

Current problems:\
    - How to deal with SPLIT actions (there are now 2 concurrent states to consider)\
        Possible solution: make the new hand post-split the next learning episode? But have to find a way to pause the learning loop to run this specific learning episode\
    - Decaying learning rate: No idea what the correct rates are

