import urllib

def read_text():
	quotes = open("")
	contents_of_file = quotes.read()
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	connection.close()

read_text()

