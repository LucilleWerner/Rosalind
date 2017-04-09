
def main():

    file = open("parents")

    prob = calc_prob(file)
    print("Probability of dominant allele: " + str(prob))

def calc_prob(file):
    n_k = file.read().split()
    k = int(n_k[0])
    m = int(n_k[1])
    n = int(n_k[2])
    tot = k+m+n
    Pk = float(k/tot)
    Pm = float(m/tot)
    Pn = float(n/tot)

    k1 = float((Pk*Pk*1)+(Pk*Pm*1)+(Pk*Pn*1))
    m1 = float((Pm*Pk*1)+(Pm*Pm*0.75)+(Pm*Pn*0.5))
    n1 = float((Pn*Pk*1)+(Pn*Pm*0.5)+(Pn*Pn*0))

    prob = float(k1+m1+n1)

    return prob

main()
