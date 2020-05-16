def generate(num_rows):
    if num_rows <= 0:
        return []

    if num_rows == 1:
        return [[1]]
    elif num_rows == 2:
        return [[1], [1,1]]
    else:
        result = [[1], [1,1]]

        for i in range(2, num_rows):
            prev_row = result[-1]
            new_row = [1]
            for j in range(1, i):
                new_elem = prev_row[j-1] + prev_row[j]
                new_row.append(new_elem)
            new_row.append(1)

            result.append(new_row)

        return result



if __name__ == '__main__':
    num_rows = 5

    result = generate(num_rows)

    print(result)