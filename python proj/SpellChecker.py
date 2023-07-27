from Trie import trie
from datetime import datetime

class spellchecker( object ):
	#storing data in a trie after object creation by scanning the file and placing it an a list then storing this list in a trie
	#that property has a time complexity of O(N)
	def __init__( self, PathOrName):	
	
		self.PathOrName=PathOrName
		self.db = trie()
		file = open(self.PathOrName, errors="ignore")
		self.data = [line.strip() for line in file]
		file.close
		#print (data)
		k=0
		while k<len(self.data) :
			self.db.insert(self.data[k])
			k+=1
#that method returns '' if the key is in the trie and returns 4 nearest words if it isn't in the trie
#that method have complexity of O(1) and that's why i choose the trie data structure(no loops)
	def suggestions(self,key):
	
		if self.db.search(key)== False :
			while len(self.db.enumerate(key))<4:
				key = key[:-1]
			return self.db.enumerate(key)[:4]
		else :
			return ''
		
#insert method takes a word and first places it in the trie (that part has the complexity of O(1)) then it overwrites the dictionary
#for not lose past data I made this function first create a Txt file with the name of the date and backup then write the data before adding new words
#that method has the complexity of O(N) as it loops in the file to store the data 

	def insert(self,word):
		now =datetime.now()
		nowtxt = (str(now)).replace(":","_")
		nowtxt=nowtxt.replace(".","-")
		fileName = "databackup-"+nowtxt+".txt"
		backup = open(fileName,"w")
		
		backup.write("date and time :	"+(str(now))+"\n\n")
		for item in self.data:
			backup.write(item+"\n")
		backup.close()
		self.db.insert(word)
		newdata = open(self.PathOrName,"w")
		for item in self.db.enumerate(''):
			newdata.write(item+"\n")
		newdata.close()
		
#this function recalls the search function in the trie class to check the availability
	def search(self,key):
		return self.db.search(key)

#I learned to make my code clear and understandable so I don't need to add comments to it, but I wrote some comments as ordered
#comments are bad smells in code


	
