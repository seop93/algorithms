# dfs 깊이 우선 탐색

# root 만 나한테줘 그러면 root가 가리키는 Tree에 속한 모든 노드를 접근해줄게
def dfs(root):
    if root is None:
        return 
    dfs(root.left)
    dfs(root.right)

# 전위순회(preorder)
def preorder(cur_node):
    if cur_node is None:
        return
    
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

# 중위순회(inorder)
def inorder(cur_node):
    if cur_node is None:
        return
    
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

# 후위순회(postorder)
def postorder(cur_node):
    if cur_node is None:
        return
    
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)

