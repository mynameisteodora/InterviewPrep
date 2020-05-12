def findDiagonalOrder(matrix):
    m, n = len(matrix), len(matrix[0])
    full_diag_length = min(m, n)
    full_diag_reps = abs(m - n) + 1
    iters = m + n - 1

    direction = 1
    current_diag_len = 1

    result = []

    current_row_idx = 0
    current_col_idx = 0

    current_diag_reps = 0

    while current_row_idx != m or current_col_idx != n:

        if current_row_idx < 0:
            current_row_idx = 0
        if current_row_idx > m - 1:
            current_row_idx = m - 1

        if current_col_idx < 0:
            current_col_idx = 0
        if current_col_idx > n - 1:
            current_col_idx = n - 1



        if direction == 1:
            direction = -1

            while current_row_idx >= 0 and current_col_idx <= n-1:
                result.append(matrix[current_row_idx][current_col_idx])

                if current_col_idx + 1 > n-1:
                    current_row_idx += 1
                else:
                    current_row_idx -= 1

                current_col_idx += 1

        elif direction == -1:
            direction = 1


            while current_row_idx <= m-1 and current_col_idx >=0:
                result.append(matrix[current_row_idx][current_col_idx])

                if current_row_idx + 1 > m-1:
                    current_col_idx += 1
                else:
                    current_col_idx -= 1
                current_row_idx += 1



    return result

if __name__ == '__main__':
    matrix = [['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]

    result = findDiagonalOrder(matrix)

    print(result)