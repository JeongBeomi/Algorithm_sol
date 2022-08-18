for tc in range(10):
    n, numbers = input().split()
    stack = []
    for num in numbers:
        if len(stack) == 0 or stack[-1] != num:
            stack.append(num)
        else:
            stack.pop()

    print(f"#{tc+1}", end=" ")
    for i in stack:
        print(f"{i}", end="")
    print()