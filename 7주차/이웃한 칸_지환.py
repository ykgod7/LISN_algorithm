def solution(board, h, w):
    answer = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]

    for i in range(4):
        if len(board) > h - dh[i] > -1 and len(board) > w - dw[i] > -1:
            if (board[h][w] == board[h - dh[i]][w - dw[i]]):
                answer += 1

    return answer