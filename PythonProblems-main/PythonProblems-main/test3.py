# def count_troikas(items):
#     troika_dict={}
#     count=0
#     for i in range(len(items)):
#         if items[i] not in troika_dict:
#             troika_dict[items[i]]=[i]
#         else:
#             troika_dict[items[i]].append(i)
#     print(troika_dict)


# print(count_troikas( [-8, -8, -8, -18, -8, 13, -8]))

# def safe_squares_bishops(n, bishops):
#     covered_squares=[]
#     for x in range(n):
#         for y in range(n):
#             for bishop in bishops:
#                 if (abs(x-bishop[0])==abs(y-bishop[0])) and (x, y) not in covered_squares:
#                     covered_squares.append((x,y))
#     print(covered_squares)
#     return n*n-len(covered_squares)

# print(safe_squares_bishops(4,  [(2, 3), (0, 1)]))

# def collapse_intervals(items):
#     result_lists=[]
#     results=''
#     pointer=0
#     if len(items)==1:
#         return str(items[0])
#     for i in range(1, len(items)):
#         if items[i-1]!=items[i]-1:
#             result_lists.append(items[pointer:i])
#             pointer=i
#         if i==len(items)-1:
#             result_lists.append(items[pointer:])
#     for interval in result_lists:
#         if len(interval)>1:
#             results+=f'{interval[0]}-{interval[len(interval)-1]},'
#         else:
#             results+=f'{interval[0]},'
#     print(result_lists)
#     return results[:-1]


# print(collapse_intervals( [1, 2, 3]))

def prominences(height):
    results=[]
    print(height[0-1:0+2])
    for i in range(0, len(height)):
        if max(height[i-1:i+2])==height[i]:
            print("Y")
            results.append((i, height[i], 0))
    print(results)

print(prominences( [4, 2, 100, 99, 101, 2]))


# def count_troikas(items):
#     troika_dict={}
#     count=0
#     for i in range(len(items)):
#         if items[i] not in troika_dict:
#             troika_dict[items[i]]=[i]
#         else:
#             troika_dict[items[i]].append(i)
#     print(troika_dict)


# print(count_troikas( [-8, -8, -8, -18, -8, 13, -8]))

# def safe_squares_bishops(n, bishops):
#     covered_squares=[]
#     for x in range(n):
#         for y in range(n):
#             for bishop in bishops:
#                 if (abs(x-bishop[0])==abs(y-bishop[0])) and (x, y) not in covered_squares:
#                     covered_squares.append((x,y))
#     print(covered_squares)
#     return n*n-len(covered_squares)

# print(safe_squares_bishops(4,  [(2, 3), (0, 1)]))

# def collapse_intervals(items):
#     result_lists=[]
#     results=''
#     pointer=0
#     if len(items)==1:
#         return str(items[0])
#     for i in range(1, len(items)):
#         if items[i-1]!=items[i]-1:
#             result_lists.append(items[pointer:i])
#             pointer=i
#         if i==len(items)-1:
#             result_lists.append(items[pointer:])
#     for interval in result_lists:
#         if len(interval)>1:
#             results+=f'{interval[0]}-{interval[len(interval)-1]},'
#         else:
#             results+=f'{interval[0]},'
#     print(result_lists)
#     return results[:-1]


# print(collapse_intervals( [1, 2, 3]))

from fractions import Fraction
# def prominences(height):
#     results=[]
#     print(height[0-1:0+2])
#     for i in range(0, len(height)):
#         if max(height[i-1:i+2])==height[i]:
#             print("Y")
#             results.append((i, height[i], 0))
#     print(results)

# print(prominences( [4, 2, 100, 99, 101, 2]))

def fractran(n, prog, giveup):
    results=[n]
    count=0
    while len(results)<=giveup:
        for frc in prog:
            print(frc)
            count+=1
            print((Fraction(*frc)*n), n, count)
            if (Fraction(frc[0],frc[1])*n).is_integer():
                results.append(int((frc[0]/frc[1])*n))
                n=int((frc[0]/frc[1])*n)
                break
        else:
            return results
    return results
    

print(fractran(7, [(7,3), (12, 7)], 10))
