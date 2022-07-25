# A Huffman Tree Node
import sys

class Node:
    def __init__(self, freq, char, left=None, right=None, code= ''):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.weight = ''
        self.code = code
 
def createCodes(node, code=''):
    newCode = code + str(node.weight)
 
    if(node.left):
        createCodes(node.left, newCode)
    if(node.right):
        createCodes(node.right, newCode)
    if(not node.left and not node.right):
        node.code = newCode
 
 
if __name__ == "__main__":
    message = "BCCABBDDAECCBBAEDDCC"
    characters = []
    frequency = []
    
    for i in range(len(message)):
        if message[i] not in characters:
            characters.append(message[i])
            
    for i in characters:
        count = 0
        for j in message:
            if j == i:
                count += 1
        frequency.append(count)
        
    Nodes = []
    
    for i in range(len(characters)):
        Nodes.append(Node(frequency[i], characters[i]))
    
    Table = Nodes
    Table = sorted(Table, key= lambda x: x.freq)
    
    while len(Nodes) > 1:
        Nodes = sorted(Nodes, key=lambda x: x.freq)
    
        left = Nodes[0]
        right = Nodes[1]
    
        left.weight = 0
        right.weight = 1
        
        newNode = Node(left.freq + right.freq, left.char + right.char, left, right)

        Nodes.remove(left)
        Nodes.remove(right)
        Nodes.append(newNode)
    
    createCodes(Nodes[0])
        
    total_size = 0
    
    uncompressed_size = (len(message) * sys.getsizeof(message[0]))
    
    for x in Table:
        total_size += ((x.freq * len(x.code)) + sys.getsizeof(x.char) + len(x.code))
    
    print(f'Char\tFrequency\tCode')    
    for x in Table:
        print(f'{x.char}\t{x.freq}\t\t{x.code}')
    
    print()
    
    print(f'Compression % : {((1 - (total_size / uncompressed_size)) * 100):.2f}')
    print(f'Compression ratio : {uncompressed_size // total_size}')
    
    print()
    