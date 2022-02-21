ABC = ['A','B','C']
List = ['A','B','C']
board = {}
keys = []
values = []
for j in range(0,3):
    for i in range(0,9):
        keys.append(List[j]+str(i))
for h in range(0,3):
    for k in range(0,9):
        values.append(k)
for x in range(0,27):
    board[keys[x]] = values[x]

def numbers(a,b):
    y = 1
    for j in range(len(ABC)):
        whitespace = 1
        for x in range(a,b):
            if whitespace < 3:
                print(board[(ABC[j]+str(x))], end = ' ')
                whitespace += 1
            else:
                if y < len(ABC):
                    print(board[(ABC[j]+str(x))], end = '  ')
                    y+=1
                else:
                    print(board[(ABC[j]+str(x))], end = '')
                    print()

def printboard():
    if ABC[0] == 'A' and len(ABC)>1:
        print('A', end = '      ')
    if len(ABC) == 1 and ABC[0] == 'A':
        print('A', end = '')
        print()
    if (len(ABC) == 3  and ABC[1] == 'B'):
        print('B',  end = '      ')
    if (len(ABC) == 2 and ABC[0] == 'B'):
        print('B',  end = '      ')
    if (len(ABC) == 2 and ABC[1] == 'B'):
        print('B', end = '')
        print()
    if (len(ABC) == 1 and ABC[0] == 'B'):
        print('B', end = '')
        print()
    if (len(ABC) == 3  and ABC[2] == 'C'):
        print('C')
    if (len(ABC) == 2 and ABC[1] == 'C'):
        print('C')
    if (len(ABC) == 1 and ABC[0] == 'C'):
        print('C')
    numbers(0,3)
    numbers(3,6)
    numbers(6,9)

def blockkiller():
    for i in List:
        if ((board[i+str(0)] == 'X') and (board[i+str(4)] == 'X') and (board[i+str(8)] == 'X')) or ((board[i+str(2)] == 'X') and (board[i+str(4)] == 'X') and (board[i+str(6)] == 'X')):
            if i in ABC:
                ABC.remove(i)
                return True
            else:
                continue
        for j in range(0,9,3):
            row_1 = 0
            for p in range(j,j+3):
                if (board[i+str(p)] == 'X'):
                    row_1+=1
                    if row_1 == 3:
                        if i in ABC:
                            ABC. remove(i)
                            return True
                        else:
                            continue
        for j in range(0,3):
            column_1 = 0
            for p in range(j,j+7,3):
                if (board[i+str(p)] == 'X'):
                    column_1+=1
                    if column_1 == 3:
                        if i in ABC:
                            ABC.remove(i)
                            return True
                        else:
                            continue

def Knights_move(x):
    if player_2 != board[x+'4']:
        y = int(player_2[-1:0:-1]) + 5
        if y <= 8 and board[x + str(y)] != 'X' :
            letter = x +str(y)
            board[letter] = 'X'
            print(f'player 1: {letter}')
            printboard()
        elif y > 8 and board[x + str(y - 10)] != 'X':
            y = y - 10
            letter = x +str(y)
            board[letter] = 'X'
            print(f'player 1: {letter}')
            printboard()
        elif board[x + str(y)] == 'X':
            y = y - 5
            if y == 1:
                letter = x +str(8)
                board[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()
            elif y == 3:
                letter = x +str(2)
                board[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()
            elif y == 5:
                letter = x +str(6)
                board[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()
            elif y == 7:
                letter = x +str(0)
                board[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()
            elif y == 8:
                letter = x +str(1)
                board[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()
            elif y == 0:
                letter = x +str(7)
                board[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()
            elif y == 6:
                letter = x +str(5)
                board[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()

def sacrifice(x):
    count = 0
    for i in range(0,9,4):
        if board[x + str(i)] == 'X':
            count += 1
            if count == 2:
                for j in range (0,9,4):
                    if board[x + str(j)] != 'X':
                        letter = x +str(j)
                        board[x +str(j)] = 'X'
                        print(f'Player 1: {letter}')
                        blockkiller()
                        printboard()
                        return True
    count = 0
    for i in range(2,9,2):
        if board[x + str(i)] == 'X':
            count += 1
            if count == 2:
                for j in range (2,9,4):
                    if board[x + str(j)] != 'X':
                        letter = x +str(j)
                        board[x + str(j)] = 'X'
                        print(f'Player 1: {letter}')
                        blockkiller()
                        printboard()
                        return True
    for j in range(0,9,3):
        row_1 = 0
        for p in range(j,j+3):
            if (board[x+str(p)] == 'X'):
                row_1+=1
                if row_1 == 2:
                    for a in range(0,9,3):
                        for b in range(a,a + 3):
                            if board[x + str(b)] != 'X':
                                letter = x + str(b)
                                board[x + str(b)] = 'X'
                                print(f'Player 1: {letter}')
                                blockkiller()
                                printboard()
                                return True
    for j in range(0,3):
        column_1 = 0
        for p in range(j,j+7,3):
            if (board[x+str(p)] == 'X'):
                column_1+=1
                if column_1 == 2:
#                    for c in range(0,3):
                    for d in range(j,j +7, 3):
                        if board[x + str(d)] != 'X':
                            letter = x + str(d)
                            board[x + str(d)] = 'X'
                            print(f'Player 1: {letter}')
                            blockkiller()
                            printboard()
                            return True

def trap(x):
    count = 0
    for j in range(0,3):
        column_1 = 0
        for p in range(j,j+7,3):
            if (board[x+str(p)] == 'X'):
                    count +=1
                    break
            else:
                column_1 += 1
                if column_1 == 3:
                    empty_column = j
    new_count =0
    if count == 2:
        for v in range(0,9,3):
            row_1 = 0
            for n in range(v,v+3):
                if (board[x+str(n)] == 'X'):
                    new_count += 1
                    break
                else:
                    row_1 += 1
                    if row_1 == 3:
                        empty_row = v
    if new_count == 2:
        y = empty_row + empty_column
        letter = x + str(y)
        board[letter] = 'X'
        print(f' Player 1: {letter}')
        printboard()
        return

def reflection(x):
    y = int(player_2[-1:0:-1])
    if y == 0 :
        letter = x + str(8)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
    elif y == 1 :
        letter = x + str(7)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
    elif y == 2 :
        letter = x + str(6)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
    elif y == 5 :
        letter = x + str(3)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
    elif y == 3 :
        letter = x + str(5)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
    elif y == 6 :
        letter = x + str(2)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
    elif y == 7 :
        letter = x + str(1)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
    elif y == 8 :
        letter = x + str(0)
        if board[letter] != 'X':
            board[letter] = 'X'
            print(f'Player 1: {letter}')
            blockkiller()
            printboard()
            return
corner = 0
checker = 0
def AI():
    global myboard
    global corner
    global checker
    if board['A4'] == 4 and board['B4']== 4 and board['C4'] == 4 :
        print('Player 1: A4')
        board['A4'] = 'X'
        printboard()
        return
    if len(ABC) == 3 and player_2[0:1] == 'A' and axes == 1:
        reflection('A')
        return
    if len(ABC) == 3 and (player_2[0:1]== 'B' or player_2[0:1] == 'C') and axes == 1:
        if player_2[0:1] == 'B':
            print('Player 1: C4')
            global myboard
            myboard = 'C'
            board['C4'] = 'X'
            printboard()
            return
        elif player_2[0:1] == 'C':
            print('Player 1: B4')
            myboard = 'B'
            board['B4'] = 'X'
            printboard()
            return
    if len(ABC) == 3 and axes == 2 and player_2[:1] != myboard:
        if sacrifice(player_2[:1]) == True :
            pseudo_variable = 0
            return
        else:
            trap(player_2[:1])
            return
    if len(ABC) == 3 and axes == 2 and player_2[:1] == myboard:
        myboard = 'A'
        sacrifice(player_2[:1])
        return
    if len(ABC) == 3 and axes == 3 and player_2[:1] != myboard:
        sacrifice(player_2[:1])
        return
    if len(ABC) == 3 and axes == 3 and player_2[:1] == myboard:
        myboard = 'A'
        sacrifice(player_2[:1])
        return
    if len(ABC) == 2 and axes == 2:
        if player_2[:1] == 'B':
            print('Player 1: C4')
            myboard = 'C'
            board['C4'] = 'X'
            printboard()
            return
        elif player_2[:1] == 'C':
            print('Player 1: B4')
            myboard = 'B'
            board['B4'] = 'X'
            printboard()
            return
    if len(ABC) == 2 and axes != 2 and player_2[:1] != myboard:
        if sacrifice(player_2[:1]) == True :
            pseudo_variable = 0
            return
        else:
            trap(player_2[:1])
            return
    if len(ABC) == 2 and board[ABC[0] + str(4)] == 'X' and board[ABC[1] + str(4)] == 'X' and player_2[:1] == myboard: #new
        sacrifice(myboard) #new
        myboard = ABC[0] #new
        return #new
    if len(ABC) == 2 and player_2[:1] == myboard:
        Knights_move(myboard)
        return
    if len(ABC) == 1 and player_2[:1] == myboard and (myboard in ABC):
        Knights_move(player_2[:1])
        return
    if len(ABC) == 1 and (player_2[:1] != myboard or (myboard not in ABC)) and corner == 0:
         alphabet = ABC[0]
         number_axes = 0
         for i in range(0,9):
             if board[alphabet + str(i)] == 'X':
                number_axes +=1
         if number_axes > 1 and checker == 0:
             if board[alphabet + str(0)] == 'X' and board[alphabet + str(8)] != 'X':
                 y = alphabet + str(8)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 corner = 1
                 printboard()
                 return
             elif board[alphabet + str(2)] == 'X' and board[alphabet + str(6)] != 'X':
                 y = alphabet + str(6)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 corner = 1
                 printboard()
                 return
             elif board[alphabet + str(6)] == 'X' and board[alphabet + str(2)] != 'X':
                 y = alphabet + str(2)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 corner = 1
                 printboard()
                 return
             elif board[alphabet + str(8)] == 'X'and board[alphabet + str(0)] != 'X':
                 y = alphabet + str(0)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 corner = 1
                 printboard()
                 return
         else:
             if board[alphabet + str(0)] == 'X' and board[alphabet + str(8)] != 'X':
                 y = alphabet + str(8)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
             elif board[alphabet + str(2)] == 'X' and board[alphabet + str(6)] != 'X':
                 y = alphabet + str(6)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
             elif board[alphabet + str(6)] == 'X'and board[alphabet + str(2)] != 'X':
                 y = alphabet + str(2)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
             elif board[alphabet + str(8)] == 'X' and board[alphabet + str(0)] != 'X':
                 y = alphabet + str(0)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
             elif board[alphabet + str(1)] == 'X' and board[alphabet + str(7)] != 'X':
                 y = alphabet + str(7)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
             elif board[alphabet + str(7)] == 'X' and board[alphabet + str(1)] != 'X':
                 y = alphabet + str(1)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
             elif board[alphabet + str(3)] == 'X' and board[alphabet + str(5)] != 'X':
                 y = alphabet + str(5)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
             elif board[alphabet + str(5)] == 'X' and board[alphabet + str(3)] != 'X':
                 y = alphabet + str(3)
                 board[y] = 'X'
                 print(f'Player 1: {y}')
                 checker += 1
                 printboard()
                 return
    if (len(ABC) == 1 and (player_2[:1] != myboard or (myboard not in alphabet)) and corner == 1):
        for o in range(1,8,2):
            alphabet = ABC[0]
            y = alphabet + str(o)
            if board[y] != 'X':
                board[y] = 'X'
                print(f' Player 1: {y}')
                printboard()
                return

printboard()
axes = 0
flag = False
while flag == False:
    if flag == True:
        break
    check = True
    while check == True:
        AI()
        check = False
    if flag == True:
        break
    check = True
    while check == True:
        player_2 = input('Player 2: ')
        if (player_2 in keys) and (board[player_2] != 'X') and (player_2[:1] in ABC):
            axes += 1
            board[player_2] = 'X'
            if len(ABC) == 1 and blockkiller() == True:
                print('Player 1 wins game')
                flag = True
                check = False
                break
            else:
                blockkiller()
                printboard()
                check = False
        else:
            print('Invalid move, please input again')


            '''
    if len(ABC) == 1 and (player_2[:1] != myboard or (myboard not in ABC)):
        alphabet = ABC[0]
        if board[alphabet + str(0)] == 'X':
            y = alphabet + str(8)
            if board[y] != 'X':
                board[y] = 'X'
                print(f'Player 1: {y}')
                corner = 1
                printboard()
                return
        elif board[alphabet + str(2)] == 'X':
            y = alphabet + str(6)
            if board[y] != 'X':
                board[y] = 'X'
                print(f'Player 1: {y}')
                corner = 1
                printboard()
                return
        elif board[alphabet + str(6)] == 'X':
            y = alphabet + str(2)
            if board[y] != 'X':
                board[y] = 'X'
                print(f'Player 1: {y}')
#                global corner
                corner = 1
                printboard()
                return
        elif board[alphabet + str(8)] == 'X':
            y = alphabet + str(0)
            if board[y] != 'X':
                board[y] = 'X'
                print(f'Player 1: {y}')
#                global corner
                corner = 1
                printboard()
                return
                '''