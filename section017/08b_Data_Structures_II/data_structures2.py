class BinarySearchTree:
    def __init__(self, values=[]):
        self.values = values 
    
    def _left_child_index(self, parent_index):
        # TODO: Write this code
        return 0

    def _right_child_index(self, parent_index):
        # TODO: Write this code
        return 0

    def _parent_index(self, child_index):
        # TODO: Write this code
        return 0

    def _is_index_valid(self, index):
        if index < len(self.values) and index >= 0:
            return True 
        else:
            return False

    def print(self, index=0, depth=0):
        if not self._is_index_valid(index):
            return

        # print the left child
        self.print(self._left_child_index(index), depth + 1)

        # print the node itself (indented)
        print('\t' * depth, self.values[index])

        # print the right child
        self.print(self._right_child_index(index), depth + 1)

'''
                20
        11              33
    4       12      25      40

[20,11,33,4,12,25,40]

0 -> 1
1 -> 3
2 -> 5

        40
    33
        25
20
        12
    11
        4

'''

bst = BinarySearchTree([20,11,33,4,12,25,40])
bst.print()