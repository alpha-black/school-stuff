#include <iostream>
#include <vector>

#include "tree.h"

std::vector<int> TREE_ELEMETNS = {10,7,6,9,13,12,11,14};

void adNodesToTree(BinarySearchTree *tree) {
    for (auto element : TREE_ELEMETNS) {
        tree->insterToBt(BinaryTreeElement(element));
    }
}
int main() {
    BinarySearchTree* tree = new BinarySearchTree();
    adNodesToTree(tree);
    tree->treeTraversal(IN_ORDER);
    tree->treeTraversal(PRE_ORDER);
    tree->treeTraversal(POST_ORDER);
    const int searchElement = 10;
    std::cout << "DFS for " << searchElement << ": ";
    if (tree->depthFirstSearch(BinaryTreeElement(searchElement)) == false) {
        std::cout << " not found!" << std::endl;
    }
    std::cout << "Common ancestor of 14 and 11 in tree: " <<
        (tree->commonAncestor(BinaryTreeElement(14), BinaryTreeElement(11))).getElementVal() << std::endl;

    tree->deleteTree();
    return 0;
}