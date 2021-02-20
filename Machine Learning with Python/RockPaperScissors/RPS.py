# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
import mchmm as mc
import numpy as np

winDict = {"R": "P", "S": "R", "P": "S"}

strategy = 1


def player(prev_play, opponent_history=[]):
    global strategy
    # firstCall
    if len(opponent_history) <= 0:
        opponent_history.append("R")
        opponent_history.append("S")
    if len(prev_play) <= 0:
        prev_play = "P"
    # /firstCall

    opponent_history.append(prev_play)

    if strategy == 1:
        memory = 800
        guess = predict(prev_play, opponent_history, memory)

    return guess


def predict(prev_play, oppnent_history, memoryLength):
    if len(oppnent_history) > memoryLength:
        oppnent_history.pop(0)

    chain = mc.MarkovChain().from_data(oppnent_history)
    predictionNextItem = giveMostProbableNextItem(chain, prev_play)
    winningMove = winDict[predictionNextItem]
    return winningMove


def contains_duplicates(X):
    X = np.round(X,4)
    return len(np.unique(X)) != len(X)


def giveIndexOfState(chain, item):
    return np.where(chain.states == item)[0][0]


def giveMostProbableNextItem(chain, lastItem):



    retval = chain.states[
        np.argmax(chain.observed_p_matrix[giveIndexOfState(chain, lastItem)])
    ]

    return retval
