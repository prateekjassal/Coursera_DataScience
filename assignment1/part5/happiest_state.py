import sys
import urllib
import json
import re

scores = {} # initialize an empty dictionary
states = {} # Stores cumulative score for each state

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
    	place = result.get('place',None)
    	user = result.get('coordinates', None)
    	if place!=None:
    		country_code = place.get('country_code',None)
    		if country_code=='US':
    			string = result.get('text','zz').encode('ascii','ignore')
    			#print str(tweet_count)+': '+ str(place)
    			#print user
    			#print 'tweet'+str(string)
    			#print 'Country: '+country_code
    			state = place.get('full_name')[-2:]
    			#print 'State: '+ state[-2:].encode('utf-8')
    			words = re.compile('\w+').findall(string)
    			for word in words:
    				word_score = int(scores.get(word,'0'))
    				tweet_score = tweet_score + word_score
    			#print 'Score: '+str(tweet_score)+'\n'
    			tweet_count= tweet_count + 1
    			# Store score for every state
    			states[state] = tweet_score - states.get(state,0)

def printStateScores():
	for key, value in sorted(states.iteritems(), key=lambda (k,v): (v,k)):
		print "%s" % (key)
		break

def main():
    createwordDict()
    scoreTweets()
    printStateScores()

if __name__ == '__main__':
    main()
