class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        result_map = {}
        height_cache = {}

        # Function to calculate the height of the tree
        def _height(node):
            if not node:
                return -1

            # Return cached height if already calculated
            if node in height_cache:
                return height_cache[node]

            h = 1 + max(_height(node.left), _height(node.right))
            height_cache[node] = h
            return h

        # DFS to precompute the maximum values after removing the subtree
        def _dfs(node, depth, max_val):
            if not node:
                return

            result_map[node.val] = max_val

            # Traverse left and right subtrees while updating max values
            _dfs(
                node.left,
                depth + 1,
                max(max_val, depth + 1 + _height(node.right)),
            )
            _dfs(
                node.right,
                depth + 1,
                max(max_val, depth + 1 + _height(node.left)),
            )

        # Run DFS to fill result_map with maximum heights after each query
        _dfs(root, 0, 0)

        return [result_map[q] for q in queries]