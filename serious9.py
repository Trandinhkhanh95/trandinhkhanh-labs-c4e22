def get_even_list(l):
    new_l = []
    for i in l:
        if i%2 == 0:
            new_l.append(i)
    print(new_l)
    return(new_l)
# get_even_list([1, 4, 5, -1, 10])