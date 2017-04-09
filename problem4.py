
def main():

    file = open("rosalind_fib.txt", "r")

    n, k, Fn = calc_Fn(file)
    print("Number of bunny pairs after {} months with offspring of {}".format(n, k))
    print(Fn)

def calc_Fn(file):

    n_k = file.read().split()
    n = int(n_k[0])          #0> n =< 40 (= month no)
    k = int(n_k[1])          #0> k =< 5 (=no of offspring)

    if n != 1 and n != 2:

        F_2 = 1
        F_1 = 1
        for i in range(3, n+1):
            Fn = F_1 + (F_2*k)
            F_2 = F_1
            F_1 = Fn
    else:
        Fn = 1

    return n, k, Fn

main()





