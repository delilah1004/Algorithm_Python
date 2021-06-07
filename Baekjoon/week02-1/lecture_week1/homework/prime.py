input = 20


def find_prime_list_under_number(number):
    num_array = [True] * (number+1)
    result = []

    for i in range(2, int(number**0.5)+1) :
      if num_array[i] :
        for idx in range(i+i, number+1, i) :
          num_array[idx] = False

    for idx in range(2, number+1) :
      if num_array[idx] :
        result += [idx]

    return result

result = find_prime_list_under_number(input)
print(result)