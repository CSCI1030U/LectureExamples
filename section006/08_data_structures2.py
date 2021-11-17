class BinarySearchTree:
    def __init__(self, values=[]):
        self.values = values
    
    def _left_child_index(self, parent_index):
        return parent_index * 2 + 1

    def _right_child_index(self, parent_index):
        return parent_index * 2 + 2

    def _parent_index(self, child_index):
        return (child_index - 1) // 2

    def _is_index_valid(self, index):
        return index < len(self.values) and index >= 0
        # if index >= len(self.values) or index < 0:
        #     return False 
        # else:
        #     return True

    '''
                    10
            7               15
        1       9       12      20
    [10,7,15,1,9,12,20]

    left child index:   right_child:
    0 (10) -> 1 (7)     2
    1 (7) -> 3 (1)      4
    2 (15) -> 5 (12)    6
    '''

    def print(self, index=0, depth=0):
        if not self._is_index_valid(index):
            return
        
        # print the left sub-tree
        left_index = self._left_child_index(index)
        self.print(left_index, depth + 1)

        # print the current node
        print('\t' * depth, self.values[index])

        # print the right sub-tree
        right_index = self._right_child_index(index)
        self.print(right_index, depth + 1)



bst = BinarySearchTree([10,7,15,1,9,12,20])
bst.print()

'''
sideways:
        20
    15
        12
10
        9
    7
        1

upright:
                10
        7               15
    1       9       12      20
[10,7,15,1,9,12,20]
'''