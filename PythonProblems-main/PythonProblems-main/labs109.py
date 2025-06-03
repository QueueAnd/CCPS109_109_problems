# import math
# import numpy

# def ryerson_letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return 'A+'
#     elif n > 84:
#         return 'A'
#     elif n > 79:
#         return 'A-'
#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         adjust = "-"
#     elif ones > 6:
#         adjust = "+"
#     else:
#         adjust = ""
#     return "DCB"[tens - 5] + adjust

# def is_ascending(items):
#     if len(items) <= 1:
#         return True
#     for i in range(1, len(items)):
#         if (items[i - 1] >= items[i]):
#             return False
#     return True

# def riffle(items, out=False):
#     result = []
#     if len(items) == 0:
#         return []

#     half = int(len(items) / 2)

#     part_one = items[:half]
#     part_two = items[half:]

#     for i in range(half):
#         to_append = [part_one[i], part_two[i]]
#         result.extend(to_append if out else to_append[::-1])

#     return result

# def only_odd_digits(n):
#     if n <= 0:
#         return False
#     while n > 0:
#         digits = n % 10
#         if digits % 2 == 0:
#             return False
#         n = n // 10
#     return True

# def is_cyclops(n):
#     if n < 0:
#         return False
#     if n == 0:
#         return True

#     count = 0
#     num_zeroes, zero_pos = 0, 0
#     while n > 0:
#         count += 1
#         far_right_digit = n % 10
#         if far_right_digit == 0:
#             num_zeroes += 1
#             zero_pos = count
#             if num_zeroes > 1:
#                 return False
#         n //= 10
#     if zero_pos != count // 2 + 1 or count % 2 == 0 or num_zeroes == 0:
#         return False
#     return True

# def domino_cycle(tiles):
#     if len(tiles) == 0:
#         return True
#     chain = []
#     for domino in tiles:
#         chain.extend(domino)
#     if chain[0] != chain[len(chain) - 1]:
#         return False
#     for i in range(1, len(chain) - 1, 2):
#         if chain[i] != chain[i + 1]:
#             return False
#     return True

# import math

# def colour_trio(colours):
#     colour_keys = {
#         'r': {
#             'y': 'b',
#             'b': 'y',
#             'r': 'r'
#         },
#         'y': {
#             'b': 'r',
#             'r': 'b',
#             'y': 'y'
#         },
#         'b': {
#             'r': 'y',
#             'y': 'r',
#             'b': 'b'
#         }
#     }

#     if len(colours) == 1:
#         return colours
#     elif len(colours) == 2:
#         return colour_keys[colours[0]][colours[1]]

#     while len(colours) > 1:
#         temp_row = ''
#         for i in range(len(colours) - 1):
#             temp_row += colours[i] if colours[i] == colours[
#                 i + 1] else colour_keys[colours[i]][colours[i + 1]]
#         colours = temp_row
#         if (math.log(len(temp_row) - 1, 3)).is_integer():
#             return colour_keys[colours[0]][colours[-1]]

# def count_dominators(items):
#     items = items[::-1]
#     max_num = items[0]
#     n = 1
#     for x in items:
#         if x > max_num:
#             max_num = x
#             n += 1
#     return n

# def extract_increasing(digits):
#     num_to_beat = -1
#     results = []

#     num_to_beat = -1
#     current = 0
#     for i in range(len(digits)):
#         d = int(digits[i])
#         current = 10 * current + d
#         if current > num_to_beat:
#             results.append(current)
#             num_to_beat = current
#             current = 0

#     return results

# def words_with_letters(words, letters):
#     results = []
#     for word in words:
#         count = 0
#         for word_letter in word:
#             if letters[count] == word_letter:
#                 count += 1
#             if count == len(letters):
#                 results.append(word)
#                 break
#     return results

# def taxi_zum_zum(moves):
#     directions = ('N', 'E', 'S', 'W')
#     direction_keys = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
#     index = 0
#     pos = [0, 0]
#     curr_direction = directions[index]
#     for move in moves:
#         if move == 'F':
#             pos[0], pos[1] = pos[0] + direction_keys[curr_direction][0], pos[
#                 1] + direction_keys[curr_direction][1]
#         else:
#             index = index + 1 if move == 'R' else index - 1
#             if index > len(directions) - 1:
#                 index = 0
#             elif index < 0:
#                 index = len(directions) - 1
#             curr_direction = directions[index]
#     return tuple(pos)

# def give_change(amount, coins):
#     results = []
#     index = 0
#     while amount != 0:
#         if (coins[index] <= amount):
#             amount -= coins[index]
#             results.append(coins[index])
#         else:
#             index += 1
#     return results

# def safe_squares_rooks(n, rooks):
#     danger_columns = []
#     danger_rows = []
#     for rook in rooks:
#         if rook[0] not in danger_rows:
#             danger_rows.append(rook[0])
#         if rook[1] not in danger_columns:
#             danger_columns.append(rook[1])
#     occupied_squares = len(danger_rows) * n + len(danger_columns) * n - len(
#         danger_rows) * len(danger_columns)
#     return n * n - occupied_squares

# def words_with_given_shape(words, shape):
#     results = []
#     for word in words:
#         if len(word) == len(shape) + 1:
#             prev = ''
#             is_shape = True
#             for i in range(len(word)):
#                 if prev == '':
#                     prev = word[i]
#                     continue
#                 else:
#                     order = 1 if word[
#                         i] > prev else 0 if word[i] == prev else -1
#                     if order != shape[i - 1]:
#                         is_shape = False
#                         break
#                     prev = word[i]
#             if is_shape:
#                 results.append(word)
#     return results

# def is_left_handed(pips):
#     sorted_pips = sorted(pips)
#     return True if pips in (sorted_pips, pips[-1:len(pips)]) else False

# def is_left_handed(pips):
#     left_handed_order = {5: 4, 4: 2, 2: 3, 3: 5}

#     if pips[1] not in left_handed_order:
#         pips.insert(0, pips.pop(len(pips) - 1))
#     if 1 not in pips:
#         pips.reverse()
#     pips = list(filter(lambda x: x not in (1, 6), pips))
#     return True if left_handed_order[pips[0]] == pips[1] else False

# def winning_card(cards, trump=None):
#     card_ranking = {
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eight": 8,
#         "nine": 9,
#         "ten": 10,
#         "jack": 11,
#         "queen": 12,
#         "king": 13,
#         "ace": 14
#     }
#     highest = cards[0]
#     for current in cards:
#         if current[1] == trump and highest[1] != trump:
#             highest = current
#         elif (current[1] == highest[1]):
#             if (card_ranking[current[0]] > card_ranking[highest[0]]):
#                 highest = current

#     return highest

# def reverse_vowels(text):
#     vowel_list, collected_vowels='aeiouAEIOU', []
#     result=''
#     for i in text:
#         if i in vowel_list:
#             collected_vowels.append(i)
#     for i in text:
#         if i in vowel_list:
#             result+=collected_vowels.pop().lower() if i in 'aeiou' else collected_vowels.pop().upper()
#         else:
#             result+=i
#     return result

# def count_and_say(digits):
#     count, result= 0, ''
#     if len(digits)==0:
#         return ''
#     current_digit=digits[0]
#     for i in range(len(digits)):
#         if current_digit==digits[i]:
#             count+=1
#         else:
#             result+=f'{count}{current_digit}'
#             count=1
#             current_digit=digits[i]
#     result+=f'{count}{current_digit}'
#     return result

# def remove_after_kth(items, k=1):
#     occurence_dict={}
#     results=[]
#     for i in set(items):
#         occurence_dict[i]=0
#     for item in items:
#         if occurence_dict[item]<k:
#             results.append(item)
#             occurence_dict[item]+=1
#     return results

# def count_carries(a,b):
#     count, prev_rem=0, 0
#     while a!=0 or b!=0:
#         rem=a%10+b%10-10+prev_rem
#         a=a//10
#         b=b//10
#         if rem>=0:
#             prev_rem=1
#             count+=1
#         else:
#             prev_rem=0
#     return count

# def expand_intervals(intervals):
#     results=[]
#     ranges=intervals.split(',')
#     if intervals=='':
#         return []
#     for item in ranges:
#         split=item.split('-')
#         if len(split)>1:
#             results.extend(x for x in range(int(split[0]), int(split[1])+1))
#         else:
#             results.append(int(item))
#     return results

# def duplicate_digit_bonus(n):
#     points=0
#     lowest_digits=True
#     count=0
#     while n>0:
#         prev=n%10
#         n=n//10
#         count+=1
#         if n%10!=prev:
#             if count>=2:
#                 points+=((10**(count-2))*2) if lowest_digits else 10**(count-2)
#             lowest_digits=False
#             count=0
#     return points

# def reverse_ascending_sublists(items):
#     results=[]
#     lower_bounds=0
#     prev=items[0]
#     for i in range(1, len(items)):
#         if items[i]<=prev:
#             results.extend(items[lower_bounds:i][::-1])
#             lower_bounds=i
#         prev=items[i]
#     results.extend(items[lower_bounds:][::-1])
#     return results

# def unscramble(words, word):
#     results=[]
#     for item in words:
#         is_word=True
#         temp_word=word
#         if len(word)==len(item) and word[0]==item[0] and word[len(word)-1]==item[len(word)-1] :
#             for letter in item:
#                 if letter in temp_word:
#                     temp_word=temp_word.replace(letter, '', 1)
#                 else:
#                     is_word=False
#                     break
#             if is_word:
#                 results.append(item)
#     return results

# def collapse_intervals(items):
#     results=''
#     if items==[]:
#         return ''
#     elif len(items)==1:
#         return f'{items[0]}'
#     lower_bounds=items[0]
#     for i in range(1, len(items)):
#         if items[i]!=items[i-1]+1:
#             if lower_bounds==items[i-1]:
#                 results+=f'{lower_bounds},'
#                 if i==len(items)-1:
#                     results+=f'{items[i]}'
#             else:
#                 results+=f'{lower_bounds}-{items[i-1]},'
#             lower_bounds=items[i]
#         elif i==len(items)-1:
#             results+=f'{lower_bounds}-{items[i]}'
#         else:
#             results+=f'{items[i]},'
#     return results

# def arithmetic_progression(items):
#     stride_count={}

#     for i in range(1, len(items)):
#         stride=items[i]-items[i-1]
#         if stride not in stride_count:
#             stride_count[stride]={"count":1, "start": items[i-1], "current": items[i]}
#         else:
#             stride_count[stride]["count"]+=1
#         for x in stride_count:
#             if items[i]-stride_count[x]["current"]==x:
#                 stride_count[x]["count"]+=1
#                 stride_count[x]["current"]=items[i]
#     max_stride, max_count=0, 0
#     for y in stride_count:
#         print(y, stride_count[y]["count"], max_count)
#         if stride_count[y]["count"]>max_count:
#             max_stride=y
#             max_count=stride_count[y]["count"]
#     print(stride_count)
#     return (stride_count[max_stride]["start"], max_stride, stride_count[max_stride]["count"])


# def tukeys_ninthers(items):
#     while len(items) > 1:
#         temp_list = []
#         for i in range(0, len(items), 3):
#             temp_list.append(sorted(items[i:i + 3])[1])
#         items = temp_list
#     return items[0]

# def sum_of_two_squares(n):
#     i, j = 1, n

#     while math.sqrt(j).is_integer() is False:
#         print(j)
#         j -= 1
#     j = math.sqrt(j)

#     while i < j:
#         print(j, i, i * i + j * j)
#         if i * i + j * j == n:
#             return (int(j), int(i))
#         else:
#             i += 1

# def knight_jump(knight, start, end):
#     jump_distance=[int(abs(x)) for x in numpy.subtract(start, end)]
#     return all(x in jump_distance for x in knight)

# def seven_zero(n):
#     def gen_seven_zero(d):
#         for i in range(1, d+1):
#             yield ('7'*i)+('0'*(d-i))
            
#     if n%2!=0 and n%5!=0:
#         result='7'
#         while int(result)%n!=0:
#             result+='7'
#         return int(result)
#     else:
#         d=1
#         while True:
#             for x in gen_seven_zero(d):
#                 if int(x)%n==0:
#                     return int(x)
#             d+=1

# def can_balance(items):
#     index=0
#     while index<len(items):
#         left_side, right_side=items[0:index][::-1], items[index+1:]
#         left_weight, right_weight=0,0
#         for i in range(len(left_side)):
#             left_weight+=left_side[i]*(i+1)
#         for i in range(len(right_side)):
#             right_weight+=right_side[i]*(i+1)
#         if left_weight==right_weight:
#             return index
#         index+=1
#     return -1

# def group_and_skip(n, out, ins):
#     results=[]
#     while n>=out:
#         leftover=n%out
#         results.append(leftover)
#         n=(int(((n-leftover)/out)*ins))
#     else:
#         results.append(n%out)
#     return results

# def count_growlers(animals):
#     growl_count=0
#     for i in range(len(animals)):
#         left_facing=True if animals[i] in ('cat', 'dog') else False
#         compared_side=animals[0:i] if left_facing else animals[i+1:]
#         temp_count=0
#         for j in compared_side:
#             if j in ('dog', 'god'):
#                 temp_count+=1
#         if temp_count>len(compared_side)-temp_count:
#             growl_count+=1
#     return growl_count

# def bulgarian_solitaire(piles, k):
#     loops=0
#     while not all(x in piles for x in range(1, k+1)):
#         temp_results=[]
#         count=0
#         for x in piles:
#             count+=1
#             if x-1>0:
#                 temp_results.append(x-1)
#         temp_results.append(count)
#         piles=temp_results
#         loops+=1
#     return(loops)

# def scylla_or_charybdis(moves, n):
#     k, min_k = 1, 1
#     min_steps = len(moves)
#     while k < len(moves):
#         position, num_steps = 0, 0
#         for i in range(k-1, len(moves), k):
#             position = position + 1 if moves[i]=='+' else position - 1
#             num_steps += 1
#             if(abs(position)>n-1) and min_steps>num_steps:
#                 min_k=k
#                 min_steps=num_steps
#                 continue
#         k += 1
#     return min_k

# def collect_numbers(perm):
#     inv=[0]*(len(perm))
#     for i in range(0, len(perm)):
#         inv[perm[i]]=i
#     count=1
#     for j in range(1, len(inv)):
#         if inv[j]<inv[j-1]:
#             count+=1
#     return count

# def frequency_sort(items):
#     result, frequency_dict= [],{}
#     for x in items:
#         if x in frequency_dict:
#             frequency_dict[x]+=1
#         else:
#             frequency_dict[x]=1
#     order=sorted(frequency_dict.keys(), key=lambda x: (frequency_dict[x], -x))[::-1]
#     for y in order:
#         result+=[y]*frequency_dict[y]
#     return result

# def arithmetic_progression(items):
#     max_start=items[0]
#     max_length=0
#     max_stride=0
#     for i in range(len(items)):
#         for j in range(i + 1, len(items)):
#             stride = items[j] - items[i]
#             length=2 #initial lenght for each loop
#             previous_item=items[j] #initialize the start for each loop
#             for k in range(j+1, len(items)):
#                 if items[k]-previous_item==stride:
#                     length = length +1
#                     previous_item=items[k] #update the current item to compare with the next item
#             if length > max_length:
#                 max_start=items[i] #update the maximum length and its start and stride
#                 max_length=length
#                 max_stride=stride
#             if length >= len(items) -i:
#                 return(max_start,max_stride,max_length) # stop when the best possible result is found.
#     return(max_start,max_stride,max_length) # return in normal way

# def bridge_hand_shorthand(hand):
#     results=''
#     ranking="AKQJx-"
#     hand_dict={"spades":[],
#           "hearts":[],
#           "diamonds":[],
#           "clubs":[]}
#     for card in hand:
#         hand_dict[card[1]].append(card[0])
#     for suit in hand_dict:
#         if hand_dict[suit]==[]:
#             hand_dict[suit]=["-"]
#             continue
#         for i in range(len(hand_dict[suit])):
#             if hand_dict[suit][i] in ("king", "queen", "jack", "ace"):
#                 hand_dict[suit][i]=hand_dict[suit][i][0].upper()
#             else:
#                 hand_dict[suit][i]="x"
#     for suit in hand_dict:
#         results+=''.join(sorted(''.join(hand_dict[suit]), key=lambda cards: [ranking.index(card) for card in cards]))+' '
#     results=results[:len(results)]
#     return results

# def bridge_hand_shape(hand):
#     result=[]
#     hand_dict={"spades": 0,
#                "hearts": 0,
#                "diamonds": 0,
#                "clubs": 0
#                }
#     for card in hand:
#         if card[1] in hand_dict:
#             hand_dict[card[1]]+=1
#     result.extend([hand_dict[x] for x in hand_dict])
#     return result

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
    
# def substitution_words(pattern, words):
#     results=[]
#     for word in words:
#         letter_dict={}
#         if len(pattern)!=len(word):
#             continue
#         for i in range(len(pattern)):
#             if word[i] not in letter_dict and pattern[i] not in letter_dict.values():
#                 letter_dict[word[i]]=pattern[i]
#         for i in range(len(word)):
#             if word[i] not in letter_dict or letter_dict[word[i]]!=pattern[i]:
#                 break
#         else:
#             results.append(word)
#     return results

# def milton_work_point_count(hand, trump='notrump'):
#     score=0
#     ranking={
#         "ace": 4,
#         "king": 3,
#         "queen": 2,
#         "jack": 1
#     }
#     shape_bonus={
#         5: 1,
#         6: 2,
#         7: 3
#     }
#     count_dict={"spades": 0,
#                 "hearts": 0,
#                 "clubs": 0,
#                 "diamonds": 0}
#     for card in hand:
#         if card[0] in ranking:
#             score+=ranking[card[0]]
#         count_dict[card[1]]+=1
#     if [3, 3, 3, 4] == sorted(count_dict.values()):
#         score-=1
#     for x in count_dict:
#         if count_dict[x] in shape_bonus:
#             score+=shape_bonus[count_dict[x]]
#         elif count_dict[x]>=7:
#             score+=3
#         if trump!='notrump' and trump!=x:
#             if count_dict[x]==0:
#                 score+=5
#             elif count_dict[x]==1:
#                 score+=3
#     return score

# def verify_betweenness(perm, constraints):
#     inv=[0]*(len(perm))
#     for i in range(len(perm)):
#         inv[perm[i]]=i
#     for constraint in constraints:
#         if not (inv[constraint[0]]<inv[constraint[1]]<inv[constraint[2]] or inv[constraint[2]]<inv[constraint[1]]<inv[constraint[0]]):
#             return False
#     return True

# def first_preceded_by_smaller(items, k=1):
#     for i in range(len(items)):
#         count=0
#         for j in range(0, i):
#             if items[j]<items[i]:
#                 count+=1
#                 if count>=k:
#                     return items[i]
#     return None

# def sum_of_two_squares(n):
#     i, j=1, int(n**(1/2))
#     while i<=j:
#         x=i*i+j*j
#         if x==n:
#             return (j, i)
#         elif x>n:
#             j-=1
#         else:
#             i+=1

def collapse_intervals(items):
    result_lists=[]
    results=''
    pointer=0
    if len(items)==1:
        return str(items[0])
    for i in range(1, len(items)):
        if items[i-1]!=items[i]-1:
            result_lists.append(items[pointer:i])
            pointer=i
        if i==len(items)-1:
            result_lists.append(items[pointer:])
    for interval in result_lists:
        if len(interval)>1:
            results+=f'{interval[0]}-{interval[len(interval)-1]},'
        else:
            results+=f'{interval[0]},'
    return results[:-1]