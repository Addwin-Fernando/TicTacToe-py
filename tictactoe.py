class tictactoe :
    def spacex(sel,board):
        sel-=1
        board[sel]= "x"   
        print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],))

    def spaceo(sel,board):
        sel-=1
        board[sel]= "o"   
        print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],))
    
    def win(board,b):
        if board[0]==board[1]==board[2]=="x":
            print("the winner is x")
            b=1
        elif board[3]==board[4]==board[5]=="x":
            print("the winner is x")
            b=1
        elif board[6]==board[7]==board[8]=="x":
            print("the winner is x")
            b=1
        elif board[0]==board[3]==board[6]=="x":
            print("the winner is x")
            b=1
        elif board[1]==board[4]==board[7]=="x":
            print("the winner is x")
            b=1
        elif board[2]==board[5]==board[8]=="x":
            print("the winner is x")
            b=1
        elif board[0]==board[4]==board[8]=="x":
            print("the winner is x")
            b=1
        elif board[2]==board[4]==board[6]=="x":
            print("the winner is x")
            b=1
        elif board[0]==board[1]==board[2]=="o":
            print("the winner is o")
            b=1
        elif board[3]==board[4]==board[5]=="o":
            print("the winner is o")
            b=1
        elif board[6]==board[7]==board[8]=="o":
            print("the winner is o")
            b=1
        elif board[0]==board[3]==board[6]=="o":
            print("the winner is o")
            b=1
        elif board[1]==board[4]==board[7]=="o":
            print("the winner is o")
            b=1
        elif board[2]==board[5]==board[8]=="o":
            print("the winner is o")
            b=1
        elif board[0]==board[4]==board[8]=="o":
            print("the winner is o")
            b=1
        elif board[2]==board[4]==board[6]=="o":
            print("the winner is o")
            b=1    




board = [" "] * 9

# player = input("Do you want to play against a computer or")
print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],))

b = 2
i=1
while i < 10:
    sel = int(input("Enter the space you want to play : "))
    place = sel - 1
    turn = i%2
    
    
    if board[place]=="x" or board[place]=="o":
        i=i-1
        print("that space is taken try another")
    
    else: 
        if turn == 1 :
            tictactoe.spacex(sel,board)
        else:
            tictactoe.spaceo(sel, board) 
        print(i)       

    tictactoe.win(board,b)
    if b == 1:
        break   
    i+=1
        