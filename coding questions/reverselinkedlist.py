# understand/revise LL
# see how to reverse then code
# codechef: https://www.codechef.com/submit/REVLL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def reverseList(self):
        prev = None
        current = self.head
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        self.printList()


    def printList(self):
        current = self.head
        if(current):
            print("ListBegins:")
            print("Head => ",end="")
            while(current):
                if(current.next != None):
                    print(current.data, end=" -> ")
                else:
                    print(current.data, end=" -> NULL")
                current = current.next
            print()
        else:
            print("List empty")

print("""
    options:
    1. Add Node
    2. Show List
    3. Reverse List
    0. Stop
    """)

ll = LinkedList()

keepGoing = True
while keepGoing:
    
    n = int(input("Enter option: "))
    match n:
        case 1:
            print("Enter value: ",end="")
            ll.addNode(int(input()))
        case 2:
            ll.printList()
        case 3:
            ll.reverseList()
        case 0:
            keepGoing = False
        case default:
            print("Enter valid option")

