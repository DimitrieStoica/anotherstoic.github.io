board = [
    ['A', 'B', 'C'],
    ['S', 'F', 'S'],
    ['A', 'D', 'E']
]

word = 'ABC'
row, col = len(board), len(board[0])

def dfs(board, word, i, j):

    if len(word) == 0:
        return True

    if ((i < 0) or
        (i >= row) or
        (j < 0) or
        (j >= col) or
        (board[i][j] != word[0])):
        return False

    node = board[i][j]
    board[i][j] = '#'
    
    res = (dfs(board, word[1:], i + 1, j) or
           dfs(board, word[1:], i - 1, j) or
           dfs(board, word[1:], i, j + 1) or
           dfs(board, word[1:], i, j - 1))
    
    board[i][j] = node
    return res
        
for i in range(row):
    for j in range(col):
        if word[0] == board[i][j] and dfs(board, word, i, j):
            print("FOUND")
    
    

