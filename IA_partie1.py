from random import random, randint

def makeMove(M, last, strategy, eps, alpha) :
#E-GREEDY STRAT
    reps = random()
    #Check if we pick random move or greedy move
    if reps >= eps or strategy == 'Q-learning':
        pgreedy = M[0][1]
        m = 0
        #trouvé la plus grande probabilité
        for i in range (1,len(M)):
            if m < M[i][1]:
                pgreedy = M[i][1]
                m = i
    if reps >= eps:
        l = []
        for i in range(len(M)):
            if M[i][1] == pgreedy:
                l.append(M[i][0])
        ps = pgreedy
        move = l[randint(0,len(l)-1)]
    else:
        rmove = randint(0,len(M)-1)
        move = M[rmove][0]
        ps = M[rmove][1]

    #Stratégie apprentissage TD(0)
    if strategy == 'TD(0)':
        if last != None:
            last[1] = (1-alpha)*last[1]+alpha*ps

    #Stratégie apprentissage Q-learning
    elif strategy == 'Q-learning':
        if last != None:
            last[1] = (1-alpha)*last[1]+alpha*pgreedy

    return move

def endGame(won, history, strategy, alpha) :
    history.reverse()
    if strategy == 'Monte Carlo':
        for i in range(len(history)):
            history[i][1] = (1-alpha**(i+1))*history[i][1]
            if won:
                history[i][1] += alpha**(i+1)

    else:
        history[0][1] = (1-alpha)*history[0][1]
        if won:
            history[0][1] += alpha
    history.reverse()
    return None
