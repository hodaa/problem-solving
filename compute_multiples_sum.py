def compute_multiples_sum(n):
    res= list()
    for i in range(3,n):
        if i % 3 == 0 or i %5 ==0 or i%7 ==0 :
            res.append(i)

    # return sum(res)
    return res




print(compute_multiples_sum(11))