


# Input: S = “ckjkUUYII”
# Output: 5




def countCamelCase(S):

	
	count = 0

	
	for i in range(len(S)):
		
		if (ord(S[i]) >= 65 and ord(S[i]) <= 91):
			count += 1

	print(count)

if __name__ == '__main__':
	S = "ckjkUUYII"
	countCamelCase(S)

 