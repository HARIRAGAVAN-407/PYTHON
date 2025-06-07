import random #PRINT THE RANDOM INTEGER NUMBERS WHICH CONTAIN RANDOM FUNCTION
#ASK TO ROLL OR NOT

choice=input("ARE GOING TO PLAY A DICE(Y/N) :").lower()#CONVERT THE UPPERCASE TO LOWERCASE
#IF USER ENTER Y

       #
if(choice=='y'):
    #GENERATE 2 NUMBERS
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f'({die1},{die2})')
elif(choice=='n'):
    print("THANK YOOU FOR THE RESPONSE...BETTR LUCK NEXT TIME")
    
else:
   print("...!INVALID CHOICE!....")
    
    