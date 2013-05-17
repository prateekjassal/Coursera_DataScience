import urllib
import json
import re
afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.
#print scores.items() # Print every (term, score) pair in the dictionary

# To keep track of the number of tweets
tweet_count = 0
lines = open("output1.txt","r")
for line in lines:
	tweet_score = 0
	result = json.loads(line)
	#print str(result)
	#print result.keys()
	str = result.get('text','zz').encode('utf-8')
	words = re.compile('\w+').findall(str)
	for word in words:
		word_score = int(scores.get(word,'0'))
		tweet_score = tweet_score + word_score
	print tweet_score




