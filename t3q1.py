 
# Read input
post_codes = list(map(int, input().split()))
desired_sum = int(input())

# Find pairs with desired sum and their indices
pairs = []
for i in range(len(post_codes)):
    for j in range(i+1, len(post_codes)):
        if post_codes[i] + post_codes[j] == desired_sum:
            pairs.append((i, j))

# Sort pairs by sum of indices
pairs.sort(key=lambda x: x[0] + x[1])

# Print the sum of indices for each pair
for pair in pairs:
    print(pair[0] + pair[1])