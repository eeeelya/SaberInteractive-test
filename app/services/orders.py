def create_order_for_task(all_tasks, name):
    visited = set()
    paths = []

    def dfs(node, path):
        visited.add(node)
        path.append(node)

        for neighbor in all_tasks[node]:
            if neighbor not in visited:
                dfs(neighbor, path[:])

        paths.append(path)

    dfs(name, [])

    return [item[-1] for item in paths]
