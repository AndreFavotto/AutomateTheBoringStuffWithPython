def game():
    theBoard = {'TL': 'TL', 'TM': 'TM', 'TR': 'TR',
                'ML': 'ML', 'MM': 'MM', 'MR': 'MR',
                'LL': 'LL', 'LM': 'LM', 'LR': 'LR'}

    def showBoard(board):
        print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
        print('--+--+--')
        print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
        print('--+--+--')
        print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])


    def playAgain():
        ans = input('Do you want to play again? (yes or no) ').lower()
        if(ans == 'yes'):
            game()
        elif(ans== 'no'):
            exit()
        else:
            print('Your answer must be yes or no!')


    def checkWinner(board):
        if((board['TL'] == board['TM'] == board['TR']) or (board['TL'] == board['ML'] == board['LL'])
        or (board['TL'] == board['MM'] == board['LR']) or (board['LL'] == board['LM'] == board['LR']) or
        (board['LL'] == board['MM'] == board['TR']) or (board['TR'] == board['MR'] == board['LR']) or
        (board['TM'] == board['MM'] == board['LM'])):
            return True


    print('The positions are the following:\n')
    showBoard(theBoard)
    print('\n')
    turn = input("Which one is going to start(X or O)?:")
    count = 0
    while(count <= 9):
        print('Turn for ' + turn + ' to play')
        move = input('Choose your spot: ')
        theBoard[move] = (' {}'.format(turn))
        showBoard(theBoard)
        if(checkWinner(theBoard)):
         print('\n {} won!'.format(turn))
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