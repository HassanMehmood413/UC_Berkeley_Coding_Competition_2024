from math import ceil

def calico(test_cases):
    calico_counts = {'C': 2, 'A': 1, 'L': 1, 'I': 1, 'O': 1} 

    results = []
    for s in test_cases:
        required_counts = {}
        
        for char in s:
            if char in "CU": 
                required_counts['C'] = required_counts.get('C', 0) + 1
            elif char in "NH":  
                if char == 'N':
                    required_counts['C'] = required_counts.get('C', 0) + 1
                else:  
                    required_counts['I'] = required_counts.get('I', 0) + 1
            elif char in calico_counts:
                required_counts[char] = required_counts.get(char, 0) + 1
            else:
                results.append(-1)
                break
        else:
            max_sets = 0
            for key, count in required_counts.items():
                max_sets = max(max_sets, ceil(count / calico_counts[key]))
            results.append(max_sets)
    
    return results

if __name__ == "__main__":
    t = int(input())
    test_cases = [input().strip() for _ in range(t)]
    results = calico(test_cases)
    for res in results:
        print(res)
