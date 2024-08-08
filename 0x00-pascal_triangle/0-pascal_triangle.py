#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''


def pascal_triangle(n):
    '''
    Function to find Pascal's Triangle integers

        Parameters:
            n (int): The number of row's of Pascal's triangle

        Returns:
            pascal_triangle (list): Binary string of the sum of a and b
    '''
    if n <= 0:
        return []
    result = [[1]]

    for i in range(1, n):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)

    return result
