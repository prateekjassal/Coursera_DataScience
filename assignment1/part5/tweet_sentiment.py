import sys
import urllib
import json
import re

scores = {} # initialize an empty dictionary

def createwordDict():
	sent_file = open(sys.argv[1])
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

def scoreTweets():
    tweet_count = 0
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
    	tweet_score = 0
    	result = json.loads(line)
    	string = result.get('text','zz').encode('utf-8')
    	words = re.compile('\w+').findall(string)
    	for word in words:
    		word_score = int(scores.get(word,'0'))
    		tweet_score = tweet_score + word_score
    	print tweet_score
def main():
    createwordDict()
    scoreTweets()

if __name__ == '__main__':
    main()
