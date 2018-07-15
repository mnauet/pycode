# -*- coding: utf-8 -*-
import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
            print('i; j; result: ' + str(i), str(j), result)
        if result == goal:
            total +=1
            print('total: len(goal): ' + str(total), len(goal))
    print('Actual probability of ', txt, '=',
        round(1/(6**len(goal)),8))
    estProbability = round(total/numTrials,8)
    print('Extimated Probability of ', txt, '=',    
        round(estProbability,8))

runSim('11111', 1000, '11111')
