

def main():

    file = open("fasta.txt", "r")

    fasta = parse_fasta(file)
    #print(fasta)
    #output = compute_cg(fasta)

    #print(output)

def parse_fasta(file):

    lines = file.read()
    fasta = []
    strand = ""
    go = True

    fasta_list = list(filter(None, lines.split(">")))

    for strand in fasta_list:
        header = strand.split()[0]
        dna = "".join(strand.split()[1:])
        fasta.append([header, dna])


    return fasta

main()
