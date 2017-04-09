

def main():

    file = open("rosalind_gc.txt", "r")

    fasta = parse_fasta(file)
    output = compute_cg(fasta)

    print(output)

def parse_fasta(file):

    lines = file.read()
    fasta = []
    fasta_list = list(filter(None, lines.split(">")))

    for strand in fasta_list:
        header = strand.split()[0]
        dna = "".join(strand.split()[1:])
        fasta.append([header, dna])

    return fasta

def compute_cg(fasta):

    percentages = []

    for strand in fasta:
        dna = strand[1]
        strand_len = len(dna)
        c_cnt = dna.count("C")
        g_cnt = dna.count("G")
        cg_cnt = c_cnt + g_cnt
        percentages.append((cg_cnt/strand_len)*100)

    max_cg = max(percentages)
    max_id = percentages.index(max_cg)
    output = "{} {:.7}".format(fasta[max_id][0], max_cg).replace(" ", "\n")

    return output

main()
