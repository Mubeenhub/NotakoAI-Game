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

printboard()

flag = False
while flag == False:
    if flag == True:
        break
    check = True
    while check == True:
        player_1 = input('Player 1: ')
        if (player_1 in keys) and (board[player_1] != 'X') and (player_1[:1] in ABC):
            board[player_1] = 'X'
            if len(ABC) == 1 and blockkiller() == True:
                print('Player 2 wins game')
                flag = True
                check = False
                break
            else:
                blockkiller()
                printboard()
                check = False
        else:
            print('Invalid move, please input again')
    if flag == True:
        break
    check = True
    while check == True:
        player_2 = input('Player 2: ')
        if (player_2 in keys) and (board[player_2] != 'X') and (player_2[:1] in ABC):
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