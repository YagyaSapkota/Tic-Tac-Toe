
def printBoard():
    print(f"0 | 1 | 2")
    print(f"---------")
    print(f"3 | 4 | 5")
    print(f"---------")
    print(f"6 | 7 | 8")
    print(f"---------")   
if __name__=="__main__":
    xState = [0,0,0,0,0,0,0,0]
    zState =[0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome To Tic Tac Toe")
    while(True):
       printBoard()
       if(turn==1):
               print("Here,X's Chance dude ")
               value = int( input("Please enter a Value"))
               xState[value] = 1
       else:  
              print("Here,X's Chance Dude")
              value= int(input("Please enter a value"))
              zState[value] = 1
              break
        