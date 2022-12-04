import numpy as np
from svg.path import Move, Line, CubicBezier, QuadraticBezier, Close
from svg.path import parse_path


def map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2

#Take as input a path encoded and interpolates its the path by using Bezier's functions
def getData(path, nbr_pts=400):
    #parse_path is used to decode svg's encoded path into instructions used after to interpolate the path.
    parsedPath = parse_path(path)
    pathlen = parsedPath.length(error=1e-4)
    nbrPts = 10 * nbr_pts
    nbrSteps = len(parsedPath)
    x_data = []
    y_data = []

    for i in range(nbrSteps):
        lenght = parsedPath[i].length(error=1e-5)
        subNbrPts = int(map(lenght, 0, pathlen, 0, nbrPts)) + 1
        t = np.linspace(0, 1, subNbrPts)
        #each step we check the type of the portion of the path and interpolate few points.
        if type(parsedPath[i]) == Move:
            x = parsedPath[i].start.real
            y = parsedPath[i].start.imag
            x_data = np.append(x_data, x)
            y_data = np.append(y_data, y)

        if type(parsedPath[i]) == Line:
            z1 = parsedPath[i].start
            z2 = parsedPath[i].end
            x = (1 - t) * z1.real + t * z2.real
            y = (1 - t) * z1.imag + t * z2.imag
            x_data = np.concatenate((x_data, x))
            y_data = np.concatenate((y_data, y))

        if type(parsedPath[i]) == QuadraticBezier:
            z1 = parsedPath[i].start
            z2 = parsedPath[i].control
            z3 = parsedPath[i].end
            x = (1 - t) ** 2 * z1.real + 2 * t * (1 - t) * z2.real + t ** 2 * z3.real
            y = (1 - t) ** 2 * z1.imag + 2 * t * (1 - t) * z2.imag + t ** 2 * z3.imag
            x_data = np.concatenate((x_data, x))
            y_data = np.concatenate((y_data, y))

        if type(parsedPath[i]) == CubicBezier:
            z1 = parsedPath[i].start
            z2 = parsedPath[i].control1
            z3 = parsedPath[i].control2
            z4 = parsedPath[i].end
            x = (1 - t) ** 3 * z1.real + 3 * t * (1 - t) ** 2 * z2.real + 3 * t ** 2 * (
                    1 - t) * z3.real + t ** 3 * z4.real
            y = (1 - t) ** 3 * z1.imag + 3 * t * (1 - t) ** 2 * z2.imag + 3 * t ** 2 * (
                    1 - t) * z3.imag + t ** 3 * z4.imag
            x_data = np.concatenate((x_data, x))
            y_data = np.concatenate((y_data, y))

        if type(parsedPath[i]) == Close:
            x = parsedPath[i].start.real
            y = parsedPath[i].start.imag
            x_data = np.append(x_data, x)
            y_data = np.append(y_data, y)

    points = [(x_data[i], y_data[i]) for i in range(len(x_data))]
    newpoints = [points[int(i)] for i in np.linspace(0, len(points) - 1, nbr_pts)]
    #return an array with the points of the path
    return np.array(newpoints)

#open an svg_file and parse the data to get the <path> encoded into it.
#return the different path as encoded strings
def getPath(svg_file):
    file = open(svg_file)
    file = file.read()
    file_path = []
    if '<path' in file:
        file = file.split('<path')
    for i in file:
        if ' d=' in i:
            item = '"'
            temp_path = i.split(' d=')[1]
            if item not in temp_path:
                item = "'"
            file_path.append(temp_path.split(item)[1])
    path = ''.join(file_path)
    return path


def opentxt(file_path):
    return np.loadtxt(file_path)

#galleryPaths = {
#    "fourier": fourier_svg,
#    "Sol": getPath("images/logos/svgs/sol.svg"),
#    "dear": getPath("images/logos/svgs/dear.svg"),
#    'linux': getPath("images/logos/svgs/linux.svg"),
#    "sigma": getPath("images/logos/svgs/sigma.svg"),
#    "iss": getPath("images/logos/svgs/iss.svg"),
#    "batman": getPath("images/logos/svgs/batman.svg")
#}
# for name in galleryPaths:
#    a = getData(galleryPaths[name])
#    b = fourier.dft(a)
#    c = fourier.getData(b)
#    d = fourier.sort(c)
#
# np.savetxt("preload/"+name+".txt", d)
# a = getData(galleryPaths['fourier'])
# b = fourier.dft(a)
# c = fourier.getData(b)
# d = fourier.sort(c)
#
# np.savetxt("preload/"+"fourier.txt", d)
