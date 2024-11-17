def min_time_to_exit(N, H, D, S, P):
    time_to_exit = D / S
    damage_taken = time_to_exit * P
    
    if N >= damage_taken:
        return time_to_exit
    
    # Case 2: When running alone is not enough, we need to heal during running
    # Calculate the time needed to heal enough before running
    
    if P >= H:
        return -1.0
    
    # Calculate the time needed to heal enough to compensate for storm damage
    # Healing time needed to compensate for storm damage
    healing_time_needed = (damage_taken - N) / (H - P)
    
    total_time = healing_time_needed + time_to_exit
    return total_time

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, H, D, S, P = map(int, input().split())
        result = min_time_to_exit(N, H, D, S, P)
        print(f"{result:.6f}")
