import numpy as np
def arbre(matrice,sequences):
    if matrice.shape == (2,2):
        return sequences
    else:
        seq_1, seq_2 = closest_sequences(matrice, sequences)
        updated_matrix = update_matrix(matrice, sequences.index(seq_1), sequences.index(seq_2))
        updated_sequences = update_seq(sequences, seq_1, seq_2)
        return arbre(updated_matrix, updated_sequences)


def closest_sequences(matrices, sequences):
    highest_score = matrices.max()
    vector = np.array(matrices)
    agglomeration = np.where(vector == highest_score)
    seq_1 = agglomeration[0][0]
    seq_2 = agglomeration[0][1]
    seq_1 = sequences[seq_1]
    seq_2 = sequences[seq_2]
    return seq_1, seq_2


def update_seq(sequences, seq_1, seq_2):
    updated_sequences = []
    sequences.remove(seq_1)
    sequences.remove(seq_2)
    updated_sequences.append([seq_1, seq_2])
    for i in range(0, len(sequences)):
        updated_sequences.append(sequences[i])
    return updated_sequences



def update_matrix(matrice, seq_1, seq_2):
    dimension = matrice.shape
    temporary_matrix = np.delete(matrice, seq_1, 0)
    temporary_matrix = np.delete(temporary_matrix, seq_2 - 1, 0)
    temporary_matrix = np.delete(temporary_matrix, seq_1, 1)
    temporary_matrix = np.delete(temporary_matrix, seq_2 - 1, 1)
    new_matrix = np.zeros((dimension[0]-1, dimension[0]-1))
    dimension_2 = temporary_matrix.shape
    for i in range(0, dimension_2[0]):
        for j in range(0, dimension_2[0]):
            new_matrix[i+1,j+1] = temporary_matrix[i ,j]
    dimension_3 = new_matrix.shape
    for i in range(1, dimension_3[0]):
        new_matrix[0, i] = (matrice[i, seq_1] + matrice[i, seq_2])/2
        new_matrix[i, 0] = new_matrix[0 ,i]
    return new_matrix
