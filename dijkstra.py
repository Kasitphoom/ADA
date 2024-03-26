"""min weight"""

import heapq

def min_weight(maze, N, M):
    """Find the minimum total weight from the top-left to the bottom-right cell."""
    # Initialize the heap for Dijkstra's algorithm
    heap = [(maze[0][0], 0, 0)]  # (weight, row, col)

    # Initialize the array of visited cells
    visited = [[False]*M for _ in range(N)]

    # While there are cells to explore
    while heap:
        weight, row, col = heapq.heappop(heap)

        # If we have reached the bottom-right cell
        if row == N - 1 and col == M - 1:
            return weight  # Return the total weight

        # If the cell has already been visited, skip it
        if visited[row][col]:
            continue

        # Mark the cell as visited
        visited[row][col] = True

        # Explore the neighboring cells
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc

            # If the new cell is inside the maze
            if 0 <= new_row < N and 0 <= new_col < M:
                # Add the new cell to the heap
                new_weight = weight + maze[new_row][new_col]
                heapq.heappush(heap, (new_weight, new_row, new_col))

    # If there is no path to the bottom-right cell
    return -1

# Read the input
n,m= map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# Print the minimum total weight
print(min_weight(maze, n,m))