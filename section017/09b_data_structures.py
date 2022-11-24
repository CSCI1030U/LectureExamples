# practice

stack = []
stack.append('A') # push
stack.append('B') # push
stack.append('C') # push
print(f'{stack.pop() = }') # pop
print(f'{stack.pop() = }') # pop
print(f'{stack.pop() = }') # pop

queue = []
queue.append('A') # enqueue
queue.append('B') # enqueue
queue.append('C') # enqueue
print(f'{queue.pop(0) = }') # dequeue
print(f'{queue.pop(0) = }') # dequeue
print(f'{queue.pop(0) = }') # dequeue

# coding exercise 9.1

class Binary_Search_Tree:
    def __init__(self, initial_values):
        self.values = initial_values[::]

    def left_child_index(self, parent_index):
        return parent_index * 2 + 1

    def right_child_index(self, parent_index):
        return parent_index * 2 + 2

    def parent_index(self, child_index):
        return (child_index - 1) // 2
    
    def _is_valid_index(self, index):
        return (index >= 0) and (index < len(self.values))

    def search(self, to_find, index = 0):
        if not self._is_valid_index(index):
            return False

        if to_find == self.values[index]:
            return True 
        elif to_find < self.values[index]:
            left_child_index = self.left_child_index(index)
            return self.search(to_find, index = left_child_index)
        else:
            # to_find > self.values[index]
            right_child_index = self.right_child_index(index)
            return self.search(to_find, index = right_child_index)

    def print_tree(self, index = 0, depth = 0):
        if not self._is_valid_index(index):
            return

        # print the right subtree
        right_child_index = self.right_child_index(index)
        self.print_tree(index = right_child_index, depth = depth + 1)

        # print the node
        print('\t' * depth + str(self.values[index]))

        # print the left subtree
        left_child_index = self.left_child_index(index)
        self.print_tree(index = left_child_index, depth = depth + 1)



tree = Binary_Search_Tree([10, 7, 15, 1, 9, 12, 20])
tree.print_tree()
print(f'{tree.search(9) = }')
'''
  0  1   2  3  4   5   6
[10, 7, 15, 1, 9, 12, 20]

        20
    15
        12
10
        9
    7
        1

                10
        7               15
    1       9       12      20

1, 2, 3, 4

    1
        2
            3
                4

'''
