def solution(new_id):
    # if 3 <= len(new_id) <= 15 and new_id[0] != '.' and new_id[-1] != '.':
    #     for s in new_id:
    #         if s.isalpha():


    new_id = new_id.lower()

    for c in new_id:
        if c.isnumeric() or c.islower() or c in ['-', '_', '.']:
            continue
        new_id = new_id.replace(c, '')

    i = 2
    while i < len(new_id):
        if new_id.find('.' * i) != -1:
            new_id = new_id.replace("." * i, '.')
            continue
        i += 1

    new_id = new_id.strip('.')

    if not new_id:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15].strip('.')

    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
