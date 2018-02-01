def question():
	ask = input("What is your question?")
	return ask









ask_prompt = ""
while ask_prompt != "quit":
	ask_prompt = question()
	if ask_prompt.endswith("?"):
		print(random.choice(possible_answers))
	elif ask_prompt == "quit":
		print("END")
	else:
		print("I’m sorry, I can only answer questions(hint:?),try again or type 'quit' to exit.")