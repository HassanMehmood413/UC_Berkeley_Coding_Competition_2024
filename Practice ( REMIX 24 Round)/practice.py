from collections import Counter

def minimize_expected_payment(n, die_faces):
    # Count the frequency of each number on the die
    freq = Counter(die_faces)
    
    # Total number of faces
    total_faces = len(die_faces)
    
    # Initialize variables to track the minimum expected payment and the optimal number
    min_expected_payment = float('inf')
    optimal_number = None
    
    # Iterate over each unique number on the die
    for x in freq:
        # Calculate the total sum excluding the faces equal to x
        total_sum = sum(face for face in die_faces if face != x)
        
        # Calculate the expected payment as a fraction (sum of remaining faces / total faces)
        expected_payment = total_sum / total_faces
        
        # Update the optimal number if this expected payment is lower
        if expected_payment < min_expected_payment:
            min_expected_payment = expected_payment
            optimal_number = x
    
    return optimal_number


# Function to solve each test case
def solve(N):
    die_faces = list(map(int, input().split()))  # Read die faces as a space-separated list
    optimal_number = minimize_expected_payment(N, die_faces)
    return optimal_number


# Main function
def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())  # Read the number of sides for each test case
        s = solve(N)
        print(s)  # Solve and print the result for each test case


if __name__ == '__main__':
    main()
