class Node:
    def __init__(self, value):
        self.value = value
        self.nachfolger = None
        self.pref = None


class DoppeltVerketteteListe:
    def __init__(self):
        self.head = None #zeigt aauf das erste element in der liste
        self.ende = None #zeigt auf das letzte element in der liste
        self.size = 0;

    def append(self, data):
        self.size += 1
        newNode = Node(data)
        if self.ende is None:
            self.head = newNode; # weil head is immer nur dann Null wenn auch das ende pointer null ist
            self.ende = newNode
        else:
            self.ende.nachfolger = newNode;
            self.ende.nachfolger.pref = self.ende;
            self.ende = newNode;

    def insertAfter(self, node, data):
        newNode = Node(data);
        if (node is None): #ganz am anfang einfügen, dann brauch man keine insertFront
            newNode.nachfolger = self.head
            if self.head is not None:
                self.head.pref = newNode
            self.head = newNode
            if self.ende is None:
                self.ende = newNode
        else:
            newNode.nachfolger = node.nachfolger
            newNode.pref = node
            if node.nachfolger is not None:
                node.nachfolger.pref = newNode
            node.nachfolger = newNode;
            if (node == self.ende):
                self.ende = newNode;
        self.size += 1

    def __iter__(self): #macht die objekte der klasse iterierbar
        current = self.head
        while current is not None:
            yield current.value
            current = current.nachfolger

    def __len__(self):
        return self.size

    def getLengt(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertOnEnd(self, data): #am Ende einfügen
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.ende = newNode
        else:
            newNode.nachfolger = self.head
            self.head.pref = newNode
            self.head = newNode
        self.size += 1

    def remove(self, node):
        if node.pref is not None:
            node.pref.nachfolger = node.nachfolger
        else:
            self.head = node.nachfolger

        if node.nachfolger is not None:
            node.nachfolger.pref = node.pref
        else:
            self.ende = node.pref
        self.size -= 1

    def drucken(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.nachfolger
        print("None")
