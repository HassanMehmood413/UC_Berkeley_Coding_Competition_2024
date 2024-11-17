def is_rectangle(grid, N, M):
    # Check if the shape is a rectangle
    first_hash_positions = []
    last_hash_positions = []
    
    for i in range(N):
        row = grid[i]
        first_hash = row.find('#')
        last_hash = row.rfind('#')
        
        if first_hash != -1:  # There is at least one '#'
            # Ensure that the '#' block is contiguous
            if row[first_hash:last_hash + 1] != '#' * (last_hash - first_hash + 1):
                return False
            first_hash_positions.append(first_hash)
            last_hash_positions.append(last_hash)
    
    # Ensure that all rows with '#' symbols have the same first and last '#' positions
    if len(set(first_hash_positions)) == 1 and len(set(last_hash_positions)) == 1:
        return True
    return False

def is_triangle(grid, N, M):
    # Check for triangle:
    hash_counts = [row.count('#') for row in grid]
    
    # Remove rows without any '#'
    hash_counts = [count for count in hash_counts if count > 0]
    
    if not hash_counts:
        return False

    # Check if the hash counts form a strictly increasing or strictly decreasing pattern
    increasing = True
    decreasing = True
    
    for i in range(1, len(hash_counts)):
        if hash_counts[i] < hash_counts[i - 1]:
            increasing = False
        if hash_counts[i] > hash_counts[i - 1]:
            decreasing = False
    
    # The shape is a triangle if the counts are either strictly increasing or strictly decreasing
    return increasing or decreasing

def process_test_case(grid, N, M):
    # First check for rectangle
    if is_rectangle(grid, N, M):
        return "ferb"
    # Then check for triangle
    elif is_triangle(grid, N, M):
        return "phineas"
    return "Unknown"

# Main function to handle multiple test cases
if __name__ == "__main__":
    T = int(input())  # Number of test cases
    for _ in range(T):
        N, M = map(int, input().split())  # Grid dimensions
        grid = [input().strip() for _ in range(N)]  # The grid
        result = process_test_case(grid, N, M)
        print(result)
