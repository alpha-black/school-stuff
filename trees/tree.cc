#include <iostream>
#include <iomanip>
#include "tree.h"

std::string orderToString(TreeTraversalOrder order) {
    switch(order) {
    case IN_ORDER:
        return "in order";
    case POST_ORDER:
        return "post order";
    case PRE_ORDER:
        return "pre order";
    }
    return "";
}

BinaryTreeNode::~BinaryTreeNode() {
    if (left) delete left;
    if (right) delete right;
}

void BinarySearchTree::deleteTree() {
    delete root;
}

BinaryTreeNode *BinarySearchTree::insterToBt(BinaryTreeNode* root, const BinaryTreeElement& element) {
    BinaryTreeNode *newNode = new BinaryTreeNode(element);
    if (root == nullptr) {
        root = newNode;
        return root;
    }
    if (root->getElementVal() > element.getElementVal()) {
        root->left = insterToBt(root->left, element);
    } else if (root->getElementVal() < element.getElementVal()) {
        root->right = insterToBt(root->right, element);
    }
    return root;
}

void BinarySearchTree::insterToBt(const BinaryTreeElement& element) {
    BinaryTreeNode *newNode = new BinaryTreeNode(element);
    if (root == nullptr) {
        root = newNode;
    }
    insterToBt(root, element);
}

void BinarySearchTree::treeTraversal(BinaryTreeNode* node) {
    if (node == nullptr) {
        return;
    }
    switch (order) {
    case IN_ORDER:
        treeTraversal(node->left);
        std::cout << node->getElementVal() << " ";
        treeTraversal(node->right);
        break;
    case PRE_ORDER:
        std::cout << node->getElementVal() << " ";
        treeTraversal(node->left);
        treeTraversal(node->right);
        break;
    case POST_ORDER:
        treeTraversal(node->left);
        treeTraversal(node->right);
        std::cout << node->getElementVal() << " ";
        break;
    }
}
void BinarySearchTree::treeTraversal(TreeTraversalOrder trav_order) {
    std::cout << "Traversal in " << orderToString(trav_order) << ": ";
    order = trav_order;
    treeTraversal(root);
    std::cout << std::endl;
}

void BinarySearchTree::printSearchResult(const BinaryTreeNode& node) const {
    std::cout << "Found element! Child nodes - ";
    std::cout << "left: " << (node.left != nullptr ? std::to_string(node.left->getElementVal()) : "None") << " ";
    std::cout << "right: " << (node.right != nullptr ? std::to_string(node.right->getElementVal()) : "None");
    std::cout << std::endl;
}

bool BinarySearchTree::search(BinaryTreeNode* node, const BinaryTreeElement& element, SearchOptions options) const {
    if (node == nullptr) {
        return false;
    }
    switch(options.method) {
    case DEPTH_FIRST:
        if (node->left) {
            bool found = search(node->left, element, options);
            if (found) return true;
        }
        if (node->getElement() == element) {
            if (options.printResult) {
                printSearchResult(*node);
            }
            return true;
        }
        if (node->right) {
            bool found = search(node->right, element, options);
            if (found) return true;
        }
        return false;
    case BREADTH_FIRST:
        std::cout << "Not implemented!" << std::endl;
        return false;
    }
    return false;
}

bool BinarySearchTree::depthFirstSearch(const BinaryTreeElement& element) const {
    return search(root, element, defaultSearchOptions);
}

bool BinarySearchTree::breadthFirstSearch(const BinaryTreeElement& element) const {
    return search(root, element, {BREADTH_FIRST, true});
}

uint8_t BinarySearchTree::depth(BinaryTreeNode* node, u_int8_t d) const {
    if (node == nullptr) {
        return 0;
    }
    uint8_t depthLeft = d, depthRight = d;
    if (node->left) {
        depthLeft = depth(node->left, d+1);
    }
    if (node->right) {
        depthRight = depth(node->right, d+1);
    }
    return std::max(depthLeft, depthRight);
}

bool BinarySearchTree::isElementInSubTree(BinaryTreeNode* subtreeRoot, const BinaryTreeElement& e) {
    if (subtreeRoot == nullptr)
        return false;

    return search(subtreeRoot, e, {DEPTH_FIRST, false});
}

const BinaryTreeElement& BinarySearchTree::commonAncestor(BinaryTreeNode* node,
        const BinaryTreeElement& e1, const BinaryTreeElement& e2) {
    if (isElementInSubTree(node->left, e1) && isElementInSubTree(node->left, e2)) {
        return commonAncestor(node->left, e1, e2);
    }
    if (isElementInSubTree(node->right, e1) && isElementInSubTree(node->right, e2)) {
        return commonAncestor(node->right, e1, e2);
    }
    return *node;
}

const BinaryTreeElement& BinarySearchTree::commonAncestor(
        const BinaryTreeElement& element1, const BinaryTreeElement& element2) {
    return commonAncestor(root, element1, element2);
}
