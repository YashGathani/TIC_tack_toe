def display(row1,row2,row3):
    print (f" {row3[0]}  | {row3[1]} | {row3[2]} \n -------------\n {row2[0]}  | {row2[1]} | {row2[2]} \n -------------\n {row1[0]}  | {row1[1]} | {row1[2]}")
def user_input(turn):
    d= {'char' : False,'notdigit':True}
    turn =turn+1
    while d['char'] ==False or d['notdigit']== True :
        text = (input (f"player {turn} input a number between 1-9"))
        if text.isdigit():
            d['char'] = True
            num = int (text)
            
            if num in range(1,10):
                d['notdigit'] = False
            else:
                print("please put a number between 1-9")
        else:
            print ("please input a digit")
            

    #print (f"{d['g']}")
    return int(text)
def mapping (row1,row2,row3,num,player):
   
    if num<=3:
        if row1[num-1] == " ":
            row1[num-1]= player
            play = True
        else:
            print("thats already filled please take any other cell")
            play = False
    elif num>3 and num<=6:
        if row2[num-4] == " ":
            row2[num-4]=player
            play =True
        else:
            print("thats already filled please take any other cell")
            play = False
    else:
        if row3[num-7]==' ':
            row3[num-7]=player
            play =True
        else:
            print("thats already filled please take any other cell")
            play = False
    return (row1,row2,row3,play)
def game_theroy(row1,row2,row3,player_names):
    for i,m in enumerate(row1):
        if row1[i]==row2[i]==row3[i] and (row1[i]==player_names[0] or row1[i]==player_names[1]):
            print (f"{m} wins")
            return True
    
        
    if row1[0]==row1[1]==row1[2] and (row1[0]==player_names[0] or row1[0]==player_names[1]):
        print (f"{row1[0]} wins")
        return True
    if row2[0]==row2[1]==row2[2] and (row2[0]==player_names[0] or row2[0]==player_names[1]):
        print (f"{row2[0]} wins")
        return True
    if row3[0]==row3[1]==row3[2] and (row3[0]==player_names[0] or row3[0]==player_names[1]):
        print (f"{row3[0]} wins")
        return True
    if row1[0]==row2[1]==row3[2] and (row1[0]==player_names[0] or row1[0]==player_names[1]):
        print (f"{row1[0]} wins")
        return True
    if row1[2]==row2[1]==row3[0] and (row1[2]==player_names[0] or row1[2]==player_names[1]):
        print (f"{row1[2]} wins")
        return True
    if (' ' not in row1) and (' ' not in row2) and (' ' not in row3):
        return True
    return False
def player_assigen():
    check = False
    while check == False:
        one = input("player one do you wanna be X or O")
        two = input("player two do you wanna be  X or O")
        if one == two:
            print("both cant be the same chareter")
        else:
            check = True
    return(one,two)
        
from IPython.display import clear_output
play = True
play_check = input("do you wanna play?(Y/N)")
if play_check == "Y":
    
    player_names= player_assigen()              # tuple of numbers
    game_on = False
    chance =0
    row1 =[' ',' ',' ']
    row2 =[' ',' ',' ']
    row3 =[' ',' ',' ']
    display(row1,row2,row3)
    while game_on == False:
        turn= (chance%2)
        num =user_input(turn)
        clear_output()#RETURNS INT
        row1,row2,row3,play = mapping (row1,row2,row3,num,player_names[turn])
        display(row1,row2,row3)
        game_on=game_theroy(row1,row2,row3,player_names)
        if play == False:
            pass
        else:
            chance+=1
            
    if game_on == True:
        print("Game Over")
