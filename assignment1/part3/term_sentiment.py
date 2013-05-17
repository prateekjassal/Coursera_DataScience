import sys
import urllib
import json
import re

scores = {} # initialize an empty dictionary

newscores = {} # empty dictionary for new words not in original file
instances = {} # tracks the number of instances of the new words

def createwordDict():
	sent_file = open(sys.argv[1])
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

def scoreTweets():
    tweet_count = 1
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
    	tweet_score = 0
    	result = json.loads(line)
    	string = result.get('text','zz').encode("ascii", "ignore") 
    	#words = re.compile('\w+').findall(string)
    	words = string.strip().split()
    	newwords= []
    	for word in words:
    		word = word.encode('utf-8')
    		word_score = int(scores.get(word,'1000000'))
    		# Means word was not found in original dictionary
    		if word_score==1000000:
    			newwords.append(word)
    		else:	
    			tweet_score = tweet_score + word_score
    	# Now check for all new words encountered
    	for word in newwords:
    		newscores[word]= newscores.get(word,0)+tweet_score
    		'''
    		# Check if the word is present in the new dictionary
    		if word in newscores:
    			# If already present take average of the old score and new one
    			old_score = newscores[word]*int(instances[word])
    			# Update the number of instances of the word
    			instances[word] = int(instances[word])+1
    			average_score = float((old_score + tweet_score)/int(instances[word]))
    			# Update the score of the word
    			newscores[word] = average_score
    			#print word+': I was updated !!'
    		else:
				# If the word is not present in newscores, set instance as 1 and score as 0
    			newscores[word]= tweet_score
    			instances[word]= 1
    		'''	
    	#print str(tweet_count)+': '+string
    	#print tweet_score
    	#print '-----'
    	tweet_count= tweet_count +1

def displayWords():
	for key, value in sorted(newscores.iteritems(), key=lambda (k,v): (v,k)):
		print "%s %s" % (key, value)

def main():
    createwordDict()
    scoreTweets()
    displayWords()

if __name__ == '__main__':
    main()
