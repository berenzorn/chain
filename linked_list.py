class Block:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def show(self):
        print(f"Block: {self.data}")


class LinkedList:

    def __init__(self):
        self.header = None
        self.tail = None
        self.index = 0
        self.counter = 0

    def length(self):
        return self.index

    def is_empty(self):
        return False if self.header is not None else True

    def __iter__(self):
        self.counter = self.header
        return self

    def __next__(self):
        if self.counter is not None:
            temp = self.counter
            self.counter = self.counter.next
            return temp
        else:
            raise StopIteration

    def append(self, data):
        block = Block(data) if not isinstance(data, Block) else data
        if self.header is None:
            self.header = block
        else:
            self.tail.next = block
            block.prev = self.tail
        self.tail = block
        self.index += 1

    def show_all(self, reverse=False):
        if reverse:
            print("Checking from tail: ")
            current = self.tail
            while current is not None:
                current.show()
                current = current.prev
        else:
            print("Checking chain: ")
            current = self.header
            while current is not None:
                current.show()
                current = current.next

    def show_tail(self):
        current = self.tail
        current.show()

    def find(self, data):
        block = Block(data) if not isinstance(data, Block) else data
        current = self.header
        while current.data != block.data:
            current = current.next
            if current is None:
                return False
        return True


if __name__ == '__main__':
    f = LinkedList()
    print(f.is_empty())
    f.append(Block('1'))
    f.append(Block('2'))
    f.append(Block('3'))
    f.show_all()
    print(f.is_empty())
    f.append('5')
    f.append('6')
    f.append('7')
    f.show_all(reverse=True)
    print(f.length())
    f.show_tail()
    print(f.find(Block('3')))
    print(f.find('3'))
    print(f.find(Block('8')))
    print(f.find('8'))

    for i in f:
        print(i.data)
