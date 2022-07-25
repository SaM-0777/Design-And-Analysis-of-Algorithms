# Hoffmann compression in Python

class Char():
    def __init__(self, ch, freq):
        self.char = ch
        self.freq = freq
        
class Node():
    def __init__(self, total_freq, left= None, right= None):
        self.total_freq = total_freq
        self.left = left
        self.right = right
        

if __name__ == "__main__":
    message = "BCCABBDDAECCBBAEDDCC"
    characters = []
    
    for i in range(len(message)):
        if message[i] not in characters:
            characters.append(message[i])
            
    frequencies = []
    for i in characters:
        count = 0
        for j in message:
            if j == i:
                count += 1
        frequencies.append(count)
        
    char_list = []   
        
    for i in range(len(characters)):
        C = Char(characters[i], frequencies[i])
        char_list.append(C)
        
    # Sort char_list according to frequencies in increasing order
    char_list = sorted(char_list, key=lambda x: x.freq)
    
    # Make Tree
    sum_ = Node(char_list[0].freq + char_list[1].freq, char_list[0], char_list[1])
    i = 2
    while i < len(char_list):
        if len(char_list) - i == 1:
            newNode = Node(sum_.total_freq + char_list[i].freq, sum_, char_list[i])
            sum_ = newNode

        elif (sum_.total_freq + char_list[i].freq) <= (char_list[i].freq + char_list[i + 1].freq):
            newNode = Node(sum_.total_freq + char_list[i].freq, sum_, char_list[i])
            sum_ = newNode
            i += 2
        
        else:
            pass
