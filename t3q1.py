 
post_codes = list(map(int, input().split()))
desired_sum = int(input())
pairs = []
for i in range(len(post_codes)):
    for j in range(i+1, len(post_codes)):
        if post_codes[i] + post_codes[j] == desired_sum:
            pairs.append((i, j))
pairs.sort(key=lambda x: x[0] + x[1])
for z in pairs:
    print(z[0] + z[1])