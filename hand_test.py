from chain import Block, LinkedList, Chain

if __name__ == '__main__':
    # f = LinkedList()
    # print(f.is_empty())
    # f.append(Block('1'))
    # f.append(Block('2'))
    # f.append(Block('3'))
    # f.show_all()
    # print(f.is_empty())
    # f.append('5')
    # f.append('6')
    # f.append('7')
    # f.show_all(reverse=True)
    # print(f.length())
    # f.show_tail()
    # print(f.find(Block('3')))
    # print(f.find('3'))
    # print(f.find(Block('8')))
    # print(f.find('8'))

    # for i in f:
    #     print(i.data)
    #     print(hash(i.data))

    c = Chain()
    c.add_transaction('1')
    c.add_transaction('2')
    c.add_transaction('3')
    c.add_block()
    print(c.last_block().data)
    print(c.last_block().hash)
    print(c.last_block().prev_hash)
    for i in c.last_block().data:
        print(i.data)

    c.add_transaction('4')
    c.add_transaction('5')
    c.add_transaction('6')
    c.add_block()
    print(c.last_block().data)
    print(c.last_block().hash)
    print(c.last_block().prev_hash)
    for i in c.last_block().data:
        print(i.data)

    #
    # for i in c.chain:
    #     print(i.data)
    #     print(hash(i.data))


