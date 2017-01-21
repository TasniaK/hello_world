
def censor(text, word):
	if word in text:
		text = text.replace(word, ("*" * len(word)))
	return text

if __name__ == "__main__":
	print censor("hey hey hey", "hey")
