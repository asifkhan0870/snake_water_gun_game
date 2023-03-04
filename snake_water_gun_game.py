import random

def summary(opponent,you):

    print("your opponent has choose "+ opponent+ " and you have choosen "+ you)
        


def gameWinner(opponent,you):
        
        if opponent==you:
                print("Match tie!")


        if(opponent=='s'):
                if(you=='w'):
                    
                    print("Oh! , you have loose the match,try next time")
                    summary(opponent,you)

                else:
                    print("Congratulations!,You have won!")
                    summary(opponent,you)

        elif opponent=='w':

               if you=='g':
                      print("Oh!,you have loose the match,try next time")   
                      summary(opponent,you)
               else :
                      print("Congratulations!,You have defeated your opponent")
                      summary(opponent,you)   

        elif opponent=='g':
               
               if you=='s':
                      print("Oh!, you have loose the match ,try next time")
                      summary(opponent,you)
               else:
                      print("Congratulations!,you have won!")
                      summary(opponent,you)      
                      
            


        
            




while 1:
       
    choice_by_your_opponent=random.randint(1,3)

    if(choice_by_your_opponent==1):
        
        opponet='s'
    elif choice_by_your_opponent==2:
        opponet='w'
    elif choice_by_your_opponent==3:
        opponet='g'



    b=input("This is your turn, s.snake,w.water,g.gun: ")

    gameWinner(opponet,b)







