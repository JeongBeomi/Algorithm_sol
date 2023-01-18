num_list = [int(input()) for _ in range(10)]
num_set = set()
for i in num_list:
    num_set.add(i % 42)
print(len(num_set))