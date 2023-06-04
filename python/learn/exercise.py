import functools


S: str = 'cycle of death'
sum: int = 0
ascii_list: list = []

for i in S:
    ord(i)
    if ord(i) not in ascii_list:
        ascii_list.append(ord(i))
        #print(ascii_list)

#print(ascii_list, 'это асци лист')

#mmmap = map(ord, S)


#for code in map(ord, S):
#    print(code)



#why = [code for code in map(ord, S)]
#print(why)


#HASH: dict = {'name': 'goremyka', 'lvl': 29, 'race': 'elly'}



#for key in HASH.keys():
#    sorted_list = []
#    sorted_list.append(key)
#    sorted_list.sort()
#   # print(sorted_list)



#sorted_list = list(filter(sorted, HASH))
#print(sorted_list)



L = [1, 2, 3, 4, 5, 6, 7, 16, 32, 64]
X = 5
found = False

i = 0

while not found and i < len(L):
    if 2 ** X == L[i]:
        found = 1
    else:
        i += 1


    if found:
        print('at index', i)

    else:
        print(X, 'not found')







