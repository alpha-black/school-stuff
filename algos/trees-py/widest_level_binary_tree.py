#!/usr/bin/env python3

from collections import deque
from typing import List

from node import TreeNode, create_tree as ct

def create_tree() -> TreeNode:
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node11 = TreeNode(11)
    node14 = TreeNode(14)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node7
    node4.left, node4.right = node8, node9
    node5.right = node11
    node7.left = node14

    return node1

def widest_binary_tree_level(root: TreeNode) -> int:
    if not root: return 0

    root.index = 0
    q = deque([root])

    max_width = 1
    while q:
        start, end = q[0].index, q[0].index
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                node.left.index = 2 * node.index + 1
                q.append(node.left)
            if node.right:
                node.right.index = 2 * node.index + 2
                q.append(node.right)
            end = node.index
        max_width = max(max_width, end - start + 1)

    return max_width


def right_most_nodes(root: TreeNode) -> List[int]:
    if not root:
        return 0

    ret = []
    q = deque([root])
    while q:
        node = None
        for i in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        if node: ret.append(node.val)

    return ret

def main():
    root = create_tree()
    print(f'Right most nodes of tree: {right_most_nodes(root)}')
    print(f'Max width of tree: {widest_binary_tree_level(root)}')

    root = ct([8,4,9,2,5,11,1,3,14,7], [1,2,4,8,9,5,11,3,7,14])
    print(f'Right most nodes of tree: {right_most_nodes(root)}')
    print(f'Max width of tree: {widest_binary_tree_level(root)}')

if __name__ == '__main__':
    main()