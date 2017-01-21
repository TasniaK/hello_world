import pdb

def censor(text, word):
	#pdb.set_trace()
	if word in text:
		text = text.replace(word, ("*" * len(word)))
	return text

if __name__ == "__main__":
	print censor("hey hey hey", "hey")
