# Ana Caroline da Rocha Braz 212008482

class Player:
    players = []

    def __init__(self, nome = '', letra = ''):
        self.name = nome
        self.letra = letra
        Player.players.append(self)

def criar_jogo():
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    return board

def print_jogo(board):
    print(' ' + board[1] + ' │ ' + board[2] + ' │ ' + board[3] + ' ')
    print('───┼───┼───')
    print(' ' + board[4] + ' │ ' + board[5] + ' │ ' + board[6] + ' ')
    print('───┼───┼───')
    print(' ' + board[7] + ' │ ' + board[8] + ' │ ' + board[9] + ' ')
    print('')

def check_vitoria(board, letra = None):
    if letra is None:
        if board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
            return True
        elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
            return True
        elif board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[5] and board[1] == board[9] and board[1] == letra:
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] == letra:
            return True
        elif board[1] == board[4] and board[1] == board[7] and board[1] == letra:
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] == letra:
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] == letra:
            return True        
        elif board[1] == board[2] and board[1] == board[3] and board[1] == letra:
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] == letra:
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] == letra:
            return True
        else:
            return False

def check_empate(board):
    for key in board.keys():
        if board[key] == ' ':
            return False

    return True

def pc_obj():
    for player in Player.players:
        if player.name == 'pc':
            return player


def jogador_obj():
    for player in Player.players:
        if player.name == 'jogador':
            return player

def joga(board, letra, pos):
    if board[pos] == ' ':
        board[pos] = letra
        print()
        print_jogo(board)
    
        if check_empate(board):
            print("Empate!")
            return
        elif check_vitoria(board):
            if letra == pc_obj().letra:
                print("O computador venceu")
            elif letra == jogador_obj().letra:
                print("Você venceu!")
        return
    else:
        print("Posição ocupada, escolha outra!")
        pos = int(input("Escolha a nova posição: "))
        joga(board, letra, pos)
        return

def vez_jogador(board, jogador):
    pos = int(input("Digite uma posição: "))
    joga(board, jogador.letra, pos)
    return

def minimax(board, prof, maxmin):
    computer = pc_obj()
    human = jogador_obj()

    if check_vitoria(board, pc.letra):
        return 1
    elif check_vitoria(board, jogador.letra):
        return -1
    elif check_empate(board):
        return 0

    if maxmin:
        best_score = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = pc.letra
                score = minimax(board, prof + 1, False)  # Next move should minimize
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = jogador.letra
                score = minimax(board, prof + 1, True)  # Next move should maximize
                board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score

def vez_pc(board, pc):
    best_score = -800
    best_move = 0

    for key in board.keys():
        board[key] = pc.letra
        score = minimax(board, 0, False)
        board[key] = ' '
        if score > best_score:
            best_score = score
            best_move = key
    
    joga(board, pc.letra, best_move)
    return

################ MAIN #####################
print("Jogo da velha por minmax")
print("O jogo é disposto pela seguinte forma:")
print()
print(' 1 │ 2 │ 3 ')
print('───┼───┼───')
print(' 4 │ 5 │ 6 ')
print('───┼───┼───')
print(' 7 │ 8 │ 9 ')
print()
print("Iniciando jogo: ")
print()
board = criar_jogo()

jogador = Player('jogador', 'x')
pc = Player('pc', 'o')
print()
print_jogo(board)

while not check_vitoria(board):
     vez_jogador(board, jogador)
     vez_pc(board, pc)

