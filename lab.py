import random

l = [random.choice([i for i in range(100)]) for j in range(10)]

print("Massiv 1",l)


try:
	steps = int(input("Step: "))
	l = l[steps:] + l[:steps]

	print("Massiv 2",l)
except:
	print('Ne nado tak :c')
