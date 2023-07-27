from Trie import trie
from datetime import datetime

class spellchecker( object ):
	#storing data in a trie after object creation by scanning file and place it an a list then store this list in a trie
	#that property has a time complexty of O(N)
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
#that method returns '' if the key is in the trie and returns 4 nearst words if it is't in the trie
#that method have complexty of O(1) and thats why i choose the trie data structior(no loops)
	def suggestions(self,key):
	
		if self.db.search(key)== False :
			while len(self.db.enumerate(key))<4:
				key = key[:-1]
			return self.db.enumerate(key)[:4]
		else :
			return ''
		
#insert method takes a word and frist place it in the trie (that part have complexty of O(1)) then its overwrite the dectionary
#for not loosing past data i made this function frist creats a txt file with the name if the date and backup then writing the data befor adding new words
#that method has complexty of O(N) as it loops in the file to store the data 

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
		
#this function recall the search fuction in the trie class to check availblty
	def search(self,key):
		return self.db.search(key)

#I lerned to make my clear and understandble so i don't need to add comments to it , but i write some comments as orderd
#comments are bad smells in code


	