import numpy as np


# Computes the Discret Fourier Transform on a set of points and returns an array containing the complex Fourier's coefficients
def dft(points):
    NbrPts = len(points)
    fourierCoef = []
    complexPoints = [complex(points[i][0], points[i][1]) for i in range(NbrPts)]
    for k in range(NbrPts):
        complexCoef_k = complex(0, 0)
        for n in range(NbrPts):
            complexCoef_k += complexPoints[n] * np.exp(-1j * 2 * np.pi * k * n / NbrPts)
        fourierCoef.append(complexCoef_k / NbrPts)
    return fourierCoef


# Takes as input the Complex Fourier's Coefficients and returns the data [radius, argument, frequency].
def getData(fourierCoef):
    dataCoef = []
    for k in range(len(fourierCoef)):
        coef = fourierCoef[k]
        rad = abs(coef)
        arg = np.angle(coef)
        freq = k
        dataCoef.append([rad, arg, freq])
    return dataCoef


# Sorts by radius the data get by the previous function
def sort(fourierCoef):
    sortCoef = []
    rad = np.array(fourierCoef)[:, 0]
    rad = np.sort(rad)
    for i in range(len(rad)):
        ind = np.where(np.array(fourierCoef)[:, 0] == rad[i])[0][0]
        sortCoef.append(fourierCoef[ind])
    return sortCoef[::-1]
