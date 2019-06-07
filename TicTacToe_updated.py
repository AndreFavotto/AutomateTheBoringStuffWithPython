def game():
    theBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def showBoard(board):
        for i in range(0, 3):
            if(i != 0):
                print('\n ---------')
            for j in range(0, 3):
                if(j == 0):
                    print('|', end='')
                print(f' {board[i][j]} ' + '|', end='')

    def playAgain():
        ans = input('Do you want to play again? (yes or no) ').lower()
        if(ans == 'yes'):
            game()
        elif(ans == 'no'):
            exit()
        else:
            print('Your answer must be yes or no!')

    def checkWinner(board):
        for i in range(0,3):  # check horizontals
            if(board[i][0] == board[i][1] == board[i][2]):
                return True
                break
        for j in range(0,3):  # check verticals
            if(board[0][j] == board[1][j] == board[2][j]):
                return True
                break
        # check diagonals
        if (board[0][0] == board[1][1] == board[2][2]):
            return True
        elif (board[0][2] == board[1][1] == board[2][0]):
            return True

    print('The positions are the following:\n')
    showBoard(theBoard)
    print('\n')
    turn = -1
    while (not(turn =='X' or turn =='O')):
        turn = input("Which one is going to start(X or O)?:").upper()
    count = 0
    while(count <= 9):
        print(f'Turn for {turn} to play')
        move = int(input('Choose your spot: '))
        while not(move in range (1,10)):
            print('Invalid spot!')
            move = int(input('Choose your spot: '))
        for i in range (0,3):
            for j in range (0,3):
                if move == theBoard[i][j]:
                    theBoard[i][j] = turn
                    break
        showBoard(theBoard)
        if(checkWinner(theBoard)):
            print(f'\n {turn} won!')
            playAgain()
        print('\n____\n')
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        count += 1
    print('Nobody won!')
    playAgain()
game()