def solution(data, ext, val_ext, sort_by):
    data_label = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑기
    data = [d for d in data if d[data_label[ext]] < val_ext]
    
    # 정렬
    data.sort(key = lambda x : x[data_label[sort_by]])
    
    return data