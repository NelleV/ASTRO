import numpy as np


def decompo(signal, filtre, num_iter=6):
    oh = [signal]
    residu = [np.zeros(signal.shape)]
    # FIXME this is going to be super slow
    for it in range(num_iter):
        w, = filtre.shape
        res = np.zeros(signal.shape)
        for j, line in enumerate(oh[it]):
            res[j] = np.convolve(line, filtre, mode='same')
        # Now, update the filter interfacing zeros
        hor = res
        res = np.zeros(signal.shape)
        for j, line in enumerate(hor.T):
            res.T[j] = np.convolve(line, filtre, mode='same')
        # Now, update the filter interfacing zeros
        oh.append(res)
        residu.append(oh[it] - res)

        new_filter = np.zeros((2 * filtre.shape[0] - 1))
        for i, element in enumerate(filtre):
            new_filter[2 * i] = element
        filtre = new_filter

    return (oh, residu)

filtre = np.array([1. / 16, 1. / 4, 3. / 4, 1. / 4, 1. / 16])

# 1D
signal = np.zeros((256, 256))
signal[126:130, 126:130] = 255
oh, res = decompo(signal, filtre, num_iter=6)
