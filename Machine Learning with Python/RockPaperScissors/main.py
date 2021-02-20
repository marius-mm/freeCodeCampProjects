# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

#play(player, quincy, 1000)
#play(player, abbey, 1000)
#play(player, kris, 1000)
#play(player, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
#play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)
"""
x = 0
j = 0
for i in range(1000):
    y = play(player,abbey,1000)
    if y > x : 
        x = y
        j = i

print("Highest Winrate{} with memorylength {}".format(x,j))        
"""
# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)