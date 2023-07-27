#creating a class to creat a node in thr tree
class Node( object ):
	def __init__( self, end_node = False ):
		
		self.end_node = end_node
		self.prefix_count = 0
		self.children = {}
	


class trie( object ):
	def __init__( self ):
		self.root = Node() #creating an emty node to be the root
	
	def insert( self, key ):
		current = self.root #starting from the root then moving to the true location
		for k in key:
			if k not in current.children:
				current.children[k] = Node()
			current = current.children[k]
			current.prefix_count += 1 #counting number of nodes to recall it when need
		current.end_node = True
	
	def search( self, key ):
		current = self.root #starting from the root
		
		for k in key:
			if k not in current.children: #checking the availablety of the key (input) in the tree char by char
				return False
			current = current.children[k]
		return current.end_node #if it is the end nood will return true
	
	def count( self, key ):
		current = self.root
		for k in key:
			if k not in current.children:
				return 0
			current = current.children[k]
		return current.prefix_count

	def _walk( self, root, prefix ):
		out = []
		if root.end_node:
			out.append( prefix )
		
		for ch in root.children:
			if isinstance( prefix, tuple ):
				tmp = self._walk( root.children[ch], prefix + (ch,) )
			elif isinstance( prefix, list ):
				tmp = self._walk( root.children[ch], prefix + [ch] )
			else:
				tmp = self._walk( root.children[ch], prefix + ch )
			out.extend( tmp )
		return out

	def enumerate( self, key ):
		current = self.root
		for k in key:
			if k not in current.children:
				return []
			current = current.children[k]
		
		return self._walk( current, key )