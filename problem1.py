
def main():

    file = open("rosalind_dna.txt", "r");

    dna_counts = calculate_lengths(file)
    print(dna_counts)

def calculate_lengths(file):

    dna_string = file.read();

    a_count = dna_string.count("A")
    t_count = dna_string.count("C")
    c_count = dna_string.count("G")
    g_count = dna_string.count("T")

    dna_counts = str(a_count) + " " + str(t_count) + " " + str(c_count) + " " + str(g_count)

    return dna_counts

main()
