# 최빈값 찾기

input = "hello my name is sparta"

def find_max_occured_alphabet_ascii(array):
    max_num = array[0]
    max_idx = 0
    dup = False
    for idx in range(1,len(array)) : 
      if max_num < array[idx] :
        max_num = array[idx]
        max_idx = idx
        
    return max_idx + ord('a')


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for s in string :
      if s.isalpha() :
        alphabet_occurrence_array[ord(s)-ord('a')] += 1

    result_ascii = find_max_occured_alphabet_ascii(alphabet_occurrence_array)

    return chr(result_ascii)

print(find_max_occurred_alphabet(input))



# input = "abacabade"


# def find_not_repeating_character(array):
#     not_repeating_character_array = []

#     for idx in range(len(array)) :
#       print(array[idx])
      
#       if array[idx] == 1 :
#         not_repeating_character_array += chr(idx + ord('a'))

#     if len(not_repeating_character_array) == 0 :
#       return "_"
#     else :
#       return not_repeating_character_array[0]


# def find_max_occurred_alphabet(string):
#     alphabet_occurrence_array = [0] * 26

#     for s in string :
#       if s.isalpha() :
#         alphabet_occurrence_array[ord(s)-ord('a')] += 1

#     return find_not_repeating_character(alphabet_occurrence_array)


# result = find_not_repeating_character(input)
# print(result)