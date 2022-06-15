
def frequency_dictionary(text):
    dictionary = dict()
    for i in range(len(text)):
        if text[i] in dictionary:
            dictionary[text[i]] += 1
        else:
            dictionary[text[i]] = 1
    return dictionary

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.father = None
        self.bit = None

def create_tree(dictionary):
    dictionary = sorted(iter(dictionary.items()), key=lambda value: value[1])
    nodes = list()
    for char, freq in dictionary:
        nodes.append(Node(char, freq))

    while len(nodes) > 1:
        node1 = nodes[0]
        del nodes[0]
        node2 = nodes[0]
        del nodes[0]

        sum_freq = node1.freq + node2.freq
        sum_char = node1.char + node2.char
        father = Node(sum_char, sum_freq, node1, node2)

        node1.father = father
        node2.father = father

        nodes.append(father)
        nodes = sorted(nodes, key=lambda value: value.freq)
    return father

def get_codes(code, node, bits):
    if len(node.char) != 1:
        get_codes(code, node.left, bits + '1')
        get_codes(code, node.right, bits + '0')
    else:
        code = bits
        codes[node.char] = code
        fordecodes[code] = node.char

def comprimir(text, codes):
    binario = ''
    for c in text:
        binario += codes[c]
    print('Texto en binario:', binario)
    return len(binario)

def main():
    text = 'EJEMPLO'
    dictionary = frequency_dictionary(text)
    print('Frequency:', dictionary)
    tree = create_tree(dictionary)
    get_codes('', tree, '')
    print('Codes:', codes)
    print('Text:', text)
    comprimir(text, codes)
    
if __name__ == '__main__':
    codes = dict()
    fordecodes= dict()
    main()
