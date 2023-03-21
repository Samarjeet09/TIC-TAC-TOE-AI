# comparison of 3 appraches

# random picker
# minMax
# alphaBeta pruning
import random


def randompicker(board):
    n = random.randint(0, 8)
    i = 0
    while board[n] != '' and i <= 8:
        n = random.randint(0, 8)
        i = i+1
    return n

# evaluation Function


def evauluationfunction(board) -> int:
    evaluation = 0
    # for rows
    for i in range(0, 7, 3):
        temp = ''
        temp = board[i]+board[i+1]+board[i+2]
        if temp == 'xxx':
            evaluation -= 1
        elif temp == 'ooo':
            evaluation += 1
        elif temp == 'xx':
            evaluation -= 0.3
        elif temp == 'oo':
            evaluation += 0.3
    # for cols
    for i in range(0, 3, 1):
        temp = ''
        temp = board[i]+board[i+3]+board[i+6]
        if temp == 'xxx':
            evaluation -= 1
        elif temp == 'ooo':
            evaluation += 1
        elif temp == 'xx':
            evaluation -= 0.3
        elif temp == 'oo':
            evaluation += 0.3
    # for diags
    temp = ''
    temp = board[0]+board[4]+board[8]
    if temp == 'xxx':
        evaluation -= 1
    elif temp == 'ooo':
        evaluation += 1
    elif temp == 'xx':
        evaluation -= 0.3
    elif temp == 'oo':
        evaluation += 0.3

    temp = ''
    temp = board[2]+board[4]+board[6]
    if temp == 'xxx':
        evaluation -= 1
    elif temp == 'ooo':
        evaluation += 1
    elif temp == 'xx':
        evaluation -= 0.3
    elif temp == 'oo':
        evaluation += 0.3
    return evaluation


# min max


def minMax(board, maxTurn, depth):
    if depth == 0:
        return evauluationfunction(board), 4
    if maxTurn:
        maxEval = -5
        posi = 4
        for x, i in enumerate(board):
            # print(i)
            if i == '':
                b = board.copy()
                b[x] = 'o'

                evall, a = minMax(b, False, depth-1)
                if (evall > maxEval):
                    posi = x
                    maxEval = evall
        return maxEval, posi
    else:
        minEval = 5
        posi = 4
        for x, i in enumerate(board):
            if i == '':
                b = board.copy()
                b[x] = 'x'
                evall, a = minMax(b, True, depth-1)
                if (evall < minEval):
                    posi = x
                    minEval = evall
        return minEval, posi

# alpha beta prunigng


def alphaBeta(board, maxTurn, depth, alpha, beta):
    if depth == 0:
        return evauluationfunction(board), 4
    if maxTurn:
        maxEval = -5
        posi = 4
        for x, i in enumerate(board):
            # print(i)
            if i == '':
                b = board.copy()
                b[x] = 'o'

                evall, a = alphaBeta(b, False, depth-1, alpha, beta)
                if (evall > maxEval):
                    posi = x
                    maxEval = evall
                alpha = max(alpha, evall)
                if (beta <= alpha):
                    break
        return maxEval, posi
    else:
        minEval = 5
        posi = 4
        for x, i in enumerate(board):
            if i == '':
                b = board.copy()
                b[x] = 'x'
                evall, a = alphaBeta(b, True, depth-1, alpha, beta)
                if (evall < minEval):
                    posi = x
                    minEval = evall
                beta == min(beta, evall)
                if alpha >= beta:
                    break
        return minEval, posi
