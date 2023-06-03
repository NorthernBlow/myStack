S: str = 'cycle of death'
sum: int = 0
ascii_list: list = []

for i in S:
    ord(i)
    sum += ord(i) + ord(i)
    if ord(i) not in ascii_list:
        ascii_list.append(ord(i))
        #print(ascii_list)

print(ascii_list, 'это асци лист')

mmmap = map(ord, S)

print(mmmap)
