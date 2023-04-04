"""A minimalist Binary Search Tree implementation.

The code draws inspiration from several descriptions of Binary Search Trees:
- https://en.wikipedia.org/wiki/Binary_search_tree
- Chapter 12 of T. H. Cormen, et al., "Introduction to algorithms", MIT press, (2022)
- https://github.com/donsheehy/datastructures

We follow the Cormen et al. convention of allowing duplicate keys.

If you would like a fully object-oriented Binary Search Tree implementation, I recommend:
- https://github.com/donsheehy/datastructures
"""


class BinarySearchTree:

    def __init__(self, root=None):
        raise NotImplementedError


class Node:

    def __init__(self, key, parent=None, left=None, right=None):
        raise NotImplementedError

    def __str__(self):
        summary = f"Node({self.key})"
        if self.parent:
            summary += f" parent={self.parent.key}"
        if self.left:
            summary += f" left={self.left.key}"
        if self.right:
            summary += f" right={self.right.key}"
        return summary


def insert(bst: BinarySearchTree, new_node: Node):
    """Insert a new node into the tree.

    Args:
        bst: the tree to insert into.
        new_node: the node to insert.
    """
    raise NotImplementedError


def search(key: int, node: Node):
    """Search for a node with a given key in the subtree of the given node.

    Args:
        key: the key to search for.
        node: the node whose subtree we wish to search
    """
    raise NotImplementedError


def delete(bst: BinarySearchTree, node: Node):
    """Delete a node from the tree.

    Args:
        bst: the tree to delete from.
        node: the node to delete.
    """
    raise NotImplementedError


def shift_nodes(bst: BinarySearchTree, old_node: Node, new_node: Node):
    """Shift the nodes from the subtree at new_node to the position of old_node.

    Args:
        bst: the tree to shift the nodes in.
        old_node: the node to be replaced.
        new_node: the node (and subtree) that is shifted.
    """
    raise NotImplementedError


def minimum(node: Node):
    """Find the minimum node in the subtree rooted at node.

    Args:
        node: Node - the root of the tree to search.
    """
    raise NotImplementedError


def maximum(node: Node):
    """Find the maximum node in the subtree rooted at node.

    Args:
        node: Node - the root of the tree to search.
    """
    raise NotImplementedError


def inorder(node):
    """Perform an inorder traversal of the tree rooted at node.

    Args:
        node: Node - the root of the tree to traverse.
    """
    raise NotImplementedError


def preorder(node):
    """Perform a preorder traversal of the tree rooted at node.

    Args:
        node: Node - the root of the tree to traverse.
    """
    raise NotImplementedError


def postorder(node):
    """Perform a postorder traversal of the tree rooted at node.

    Args:
        node: Node - the root of the tree to traverse.
    """
    raise NotImplementedError


def main():
    bst = BinarySearchTree()
    insert_keys = [5, 3, 2, 7, 1, 8, 9, 12]
    node_list = [Node(key) for key in insert_keys]
    for node in node_list:
        insert(bst, node)

    # print out traversals
    print(f"Inorder traversal")
    inorder(bst.root)
    print("")
    print(f"Preorder traversal")
    preorder(bst.root)
    print("")
    print(f"Postorder traversal")
    preorder(bst.root)
    print("")

    node_to_delete = node_list[3]
    print(f"Deleting node {node_to_delete}")
    delete(bst, node_to_delete)

    # print out traversal
    print(f"Inorder traversal after deletion")
    inorder(bst.root)
    print("")

    # print out minimum and maximum
    print(f"Minimum key: {minimum(bst.root).key}")
    print(f"Maximum key: {maximum(bst.root).key}")

    """
    Print out:

    Inorder traversal
    1 2 3 5 7 8 9 12
    Preorder traversal
    5 3 2 1 7 8 9 12
    Postorder traversal
    5 3 2 1 7 8 9 12
    Deleting node Node(7) parent=5 right=8
    Inorder traversal after deletion
    1 2 3 5 8 9 12
    Minimum key: 1
    Maximum key: 12
    """


if __name__ == "__main__":
    main()
