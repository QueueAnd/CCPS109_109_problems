# import math
# def frog_collision_time(frog1, frog2):
#     if (frog2[1]!=frog1[1] and frog2[3]==frog1[3]) or (frog2[0]!=frog1[0] and frog2[2]==frog1[2]):
#         return None
#     coinc_y= 0 if (frog2[1]==frog1[1] and frog2[3]==frog1[3]) else -(frog2[1]-frog1[1])/(frog2[3]-frog1[3])
#     coinc_x= 0 if (frog2[0]==frog1[0] and frog2[2]==frog2[2]) else -(frog2[0]-frog1[0])/(frog2[2]-frog1[2])
#     if coinc_x==coinc_y:
#         return int(coinc_x)
#     elif coinc_y==0:
#         return int(coinc_x)
#     elif coinc_x==0:
#         return int(coinc_y)
#     else:
#         return None

# print(frog_collision_time( (-28, 9, 9, -4),   (-26, -5, 8, -2)))

def substitution_words(pattern, words):
    results=[]
    for word in words:
        letter_dict={}
        if len(pattern)!=len(word):
            continue
        for i in range(len(pattern)):
            print(pattern[i]) 
            if word[i] not in letter_dict and pattern[i] not in letter_dict.values():
                letter_dict[word[i]]=pattern[i]
        for i in range(len(word)):
            if word[i] not in letter_dict or letter_dict[word[i]]!=pattern[i]:
                break
        else:
            results.append(word)
    return results

print(substitution_words('LLRR', ['abba']))