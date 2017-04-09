def main():

    file = open("rosalind_revc.txt", "r");

    complement_string, org_string = complement_dna(file)
    print(org_string)
    print(complement_string)

def complement_dna(file):

    org_string = file.read();
    dna_string = org_string

    dna_string = dna_string.replace("T", "a")
    dna_string = dna_string.replace("C", "g")
    dna_string = dna_string.replace("A", "T")
    dna_string = dna_string.replace("G", "C")
    dna_string = dna_string.upper()

    complement_string = dna_string[::-1]

    return complement_string, org_string

main()
