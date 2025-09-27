import random
user_score = 0
bot_score = 0
while True:
 user_option=["rock","paper","scissor",]
 print("Choose from rock,paper and scissor")
 user_choice=input("Enter your choice").strip().lower() #.strip used for ignoring spaces
 if user_choice not in user_option:
    print("Invalid choice")
    continue
 print("You chose",user_choice.capitalize())
 bot_option=["rock","paper","scissor"]
 bot_choice=random.choice(bot_option)
 print("bot chose",bot_choice.capitalize())
 if user_choice==bot_choice:
    print("It's a draw")


 elif user_choice=="rock" and bot_choice=="paper" or user_choice=="scissor" and bot_choice=="rock" or user_choice=="paper" and bot_choice=="scissor":
   print("you lost")
   bot_score=+1

 else:
    print("you won")
    user_score=+1
 user_action=["contiue","quit"]
 user_input=input("DO YOU WANT TO CONTINUE OR QUIT").strip().lower()
 if user_input =="quit":
   print("Your Final Score is",user_score)
   print("Bot Final Score is",bot_score)
   exit()

