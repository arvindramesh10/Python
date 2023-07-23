

# Longest Common Prefix

input = ["apple","ape","april"]

input.sort()

common_prefix = ""
for i in range(min(len(input[0]), len(input[-1]))):
    if input[0][i] == input[-1][i]:
        common_prefix += input[0][i]
    else:
        break

print("Longest Common Prefix:", common_prefix)
