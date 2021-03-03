import hashlib
import json
from datetime import datetime

class Block:

    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.serialized = self.serialize()
        self.hash = self.calc_hash()
        self.timestamp = datetime.timestamp(datetime.utcnow())

    def __repr__(self):
        return {"data": self.data, "hash": self.hash}

    def __str__(self):
        return str(self.__repr__())
        
    def serialize(self):
        jsonified = json.dumps(self, 
                               default=lambda o: o.__dict__, 
                               sort_keys=True).encode('utf-8')
        return jsonified
    
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.serialized)
        return sha.hexdigest()



class Blockchain:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_blocks = 0


    def put(self, data):
        if self.head is None:
            new_block = Block(data=data, prev_hash=None)
            self.head = new_block
            self.tail = new_block
        else:
            current_tail = self.tail
            current_hash = current_tail.hash
            new_block = Block(data=data, prev_hash=current_hash)
            self.tail = new_block


if __name__ == '__main__':

    # Test 1

    test_chain_1 = Blockchain()
    for n in range(4):
        test_chain_1.put(n)

    test_chain_2 = Blockchain()
    for n in range(4):
        test_chain_2.put(n)

    print(test_chain_1.tail)
    print(test_chain_2.tail)
    assert test_chain_1.tail.hash == test_chain_2.tail.hash


    # Test 2

    test_chain_3 = Blockchain()
    for n in range(4):
        if n == 2:
            n = 6
        test_chain_3.put(n)

    print(test_chain_2.tail)
    print(test_chain_3.tail)
    assert test_chain_2.tail.hash != test_chain_3.tail.hash

    # Test 2
