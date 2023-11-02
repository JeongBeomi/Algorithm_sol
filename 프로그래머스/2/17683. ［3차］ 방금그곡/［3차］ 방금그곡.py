def check_melody(play_time, melody, m):
    m_length = len(m)
    result = False
    for i in range(play_time - m_length + 1):
        for j in range(i, i + m_length):
            if m[j - i] != melody[j % len(melody)]:
                break
        else:
            # if melody[(j + 1) % len(melody)] != "#":
            result = True
            break
    return result


def solution(m, musicinfos):
    answer = ["(None)", 0]
    replace_dict = {"C#" : "c", "D#" : "d", "F#" : "f", "G#" : "g", "A#" : "a"}
    for k, v in replace_dict.items():
        m = m.replace(k, v)
    
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(",")
        
        for k, v in replace_dict.items():
            melody = melody.replace(k, v)
            
        # print(m, melody)
        
        play_time = (int(end_time[0:2]) - int(start_time[0:2])) * 60 + (int(end_time[3:5]) - int(start_time[3:5]))
        if check_melody(play_time, melody, m) == True and answer[1] < play_time:
            answer = [title, play_time]
    
    return answer[0]
