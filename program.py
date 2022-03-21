#Program for the tic_tac_toe game

tac_toe=[ [],[],[],[],[],[],[],[],[] ]
#create a blank list to store the each input such as 0 and *


def check_winner(tac_toe):
#create function to get the inputed data and check the condition of games
               
            if(len(tac_toe[0])==1 and len(tac_toe[1])==1 and len(tac_toe[2])==1):
            #check length of that position is 1 or 0 for comparing the index of that data(0 and *)
                if(tac_toe[0]==tac_toe[1] and tac_toe[0]==tac_toe[2]):
                #if this condition is satisfied then means you win the game
                    print(tac_toe[0],'is winner')
                    #displaying that who is winner of the game 1 or *
                    exit()
                    #after winning the game we dont have to continue and close the program
                    
            if(len(tac_toe[3])==1 and len(tac_toe[4])==1 and len(tac_toe[5])==1):    
                    if(tac_toe[3]==tac_toe[4] and tac_toe[3]==tac_toe[5]):
                        print(tac_toe[3],'is winner')
                        exit()
            
            if(len(tac_toe[6])==1 and len(tac_toe[7])==1 and len(tac_toe[8])==1):                    
                if(tac_toe[6]==tac_toe[7] and tac_toe[6]==tac_toe[8]):
                    print(tac_toe[6],'is winner')
                    exit()
                    
            if(len(tac_toe[0])==1 and len(tac_toe[3])==1 and len(tac_toe[6])==1):
                if(tac_toe[0]==tac_toe[3] and tac_toe[0]==tac_toe[6]):
                    print(tac_toe[0],'is winner')
                    exit()
             
            if(len(tac_toe[1])==1 and len(tac_toe[4])==1 and len(tac_toe[7])==1):  
                if(tac_toe[1]==tac_toe[4] and tac_toe[1]==tac_toe[7]):
                    print(tac_toe[1],'is winner')
                    exit()
            
            if(len(tac_toe[2])==1 and len(tac_toe[5])==1 and len(tac_toe[8])==1):
                if(tac_toe[2]==tac_toe[5] and tac_toe[2]==tac_toe[8]):
                    print(tac_toe[2],'is winner')
                    exit()
            
            if(len(tac_toe[0])==1 and len(tac_toe[4])==1 and len(tac_toe[8])==1):
                if(tac_toe[0]==tac_toe[4] and tac_toe[0]==tac_toe[8]):
                    print(tac_toe[0],'is winner')
                    exit()
            
            if(len(tac_toe[2])==1 and len(tac_toe[4])==1 and len(tac_toe[6])==1):
                if(tac_toe[2]==tac_toe[4] and tac_toe[2]==tac_toe[6]):
                    print(tac_toe[2],'winner') 
                    exit()
                        
            
def game(tac_toe):
#create a game function and passes the tac_toe list 
          
        for i in range(len(tac_toe)):
            #used for loop for lenth of tac_toe data inputs not more than that
            print(tac_toe[0],tac_toe[1],tac_toe[2])
            print(tac_toe[3],tac_toe[4],tac_toe[5])
            print(tac_toe[6],tac_toe[7],tac_toe[8])
            #firstly show the list or display the game that how it is look like
                
            inp=int(input(f'\n on which place you want\n'))
            #enter the position first of the item 0 or *
            if(len(tac_toe[inp])==0):
            #now if on that index there is no item then get the item
                tac_toe[inp]=input('enter 0 or *\n')
            else:
            #otherwise show the message that on this index there is already an item present
                print('position already occupied enter diff')
                      
            check_winner(tac_toe)
            #send the new tac_toe list to the check_winner function for the processing or checking winner
        
        else:
            #incase there is none condition that will true then diplay the massage the no one winner 
            print('game tie')

game(tac_toe)
#call the main function that is game









# list=[1,2,1,1]
# # if(list[0]==1 and list[2]==1 and list[3]==1 and list[1]==2):
# #     print('possible')
# # else:
# #     print('no')

# for i in range(len(list)):
#     if(i+1==len(list)):
#         break
#     list[i]=list[i+1]
#     print(list[1])