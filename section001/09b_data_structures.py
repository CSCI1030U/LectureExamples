# practice

stack = []
stack.append('A')
stack.append('B')
stack.append('C')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')

# (1 + 2) * (3 + (3 - 2))

queue = []
queue.append('A')
queue.append('B')
queue.append('C')
print(f'{queue.pop(0) = }')
print(f'{queue.pop(0) = }')
print(f'{queue.pop(0) = }')

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
        return index < len(self.values) and index >= 0

    def search(self, to_find, current_index = 0):
        if not self._is_valid_index(current_index):
            return False

        if to_find == self.values[current_index]:
            return True 
        elif to_find < self.values[current_index]:
            return self.search(to_find, self.left_child_index(current_index))
        else:
            return self.search(to_find, self.right_child_index(current_index))

    def print(self, depth=0, index=0):
        if not self._is_valid_index(index):
            return
        
        # right subtree
        self.print(depth + 1, self.right_child_index(index))

        # node value
        print('\t' * depth + str(self.values[index]))

        # left subtree
        self.print(depth + 1, self.left_child_index(index))





values = [7, 3, 12, 1, 5, 9, 14]
tree = Binary_Search_Tree(values)
print(f'{tree.search(14) = }')
tree.print()
# print(f'{tree.left_child_index(0) = }')
# print(f'{tree.left_child_index(1) = }')
# print(f'{tree.left_child_index(2) = }')
# print(f'{tree.right_child_index(0) = }')
# print(f'{tree.right_child_index(1) = }')
# print(f'{tree.right_child_index(2) = }')
# print(f'{tree.parent_index(1) = }')
# print(f'{tree.parent_index(2) = }')
# print(f'{tree.parent_index(3) = }')
# print(f'{tree.parent_index(4) = }')
# print(f'{tree.parent_index(5) = }')
# print(f'{tree.parent_index(6) = }')
'''
                7
        3               12
    1       5       9       14

        14
    12
        9
7
        5
    3
        1
'''
