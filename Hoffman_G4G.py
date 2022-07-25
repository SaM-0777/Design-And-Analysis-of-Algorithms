# Huffman Compression

class Node:
	def __init__(self, freq, char, left= None, right= None):
		self.freq = freq
		self.char = char
		self.left = left
		self.right = right
		self.weight = ''
  
huffman_codes = []
  
def createCode(Node, code= ''):
    newCode = code + str(Node.weight)
    
    if Node.left:
        createCode(Node.left, newCode)
    if Node.right:
        createCode(Node.right, newCode)
    if not Node.left and not Node.right:
        huffman_codes.append(int(newCode))
        
        

if __name__ == "__main__":
    message = "BCCABBDDAECCBBAEDDCC"
    characters = []
    
    for i in range(len(message)):
        if message[i] not in characters:
            characters.append(message[i])
            
    frequency = []
    for i in characters:
        count = 0
        for j in message:
            if j == i:
                count += 1
        frequency.append(count)
        
    Nodes = []
    
    for i in range(len(characters)):
        Nodes.append(Node(frequency[i], characters[i]))
    
    print(len(Nodes))
        
    while len(Nodes) > 1:
        Nodes = sorted(Nodes, key= lambda x: x.freq)
        
        left = Nodes[0]
        right = Nodes[1]
        
        left.weight = 0
        right.weight = 1
        
        newNode = Node(left.freq + right.freq, left.char + right.char, left, right)
        print(newNode.char, newNode.freq)
        
        Nodes.remove(left)
        Nodes.remove(right)
        Nodes.append(newNode)
            
    createCode(Nodes[0])
    
    #print(Nodes)
    
    for i in range(len(Nodes)):
        print(f'{Nodes[i].char} - > {huffman_codes[i]}')
            
            
            

"""codes = []

def printNodes(node, val=''):
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

		# if node is edge node then
		# display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")
		codes.append(int(newVal))"""
		
    
#codes.append(newVal)


"""# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']

# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]"""

"""# list containing unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
	nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
	# sort all the nodes in ascending order
	# based on theri frequency
	nodes = sorted(nodes, key=lambda x: x.freq)

	# pick 2 smallest nodes
	left = nodes[0]
	right = nodes[1]

	# assign directional value to these nodes
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create
	# new node as their parent
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	# remove the 2 nodes and add their
	# parent as new node among others
	nodes.remove(left)
	nodes.remove(right)
	nodes.append(newNode)

# Huffman Tree is ready!
printNodes(nodes[0])
print(codes)
"""