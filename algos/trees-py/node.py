#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None
    index: Optional[int] = None


def create_tree(in_order: List[int], pre_order: List[int]) -> TreeNode:
    if len(in_order) == 0:
        return None
    root = TreeNode(pre_order[0], None, None)
    root_indx = in_order.index(pre_order[0])
    if root_indx >= 1:
        root.left = create_tree(in_order[:root_indx], pre_order[1: root_indx + 1])
    if root_indx + 1 < len(in_order):
        root.right = create_tree(in_order[root_indx + 1:], pre_order[root_indx + 1:])
    return root