# def maopao(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-i-1):
#             if list[j] < list[j+1]:
#                 l = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = l
#     return list

def houyi(list):
    l = []
    for i in range(1, len(list)):
        l.append(list[i])
    l.append(list[0])
    return l

print(houyi([1,3,2,5,4,1,1,0]))