def print_matrix(matrix):
    for row in matrix:
        print(row)

def multiply_matrices(word_matrix, matrix):
    result = []
    for row in word_matrix:
        result_row = []
        for i in range(len(matrix[0])):
            result_row.append(sum([row[j] * matrix[j][i] for j in range(len(matrix))]))
        result.append(result_row)
    return result

user_word = input("Enter a word to Encode: ")
word = list(user_word.lower())
word_matrix = []
word_matrix_final = []
matrix_size = int(input("Enter the width of the matrix: "))
for char in word:
    word_matrix.append(ord(char) - 97) # CHANGE TO 96 IF A = 1

if len(word_matrix) > matrix_size:
    curr = 0
    for i in range(len(word_matrix) // matrix_size):
        word_matrix_final.append(word_matrix[curr:curr + matrix_size])
        curr += matrix_size
else:
    word_matrix_final.append(word_matrix)

matrix = []

for i in range(matrix_size):
    row = input("\nEnter Row " + str(i + 1) + " (Seperated By Spaces): ")
    row = row.split(" ")
    row = [int(i) for i in row]
    matrix.append(row)

mod_num = int(input("Enter the modulo number: "))

coded_values = multiply_matrices(word_matrix_final, matrix)

output_word = ""

for i in range(len(coded_values)):
    for num in coded_values[i]:
        output_word += chr((num % mod_num) + 97)

print(f"\nThe Encoded Word Is: {output_word.upper()}")


