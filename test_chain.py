import unittest
import chain


class ChainTest(unittest.TestCase):

    def setUp(self):
        self.block = chain.Block('1')
        self.chain = chain.Chain()
        self.array = chain.LinkedList()
        self.trns = chain.LinkedList()

        self.chain.add_transaction('1')
        self.chain.add_transaction('2')
        self.chain.add_transaction('3')

    def test_get_tail_hash_initial(self):
        self.assertIsNone(self.array.tail.hash)

    def test_append(self):
        self.assertEqual(self.array.index, 0)
        self.array.append(chain.Block('1'))
        self.array.append(chain.Block('2'))
        self.assertEqual(self.array.index, 2)
        self.assertEqual(self.array.header.data, '1')
        self.assertEqual(self.array.tail.data, '2')
        self.array.append('3')
        self.array.append('4')
        self.assertEqual(self.array.index, 4)
        self.assertEqual(self.array.header.data, '1')
        self.assertEqual(self.array.tail.data, '4')

    # Block
    def test_show(self):
        self.block.show()

    # LinkedList
    def test_length(self):
        self.assertEqual(self.array.index, 4)

    def test_get_next_index(self):
        self.assertEqual(self.array.index, 5)

    def test_next_iter(self):
        temp = []
        for i in self.array:
            temp.append(i.data)
        self.assertEqual(temp, ['1', '2', '3', '4'])

    def test_get_tail_hash(self):
        self.assertIsNotNone(self.array.tail.hash)

    def test_find(self):
        var1 = chain.Block('2')
        var2 = '2'
        var3 = chain.Block('8')
        var4 = '8'
        self.assertTrue(self.array.find(var1))
        self.assertTrue(self.array.find(var2))
        self.assertFalse(self.array.find(var3))
        self.assertFalse(self.array.find(var4))

    def test_add_block(self):
        block = chain.Block(self.trns)
        block.index = self.array.get_next_index()
        block.time = 0
        block.prev_hash = self.array.get_tail_hash()
        block.hash = self.chain.hash(block)
        self.array.append(block)
        # self.assertEqual()
