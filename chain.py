class TwoWayList:

    def __init__(self):
        self.header = None
        self.tail = None

    def is_empty(self):
        return False if self.header is not None else True

    def append(self, data):
        block = Chain.Block(data)
        if self.header is None:
            self.header = block
        else:
            self.tail.next = block
            block.prev = self.tail
        self.tail = block

    def show(self, reversed=False):
        if reversed:
            print("Checking from tail: ")
            current = self.tail
            while current is not None:
                current.show_block()
                current = current.prev
        else:
            print("Checking chain: ")
            current = self.header
            while current is not None:
                current.show_block()
                current = current.next

    def check(self, block):
        current = self.header
        while current.data != block.data:
            current = current.next
            if current is None:
                return False
        return current


class Collector:

    def __init__(self):
        self.array = TwoWayList()

    def append(self, data):
        self.array.append(data)

    def show(self):
        self.array.show()


class Transaction:

    def __init__(self):
        self.data = dict()


class Chain:

    class Block:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None
            # self.hash = 0
            self.prev_hash = 0

    def __init__(self):
        self.chain = TwoWayList()
        self.current_trns = []

    def new_block(self, data):
        # block = {
        #     'index': len(self.chain) + 1,
        #     'timestamp': time(),
        #     'transactions': self.current_transactions,
        #     'proof': proof,
        #     'previous_hash': previous_hash or self.hash(self.chain[-1]),
        # }
        TwoWayList.append(self.chain, data)
        # self.current_transactions = []
        #
        # self.chain.append(block)
        # return block

    def new_transaction(self, data):
        self.current_trns.append(data)
        # self.current_transactions.append({
        #     'sender': sender,
        #     'recipient': recipient,
        #     'amount': amount,
        # })
        #
        # return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Хеширует блок
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        # block_string = json.dumps(block, sort_keys=True).encode()
        # return hashlib.sha256(block_string).hexdigest()
        pass


if __name__ == '__main__':
    chain = TwoWayList()
    chain.append('1')
    chain.append('2')
    chain.append('3')
    chain.append('4')
    chain.append('5')
    chain.show()
    print()
    chain.show(reversed=True)
    print()
    block3 = Chain.Block('3')
    if chain.check(block3):
        print(block3.data, "found")
