# Get all substrings of given string
def get_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    return substrings



def bfs(tree):
    queue = [tree]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node.val)
            visited.append(node)
            queue.append(node.children)