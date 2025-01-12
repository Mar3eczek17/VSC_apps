import vertexai
import pprint

PROJECT_ID = "YOUR_PROJECT_ID"
REGION = "us-central1"

vertexai.init(project=PROJECT_ID, location=REGION)

from vertexai.preview.extensions import Extension

extension_code_interpreter = Extension.from_hub("code_interpreter")
CODE_QUERY = """"Write a python method to invert a binary tree in O(n) time."""

response = extension_code_interpreter.execute(
    operation_id = "generate_and_execute",
    operation_params = {"query": CODE_QUERY}
    )

print("Generated Code:")
pprint.pprint({response['generated_code']})

# The above snippet will generate the following code.
''' Generated Code: class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def invert_binary_tree(root):
        """
        Inverts a binary tree.
        Args:
            root: The root of the binary tree.
        Returns:
            The root of the inverted binary tree.
        """
        
    if not root:
        return None
        
    # Swap the left and right children recursively
    root.left, root.right = 
invert_binary_tree(root.right), invert_binary_tree(root.left)

    
    return root
    
# Example usage: # Construct a sample binary tree root =
TreeNode(4) root.left = 
TreeNode(2) root.right = 
TreeNode(7) root.left.left = 
TreeNode(1) root.left.right = 
TreeNode(3) root.right.left = 
TreeNode(6) root.right.right = 
TreeNode(9)

# Invert the binary tree 
inverted_root = invert_binary_tree(root)
'''