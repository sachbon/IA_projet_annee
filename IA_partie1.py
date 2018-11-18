from random import random, randint

def makeMove(M, last, strategy, eps, alpha) :
    #e-greedy
    reps = random()
    #greedy
    if reps >= eps or strategy == 'Q-learning':
        pgreedy = M[0][1]
        #trouvé la plus grande probabilité
        for i in range (1,len(M)):
            if pgreedy < M[i][1]:
                pgreedy = M[i][1]
    if reps >= eps:
        x = []
        for i in range(len(M)):
            if M[i][1] == pgreedy:
                x.append(M[i])
        r = randint(0,len(x)-1)
        move = x[r][0]
        p = x[r][1]
    else:
        m = randint(0,len(M)-1)
        move = M[m][0]
        p = M[m][1]

    if strategy == 'TD(0)' and last != None:
        last[1] = (1-alpha)*last[1]+alpha*p

    elif strategy == 'Q-learning' and last != None:
        last[1] = (1-alpha)*last[1]+alpha*pgreedy

    return move

def endGame(won, history, strategy, alpha) :
    if strategy == 'Monte Carlo':
        w = 0
        if won:
            w = 1
        history.reverse()
        for i in range(len(history)):
            history[i][1] = (1 - alpha**(i+1)) + w * alpha**(i+1)
        history.reverse()
    else:
        p = history[len(history)-1][1]
        history[len(history)-1][1] = (1-alpha)*p
        if won:
            history[len(history)-1][1] += alpha
    return None
