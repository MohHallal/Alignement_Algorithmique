import alignement
import upgma
def seperating_sequences(file):
    with open(file, "r", encoding="utf-8") as fasta_file:
        seq = ""
        seq_name = ""
        dico_seqs = {}
        for line in fasta_file:
            if line[0] == ">":
                if seq:
                    dico_seqs[seq_name] = seq
                    seq = ""
                seq_name = line[1:].strip()
            else:
                seq = seq + line.strip()
        if seq:
            dico_seqs[seq_name] = seq
        return dico_seqs
if __name__=="__main__":
    input_file = "opsines"
    sequences = seperating_sequences(input_file)
    alignement.needlman_alignement(sequences["seq1"],sequences["seq2"])
    scores = alignement.needlman_score(sequences)
    sequences_names = list(sequences.keys())
    tree = upgma.arbre(scores,sequences_names)
    print(tree)