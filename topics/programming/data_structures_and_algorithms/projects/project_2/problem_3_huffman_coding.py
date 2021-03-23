from collections import Counter
import queue as Q
from dataclasses import dataclass, field
from typing import Any
import sys


@dataclass(order=True)
class Node:
    freq: int
    char: str = field(compare=False)
    left_child: Any = field(compare=False, default=None)
    right_child: Any = field(compare=False, default=None)


class HuffmanTree:
    def __init__(self):
        self.string = None
        self.q = Q.PriorityQueue()
        self.mapping = {}
        self.rev_mapping = {}
        self.root_node = None

    def make_q(self, string):
        self.string = string
        freq_dict = Counter(string)
        for item in freq_dict.items():
            new_node = Node(char=item[0], freq=item[1])
            self.q.put((new_node.freq, new_node))

    def merge_nodes(self, node1, node2):
        combined_freq = node1.freq + node2.freq
        new_node = Node(char=None, freq=combined_freq)
        new_node.left_child = node1
        new_node.right_child = node2
        return new_node

    def grow_tree(self):
        node1 = self.q.get()[1]
        if self.q.qsize() == 0:
            self.root_node = node1
            return

        while self.q.qsize() > 1:
            node2 = self.q.get()[1]
            if node1.freq > node2.freq:
                self.q.put((node1.freq, node1))
                node1 = node2
            else:
                node1 = self.merge_nodes(node1, node2)
        self.root_node = self.merge_nodes(node1, self.q.get()[1])

    def make_codes_helper(self, root, current_code):
        if root is None:
            return
        if root.char is not None:
            self.mapping[root.char] = current_code
            self.rev_mapping[current_code] = root.char
            return
        self.make_codes_helper(root.left_child, current_code + "0")
        self.make_codes_helper(root.right_child, current_code + "1")

    def make_codes(self):
        current_code = ""
        if self.root_node.left_child == None and self.root_node.right_child == None:
            self.mapping[self.root_node.char] = "0"
            self.rev_mapping["0"] = self.root_node.char
        else:
            self.make_codes_helper(self.root_node, current_code)

    def encode(self, text, return_root=False):
        encoded_text = ""
        for char in text:
            encoded_text += self.mapping[char]

        if return_root == True:
            return encoded_text, self.root_node
        else:
            return encoded_text

    def decode(self, encoded_text, root_node=None):
        if self.mapping == {}:
            self.root_node = root_node
            self.make_codes()
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.rev_mapping:
                character = self.rev_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text


def huffman_encoding(text):
    if len(text) == 0:
        raise ValueError("Must provide data to decode")
    ht = HuffmanTree()
    ht.make_q(text)
    ht.grow_tree()
    ht.make_codes()
    encoded_text, root = ht.encode(text, return_root=True)
    return encoded_text, root


def huffman_decoding(encoded_text, root):
    ht = HuffmanTree()
    decoded_text = ht.decode(encoded_text, root_node=root)
    return decoded_text


def pad_encoded_text(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
        encoded_text += "0"

    padded_info = "{0:08b}".format(extra_padding)
    encoded_text = padded_info + encoded_text
    return encoded_text


def get_byte_array(padded_encoded_text):
    if len(padded_encoded_text) % 8 != 0:
        print("Encoded text not padded properly")
        exit(0)

    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i : i + 8]
        b.append(int(byte, 2))
    return b


if __name__ == "__main__":

    string = "A man a plan a canal panama. The quick brown fox jumped over the lazy dog."
    print(f"Test string: \n{string}\n")

    ht = HuffmanTree()

    # Test 1
    print("Test 1")
    ht.make_q(string)
    for item in ht.q.queue:
        print(f"priority: {item[0]}, \tNode: {item[1]}")
        if item[1].char == "a":
            assert item[1].freq == 10  # There are a lot of a's in the test string
        assert item[0] == item[1].freq
    print("\n")

    # Test 2
    ht.grow_tree()
    ht.make_codes()
    print(ht.mapping)

    encoded_text, root_node = ht.encode(string, return_root=True)
    print(f"frequency of root node: {root_node.freq}\n")

    assert root_node.freq == len(string)
    print(f"encoded text: \n{encoded_text}\n")
    decoded_text = ht.decode(encoded_text)
    print(f"decoded text: \n{decoded_text}\n")


    # Test 3
    print(f"The content of the data is: {string}")
    print(f"The size of the data is: {sys.getsizeof(string)}\n")

    encoded_data, tree = huffman_encoding(string)
    byte_array = get_byte_array(pad_encoded_text(encoded_data))
    print(f"The content of the encoded data is: {encoded_data}")
    print(f"The size of the data is: {sys.getsizeof(byte_array)}\n")
    assert sys.getsizeof(byte_array) < sys.getsizeof(string)

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"The content of the decoded data is: {decoded_data}")
    print(f"The size of the data is: {sys.getsizeof(decoded_data)}\n")

    # Test 4
    string = "AAAAAA"
    encoded_data, tree = huffman_encoding(string)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == string
    print(decoded_data)

    # Test 5
    string = "AAABBB"
    encoded_data, tree = huffman_encoding(string)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == string
    print(decoded_data)


