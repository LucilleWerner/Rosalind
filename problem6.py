
def main():

    file = open("rosalind_hamm.txt", "r")

    output = compute_SNP(file)
    print(output)

def compute_SNP(file):

    dna = file.readlines()
    SNP_cnt = 0
    strand1 = dna[0].strip()
    strand2 = dna[1].strip()

    for nuc1, nuc2 in zip(strand1, strand2):
        if nuc1 != nuc2:
            SNP_cnt += 1

    return SNP_cnt

main()

