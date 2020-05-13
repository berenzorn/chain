import hashlib
from datetime import datetime, timezone, timedelta


class Block:
    """
    Block fields:
    index from chain,
    timestamp,
    data - his transactions list,
    next - pointer to the next block if exist,
    prev - pointer to the previous block,
    hash - sha256 of its transactions list data fields
    prev_hash - sha256 of the previous block
    """
    def __init__(self, data):
        self.index = None
        self.time = None
        self.data = data
        self.next = None
        self.prev = None
        self.hash = None
        self.prev_hash = None

    def show(self):
        print(f"Block: {self.data}")


class LinkedList:
    """
    LinkedList fields:
    header - pointer to the first block
    tail - pointer to the last block
    index - how many blocks we have
    counter - loop iterator from zero to index
    """
    def __init__(self):
        self.header = None
        self.tail = None
        self.index = 0
        self.counter = 0

    def length(self):
        return self.index

    def get_next_index(self):
        return self.index + 1

    def is_empty(self):
        return False if self.header is not None else True

    '''
    Loop iterator
    '''
    # TODO iterator from tail to header
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

    '''
    Add new block to the linked list
    '''
    def append(self, data):
        block = Block(data) if not isinstance(data, Block) else data
        if self.header is None:
            self.header = block
        else:
            self.tail.next = block
            block.prev = self.tail
        self.tail = block
        self.index += 1

    '''
    Show all blocks data from the header or vice versa
    '''
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

    def get_tail(self):
        return self.tail if self.tail is not None else False

    def get_tail_hash(self):
        return self.tail.hash if self.tail is not None else False

    def find(self, data):
        block = Block(data) if not isinstance(data, Block) else data
        current = self.header
        while current.data != block.data:
            current = current.next
            if current is None:
                return False
        return True


class Chain:

    def __init__(self):
        self.chain = LinkedList()
        self.current_trs = LinkedList()

    def add_block(self):
        block = Block(self.current_trs)
        self.current_trs = LinkedList()
        block.index = self.chain.get_next_index()
        block.time = self.timestamp()
        block.prev_hash = self.chain.get_tail_hash()
        block.hash = self.hash(block.data)
        self.chain.append(block)

    def add_transaction(self, data):
        self.current_trs.append(data)

    def last_block(self):
        return self.chain.get_tail()

    def last_block_hash(self):
        return self.chain.get_tail_hash()

    @staticmethod
    def hash(linklist):
        string = ";".join(idx.data for idx in linklist)
        return hashlib.sha256(string[:-1].encode()).hexdigest()

    @staticmethod
    def timestamp():
        epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)  # use POSIX epoch
        now = datetime.now(timezone.utc)
        timestamp_micros = (now - epoch) // timedelta(microseconds=1)
        return timestamp_micros


if __name__ == '__main__':
    pass
