def find_it(seq):
    lista_dic = {}
    for x in seq:
        lista_dic[x] = 1 if x not in lista_dic else lista_dic[x] + 1

    odd = list(filter(lambda i: i % 2 == 1, lista_dic.values()))
    
    for i in lista_dic:
        if lista_dic[i] == odd[0]:
            n = i
    
    return n