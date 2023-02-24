import numpy as np
import constants as cst

def needlman(sequences):
    seq_names = list(sequences.keys())
    scores = np.zeros((len(seq_names),len(seq_names)))
    for i in range(len(seq_names) - 1):
        seq_1 = sequences[seq_names[i]]
        for j in range(i + 1, len(seq_names)):
            seq_2 = sequences[seq_names[j]]
            scores[i,j] = calculs(seq_1,seq_2)
    for i in range(len(seq_names) - 1):
        for j in range(i + 1, len(seq_names)):
            scores[j,i] = scores[i,j]
    return scores

def calculs(seq_1, seq_2):
    seq_1 = "-" + seq_1
    seq_2 = "-" + seq_2
    score_align = np.zeros((len(seq_1), len(seq_2)))
    for i in range(1,len(seq_1)):
        score_align[i,0] = score_align[i-1,0]+cst.SCORE_GAP
    for i in range(1,len(seq_2)):
        score_align[0,i] = score_align[0,i-1]+cst.SCORE_GAP
    for i in range(1,len(seq_1)):
        for j in range(1,len(seq_2)):
            aa1 = seq_1[i]
            aa2 = seq_2[j]
            aa1 = cst.DAA[aa1]
            aa2 = cst.DAA[aa2]
            score_1 = score_align[i-1 , j] - cst.SCORE_GAP
            score_2 = score_align[i , j-1] - cst.SCORE_GAP
            score_3 = score_align[i-1 , j-1] + cst.BLOSUM62[aa1,aa2]
            score_align[i,j] = max(score_1 , score_2 , score_3)
    return score_align[len(seq_1)-1,len(seq_2)-1]
