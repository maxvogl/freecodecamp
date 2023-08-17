import numpy as np

def calculate(mylist):
    """
    Function to calculate the mean, variance, standard deviation, max, min,
    and sum of the rows, columns, and elements in a 3 x 3 matrix.

    :param mylist:  (list) a list containing 9 numbers
    :return:  (dict) a dictionary of statistical values
                     in both axes (row, column) and flattened
    """
    if len(mylist) == 9:
        mean = []
        var = []
        std = []
        max = []
        min = []
        sum = []
        mat = np.reshape(np.array(mylist), (3,3))
        for i in [0, 1, None]:
            mean.append(np.mean(mat, axis=i).tolist())
            var.append(np.var(mat, axis=i).tolist())
            std.append(np.std(mat, axis=i).tolist())
            max.append(np.max(mat, axis=i).tolist())
            min.append(np.min(mat, axis=i).tolist())
            sum.append(np.sum(mat, axis=i).tolist())


        calculations = {'mean': mean,
                        'variance': var,
                        'standard deviation': std,
                        'max': mean,
                        'min': min,
                        'sum': sum}
    else:
        raise ValueError("List must contain nine numbers.")

    return calculations