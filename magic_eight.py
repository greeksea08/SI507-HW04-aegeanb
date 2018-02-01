import random

def question():
	ask = input("What is your question?")
	return ask

possible_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it",
"As I see it, Yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again",
"Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it",
"My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]


ask_prompt = ""
while ask_prompt != "quit":
	ask_prompt = question()
	if ask_prompt.endswith("?"):
		print(random.choice(possible_answers))
	elif ask_prompt == "quit":
		print("END")
	else:
		print("I’m sorry, I can only answer questions(hint:?),try again or type 'quit' to exit.")

