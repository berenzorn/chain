class Block:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.hash = 0

    def show_block(self):
        print(f"Block: {self.data}")


class TwoWayList:

    def __init__(self):
        self.header = None
        self.tail = None

    def is_empty(self):
        return False if self.header is not None else True

    def list_init(self, data):
        block = Block(data)
        self.header = block
        self.tail = block

    def list_add(self, data):
        block = Block(data)
        self.tail.next = block
        block.prev = self.tail
        self.tail = block

    def check_whole(self):
        print("Checking chain: ")
        current = self.header
        while current is not None:
            current.show_block()
            current = current.next
        print()


if __name__ == '__main__':
    chain = TwoWayList()
    chain.list_init('1')
    chain.list_add('2')
    chain.list_add('3')
    chain.check_whole()
