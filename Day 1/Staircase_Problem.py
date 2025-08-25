def count_ways(n, memo={}):
    # Base cases
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    # Check if already calculated
    if n in memo:
        return memo[n]
    
    # Calculate ways by taking 1 or 2 steps
    memo[n] = count_ways(n-1) + count_ways(n-2)
    return memo[n]

def main():
    stairs = 20
    total_ways = count_ways(stairs)
    
    print(f"For {stairs} stairs:")
    print(f"Total number of possible ways: {total_ways}")
    print(f"Probability of each way: {1/total_ways:.10f}")

if __name__ == "__main__":
    main()