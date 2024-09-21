#finding given email has sperming or not
email='''npdimagine@gmail.com hi vicky kumar you have selected for my company as ceo
you get 100 crore prize and making you crore pati in one day and how you become toppest
if you chose this course then you get opportunity from use '''
spam=['crore pati','crore','Act now',]
spam='''Act now
Limited time
Don’t miss out
Last chance
Hurry
Urgent
Now only
Earn money
Make money
Cash bonus
100% free
Free gift
Guaranteed
Click here
Buy now
Free access
Free trial
No fees
Once in a lifetime
This isn’t a scam
Congratulations
Winner
You have been selected
Opportunity
Best price
Act immediately
Information you requested
Dear friend
100% satisfied
Call now
Sign up free
Order\tnow
Best in the world
Incredible deal
Ultimate
Amazing
Unbeatable
'''.split()
#print(spam)
def filter(email):
    count=0

    for i in email.split():
        
        if i in spam:
            count+=1
    if count!=0:
        print("spam email")
    else:
        print("trusted email")
while True:
        choice=int(input("do you want to filter email\tfiltering\t0\tbreak\n"))
        if choice==1:
            filter(email)
            choice
        elif choice==0:
            break
      

    
