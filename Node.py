class Node():
    def __init__(self, val, Prev=None, Next=None):
        self.val = val
        self.Next = Next
        self.Prev = Prev

if __name__ == "__main__":
   Head = Node(5)
   Temp = Head
   for i in range(5):
       if Head.Next == Head.Prev == None:
           newNode = Node(i ** 2 + 50, Head)
           newNode.Prev = Temp
           newNode.Next = None
           Head.Next = newNode
           Temp = newNode
       else:
           newNode = Node(i ** 2 + 50, Temp)
           Temp.Next = newNode
           newNode.Prev = Temp
           newNode.Next = None
           Temp = newNode
           
   while Temp.Prev != None:
        print(f'Data : {Temp.val}')
        Temp = Temp.Prev
   
           
    