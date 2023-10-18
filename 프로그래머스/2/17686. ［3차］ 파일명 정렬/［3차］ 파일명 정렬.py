def solution(files):
    answer = []
    split_files = []
    # HEAD, NUMBER, TAIL 나눠서 저장
    for file in files:
        # 숫자가 시작하는 인덱스, 끝나는 인덱스
        num_start, num_end = 0, len(file)
        for i in range(len(file)):
            if file[i].isnumeric():
                num_start = i
                # 숫자가끝나는 위치 찾기
                for j in range(i + 1, len(file)):
                    if not file[j].isnumeric():
                        num_end = j
                        break
                break
        split_files.append((file[:num_start], file[num_start : num_end], file[num_end :]))
    
    split_files.sort(key = lambda x : (x[0].upper(), int(x[1])))    
    
    for f in split_files:
        answer.append("".join(f))
        
    return answer