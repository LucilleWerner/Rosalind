def main():

    file = open("rosalind_rna.txt", "r");

    rna_string = transcribe_dna(file)
    print(rna_string)

def transcribe_dna(file):

    dna_string = file.read();

    rna_string = dna_string.replace("T", "U")

    return rna_string

main()
