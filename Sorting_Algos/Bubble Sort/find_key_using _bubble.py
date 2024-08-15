elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'kabir',  'transaction_amount': 700,  'device': 'samsung'},
        { 'name': 'lanson',  'transaction_amount': 900,  'device': 'lava'}
    ]

# print(len(elements))
# for i in range(len(elements)-1):
#     print(elements[i]["name"])
# # print(elements[i])


def b_j_sort(elements,key):
    size =len(elements)

    for i in range(size-1):
        for j in range(size-1):
            a = elements[j][key]
            b = elements[j+1][key]
            if a>b:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp

    return elements


print(b_j_sort(elements,key="name"))
print(b_j_sort(elements,key="device"))
