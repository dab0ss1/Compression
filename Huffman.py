# dependencies

class Node():
    def __init__(self):
        self.left = None
        self.right = None

'''
Creates a Huffman Tree out of a list of values. 1D list: [a, b, c, d,..., y, z]
'''

# main
def main():
    # Used as an example
    data = [1,2,3,5,6,8,3,5,7,9,4,6,7,9,4,5,6,7,4,3,2,1,4,5,6,7,8,7,5,3,4,5,6,8,9,9,6,5,4,3,2,4,5,5,6,6,7,8,9,0,9,8,7,6,5,5,4,3,3,3,2,3,4,5,5,6,6,6,7,7,8,8,6,7,6,4,4,3,3,3]
    list = createHuff(data)
    print(list)
# end main

# returns a mapping from the elements in a list to their huffman code
def createHuff(list):
    data_count = countRepeats(list)
    huff_tree = createHuffTree(data_count)
    color_code = elementToCode(huff_tree, "")  # huff codes
    return color_code

# Returns a sorted list of tuples where the first element of the tuple is a string version
# of the elements in the list given and the second value in the tuple is the frequency it appears.
# keys: string elements. values: number of times the element appears
def countRepeats(data):
    dict = {}
    for element in data:
        if str(element) in dict.keys():
            dict[str(element)] += 1
        else:
            dict[str(element)] = 1
    dict_sort = sorted(dict.items(), key=lambda x: x[1])
    return dict_sort


# Creates a huffman tree of the color values
# assumes dict given is sorted by least to most frequent elements
def createHuffTree(dict):
    while len(dict) != 1:
        p1 = dict.pop(0)
        p2 = dict.pop(0)
        node = Node()
        node.left = p1[0]
        node.right = p2[0]
        dict.append((node, p1[1] + p2[1]))
        dict = sorted(dict, key=lambda x: x[1])
    return dict[0][0]

# Returns a dictionary. keys: element values. values: huffman code
# hufftree is of type Node
def elementToCode(hufftree, code):
    dict = {}
    left = '0'
    right = '1'

    # in cases where there is only one element in the picture
    if isinstance(hufftree, str):
        dict[hufftree] = code + str(left)
        return dict

    # left node of huffman tree
    if hufftree.left is not None and isinstance(hufftree.left, str):
        dict[hufftree.left] = code + str(left)
    else:
        dict.update(elementToCode(hufftree.left, code + str(left)))
    # right node of huffman tree
    if hufftree.right is not None and isinstance(hufftree.right, str):
        dict[hufftree.right] = code + str(right)
    else:
        dict.update(elementToCode(hufftree.right, code + str(right)))
    return dict

if __name__ == '__main__':
    main()
