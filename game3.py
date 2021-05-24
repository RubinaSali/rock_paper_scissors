import random

print("...rock...\n...paper...\n...scissors...")
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
	print(f"player = {player_wins}  computer = {computer_wins}")
	rand_number= random.randint(0,2)
	player=input("Make your move:  ")
	if player == "quit" or player== "q":
		break
	if rand_number==0:
		computer="rock"
	elif rand_number==1:
		computer="paper"
	else:
		computer="scissors"
	print("computer plays: " + computer)
	if player==computer:
		print("draw")
	elif player=="rock":
		if computer=="scissors":
			print("player wins!!")
			player_wins +=1
		elif computer=="paper":
			print("computer wins!!")
			computer_wins +=1
	elif player=="paper":
		if computer=="rock":
			print("player wins!!")
			player_wins +=1
		elif computer == "scissors":
			print("computer wins!!")
			computer_wins +=1
	elif player=="scissors":
		if computer=="rock":
			print("computer wins!!")
			computer_wins +=1
		elif computer=="paper":
			print("player wins")
			player_wins +=1
		else:
			print("something went wrong")

print(f"FINAL SCORES...player = {player_wins}  computer = {computer_wins}")
if player_wins > computer_wins:
	print("CONGRATS")
elif player_wins==computer_wins:
	print("it's a tie!")
else:
	print("SORRY YOU LOST")

