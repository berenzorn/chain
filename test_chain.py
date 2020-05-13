import unittest
import chain


class ChainTest(unittest.TestCase):

    def setUp(self):
        self.block = chain.Block('1')
        self.chain = chain.Chain()
        self.linkedlist = chain.LinkedList()
        self.trns = chain.LinkedList()

        self.chain.add_transaction('1')
        self.chain.add_transaction('2')
        self.chain.add_transaction('3')

        self.linkedlist.append(chain.Block('1'))
        self.linkedlist.append(chain.Block('2'))
        self.linkedlist.append('3')
        self.linkedlist.append('4')

    def test_append(self):
        self.assertEqual(self.linkedlist.index, 4)
        self.linkedlist.append(chain.Block('5'))
        self.linkedlist.append(chain.Block('6'))
        self.assertEqual(self.linkedlist.index, 6)
        self.assertEqual(self.linkedlist.header.data, '1')
        self.assertEqual(self.linkedlist.tail.data, '6')
        self.linkedlist.append('7')
        self.linkedlist.append('8')
        self.assertEqual(self.linkedlist.index, 8)
        self.assertEqual(self.linkedlist.header.data, '1')
        self.assertEqual(self.linkedlist.tail.data, '8')

    # LinkedList
    def test_length(self):
        self.assertEqual(self.linkedlist.index, 4)

    def test_is_empty(self):
        self.assertTrue(self.linkedlist.header)

    def test_next_iter(self):
        temp = []
        for i in self.linkedlist:
            temp.append(i.data)
        self.assertEqual(temp, ['1', '2', '3', '4'])

    def test_show_all(self):
        self.assertTrue('Block: 1'
                        'Block: 2'
                        'Block: 3'
                        'Block: 4')

    def test_show_tail(self):
        self.assertTrue('Block: 4')

    def test_find(self):
        self.assertTrue(self.linkedlist.find(chain.Block('1')))
        self.assertTrue(self.linkedlist.find('1'))
        self.assertTrue(self.linkedlist.find(chain.Block('4')))
        self.assertTrue(self.linkedlist.find('4'))
        self.assertFalse(self.linkedlist.find(chain.Block('8')))
        self.assertFalse(self.linkedlist.find('8'))

    # Chain
    def test_add_block(self):
        temp = self.linkedlist.index
        block = chain.Block(self.trns)
        block.index = self.linkedlist.get_next_index()
        block.time = 0
        block.prev_hash = self.linkedlist.get_tail_hash()
        block.hash = self.chain.hash(self.trns)
        self.linkedlist.append(block)
        self.assertEqual(self.linkedlist.index, temp + 1)

    def test_add_transaction(self):
        self.chain.add_transaction('4')
        self.assertEqual(self.chain.current_trs.length(), 4)
        self.assertEqual(self.chain.current_trs.tail.data, '4')

    def test_hash(self):
        self.chain.add_block()
        self.assertIsNotNone(self.chain.last_block().data)
        self.assertEqual(self.chain.last_block().hash,
                         '31e3d12715096e87b840e0282777f202b3ba0ba309b1a3f61d2fd3d3f0ecd015')
        self.assertFalse(self.chain.last_block().prev_hash)
        self.assertEqual([x.data for x in self.chain.last_block().data], ['1', '2', '3'])

        self.chain.add_transaction('4')
        self.chain.add_transaction('5')
        self.chain.add_transaction('6')
        self.chain.add_block()

        self.assertIsNotNone(self.chain.last_block().data)
        self.assertEqual(self.chain.last_block().hash,
                         'ca5e064780562a6fd68d18b38669f17b03ce4908d0dcee52e494b4d18c842869')
        self.assertEqual(self.chain.last_block().prev_hash,
                         '31e3d12715096e87b840e0282777f202b3ba0ba309b1a3f61d2fd3d3f0ecd015')
        self.assertEqual([x.data for x in self.chain.last_block().data], ['4', '5', '6'])


if __name__ == '__main__':
    unittest.main()
