print("Do Multiplication ")

n = int(input("Enter number :-"))

idx = 1

for t in range(n, n*10+1, n):
	print(n ,"x", idx, "=", t)
	idx += 1
