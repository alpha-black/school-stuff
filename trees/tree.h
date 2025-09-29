#pragma once

enum TreeTraversalOrder {
    IN_ORDER,
    PRE_ORDER,
    POST_ORDER,
};

enum SearchMethod {
    DEPTH_FIRST,
    BREADTH_FIRST,
};

struct SearchOptions {
    SearchMethod method;
    bool printResult;
};

const SearchOptions defaultSearchOptions = {DEPTH_FIRST, true};

std::string orderToString(TreeTraversalOrder order);

class BinaryTreeElement {
private:
    int val;
public:
    explicit BinaryTreeElement(const int val) : val(val) {}
    explicit BinaryTreeElement(const BinaryTreeElement& element) : val(element.getElementVal()) {}
    bool operator==(const BinaryTreeElement& element) const {
        return val == element.val;
    }
    bool operator>(const BinaryTreeElement& element) const {
        return val > element.val;
    }
    bool operator<(const BinaryTreeElement& element) const {
        return val > element.val;
    }
    int getElementVal() const {
        return val;
    }
    const BinaryTreeElement& getElement() const {
        return *this;
    }
};

class BinaryTreeNode: public BinaryTreeElement {
public:
    BinaryTreeNode *left;
    BinaryTreeNode *right;
    BinaryTreeNode(const BinaryTreeElement& element) :
        BinaryTreeElement(element), left(nullptr), right(nullptr) {}
    ~BinaryTreeNode();
};

class BinarySearchTree {
private:
    BinaryTreeNode *root;
    TreeTraversalOrder order;
    bool search(BinaryTreeNode* node, const BinaryTreeElement& element,
        SearchOptions option = defaultSearchOptions) const;
    void printSearchResult(const BinaryTreeNode& node) const;
    bool isElementInSubTree(BinaryTreeNode* subtreeRoot, const BinaryTreeElement& e);

public:
    BinarySearchTree() : root(nullptr) {}
    ~BinarySearchTree() = default;

    BinaryTreeNode* insterToBt(BinaryTreeNode* node, const BinaryTreeElement& element);
    void insterToBt(const BinaryTreeElement& element);
    void treeTraversal(BinaryTreeNode *node);
    void treeTraversal(TreeTraversalOrder order = IN_ORDER);

    // Search
    bool depthFirstSearch(const BinaryTreeElement& element) const;
    bool breadthFirstSearch(const BinaryTreeElement& element) const;

    uint8_t depth(BinaryTreeNode* node, u_int8_t d) const;
    const BinaryTreeElement& commonAncestor(BinaryTreeNode* node, const BinaryTreeElement& e1, const BinaryTreeElement& e2);
    const BinaryTreeElement& commonAncestor(const BinaryTreeElement& element1, const BinaryTreeElement& element2);

    void deleteTree();
};