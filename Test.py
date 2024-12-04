def assign(root, row, col, ans):
    if not root:
        return
    if col in ans:
        if row in ans[col]:
            temp_arr = ans[col][row]
            temp_arr.append(root.val)
            temp_arr.sort()
            ans[col][row] = temp_arr
        else:
            ans[col][row] = [root.val]
    else:
        ans[col] = {row: [root.val]}

    assign(root.left, row+1, col-1, ans)
    assign(root.right, row+1, col+1, ans)

def verticalTraversal(root):
    """
    Better Approach
    1. calculate vertical for each node using preorder or other left = (row + 1, col - 1), right = (row + 1, col + 1)
    2. key inseting in dict in this format {col: {row: val}}
    3. sort dict by outer key
    4. sort dict by inner key
    5. flatten inner val and add it to final ans
    Time Complexity: O(NlogN) + O(NlogN + MlogM)) + O(N)
                    calculate    for sorting dict   flatten arr
                    vertical     both key, val are
                                    independent
    Space Complexity: O(N) + O(N) +     log(N)
                      dict   final_ans  temp arr
    """
    ans = {}
    assign(root, 0, 0, ans)
    final_ans = []
    print(ans)
    for key, val in sorted(ans.items()):
        temp = []
        for inner_key, inner_val in sorted(val.items()):
            temp.extend(inner_val)
        final_ans.append(temp)
    return final_ans
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(10)
root.right.left = Node(9)
root.right.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)

print(verticalTraversal(root))
