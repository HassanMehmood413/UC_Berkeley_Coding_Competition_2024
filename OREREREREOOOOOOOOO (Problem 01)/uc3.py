def draw_cookies(test_cases):
    results = []  # List to store results for all test cases

    for test in test_cases:
        arr = []  # List to store lines for the current test case
        token = ""  # Accumulate characters to form tokens

        for char in test:
            token += char  # Append current character to the token

            if token == 'O':
                arr.append("[###OREO###]")  # Add line for 'O'
                token = ""  # Reset token
            elif token == 'RE':
                arr.append("[--------]")  # Add line for 'RE'
                token = ""  # Reset token
            elif token == '&':
                arr.append("")  # Add an empty line for '&'
                token = ""  # Reset token

        results.append("\n".join(arr))  # Combine all lines for this test case

    return results


if __name__ == "__main__":
    t = int(input())  # Number of test cases
    test_cases = [input().strip() for _ in range(t)]  # Input for each test case
    results = draw_cookies(test_cases)  # Process test cases

    for res in results:
        print(res)  # Print results for each test case
