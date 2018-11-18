from random import random, randint

"""
    Auteur: Sacha Bon
    Matricule: 000458911
    Date: 18/11/18
    B1-INFO
"""

def makeMove(M, last, strategy, eps, alpha) :

    reps = random()

    #Trouver la probabilité gloutonne
    if reps >= eps or strategy == 'Q-learning':
        pgreedy = M[0][1]
        for i in range (1,len(M)):
            if pgreedy < M[i][1]:
                pgreedy = M[i][1]

    #choix glouton
    if reps >= eps:
        x = []
        for i in range(len(M)):
            if M[i][1] == pgreedy:
                x.append(M[i])
        r = randint(0,len(x)-1)
        move = x[r][0]
        p = x[r][1]

    #exploration
    else:
        m = randint(0,len(M)-1)
        move = M[m][0]
        p = M[m][1]

    #apprentissage en TD(0)
    if strategy == 'TD(0)' and last != None:
        last[1] = (1-alpha)*last[1]+alpha*p

    #apprentissage en Q-learning
    elif strategy == 'Q-learning' and last != None:
        last[1] = (1-alpha)*last[1]+alpha*pgreedy

    return move

def endGame(won, history, strategy, alpha) :

    #apprentissage en Monte Carlo
    if strategy == 'Monte Carlo':
        for i in range(len(history)):
            history[i][1] = (1-alpha**(len(history)-i+1)) * history[i][1]
            if won:
                history[i][1] += alpha**(len(history)-i+1)

    #Conclusion des apprentissages on-line TD(0) et Q-learning
    else:
        history[len(history)-1][1] = (1-alpha)*history[len(history)-1][1]
        if won:
            history[len(history)-1][1] += alpha
    return None
