from collections import deque

pair_dict = {")": "(", "]": "["}

while True:
    input_text = input()
    if input_text == ".":
        break

    result = "no"
    s = deque()

    for t in input_text:
        if t in ("(", "["):
            s.append(t)
        elif t in (")", "]"):
            if s and s[-1] == pair_dict[t]:
                s.pop()
            else:
                break
    else:
        if not s:
            result = "yes"

    print(result)
