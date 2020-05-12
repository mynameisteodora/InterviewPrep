from operator import add

def spiralMatrix(matrix):

    if len(matrix) == 0:
        return []
    elif len(matrix[0]) == 0:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    c1 = 0
    c2 = n-1

    r1 = 0
    r2 = m - 1

    while c1 <= c2 and r1 <= r2:

        # top
        for col in range(c1, c2 + 1):
            result.append(matrix[r1][col])

        # right
        for row in range(r1+1, r2+ 1):
            result.append(matrix[row][c2])

        if r1 < r2 and c1 < c2:
            # left
            for col in range(c2-1, c1, -1):
                result.append(matrix[r2][col])

            # up
            for row in range(r2, r1, -1):
                result.append(matrix[row][c1])

        c1 += 1
        c2 -= 1
        r1 += 1
        r2 -= 1


    return result



if __name__ == '__main__':
    matrix = [[2,3,4]]

    result = spiralMatrix(matrix)

    print(result)
