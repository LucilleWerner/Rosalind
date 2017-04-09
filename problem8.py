
def main():

    file = open("seq.txt")

    complement = get_complement(file)
    print(complement)

def get_complement(file):

    dna = file.read()
    complement = ""

    dna_dic = {"a": "t", "t": "a", "c": "g", "g": "c"}

    for nuc in reversed(dna):
        complement += dna_dic.get(nuc.lower())

    return complement

main()
