class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def constructFromPrePost(self, preorder, postorder):
        """
        :param preorder: List[int]
        :param postorder: List[int]
        :return: Optional[TreeNode]
        """

        post_dic = {v: i for i, v in enumerate(postorder)}


        def Construct(pre_s, pre_e, post_s, post_e):

            if pre_s > pre_e:
                return None

            root_v = preorder[pre_s]
            root = TreeNode(root_v)

            if pre_s == pre_e:
                return root


            left_root_val = preorder[pre_s+1]

            left_subtree_post_index = post_dic[left_root_val]

            left_subtree_size = left_subtree_post_index - post_s + 1

            root.left = Construct(pre_s+1, pre_s + left_subtree_size, post_s, left_subtree_post_index)

            root.right = Construct(pre_s + left_subtree_size+1, pre_e, left_subtree_post_index+1, post_e-1)


            return root


        return Construct(0, len(preorder)-1, 0, len(postorder)-1)