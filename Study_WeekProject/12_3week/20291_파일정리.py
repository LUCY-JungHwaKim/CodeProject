n = int(input())

ary = []
dict = {}

for i in range(n):
    tmp = str(input())
    ary.append(tmp)

for i in range(n):
    splt_str = ary[i].split('.')
    if splt_str[1] not in dict:
        dict[splt_str[1]] = 1
    else:
        dict[splt_str[1]] += 1
dict_keys = sorted(dict.keys(), reverse = False)
dict_srt = {key : dict[key] for key in dict_keys}

for key, value in dict_srt.items():
    print(key, value)