def klever_permutation(n, k):
    # Create two halves of the sequence
    first_half = list(range(1, n // 2 + 1))
    second_half = list(range(n // 2 + 1, n + 1))
    
    permutation = []
    
    # Weave the two halves together
    for i in range(k // 2):
        permutation.append(second_half.pop())
        permutation.append(first_half.pop())
    
    # Add the remaining numbers in order
    permutation += first_half[::-1] + second_half
    
    # If k is not equal to n, adjust the sequence by rotating it
    if k != n:
        permutation = permutation[-(k // 2):] + permutation[:-(k // 2)]
    
    return permutation

# Example usage:
t = int(input())  # Number of test cases
for _ in range(t):
    n, k = map(int, input().split())  # Read n and k
    print(*klever_permutation(n, k))  # Generate and print the k-level permutation
