import tkinter as tk
import numpy as np
from screeninfo import get_monitors


fourier_svg = "m 978.141,416.063 c 7.732,-7.25 21.793,1.315 26.098,1.45 14.066,0.442 28.632,-1.293 34.314,-0.725 9.666,0.966 32.381,0.725 39.147,-3.142 0,0 -2.9,-0.967 -6.767,-1.45 -3.866,-0.483 -6.766,-2.9 -12.565,-2.9 -3.057,0 -12.083,3.383 -14.016,3.383 -1.934,0 -8.216,-3.866 -15.949,-2.9 -7.732,0.967 -13.049,5.286 -16.915,5.286 l -5.8,2.93 c 6.766,5.8 18.365,12.566 31.897,11.599 13.532,-0.966 13.049,0 27.064,-8.216 14.017,-8.216 18.366,-12.566 16.433,1.45 -1.933,14.016 8.699,-11.116 8.699,-11.116 0,0 2.741,-9.988 0,-22.715 -1.931,-8.964 -15.466,-16.432 -19.332,-20.298 0,0 -11.437,-31.415 -13.532,-42.531 -1.291,-6.849 12.083,2.417 19.332,6.766 7.25,4.35 26.099,-7.249 30.448,-10.149 4.349,-2.9 -3.384,-9.666 -9.253,-9.753 -3.54,2.867 -7.693,5.403 -15.396,5.403 -10.633,0 -28.031,-5.8 -28.031,-5.8 0.483,-9.504 -5.958,-26.259 4.995,-35.281 16.264,-13.397 25.36,-15.109 37.535,-10.149 4.35,1.771 22.393,25.615 22.393,25.615 0,0 -9.668,12.888 -12.889,11.599 -3.221,-1.288 -16.109,-14.821 -21.909,-14.821 -5.8,0 -23.198,2.577 -25.132,6.443 -1.934,3.867 -5.154,15.466 -2.577,12.244 2.577,-3.222 7.733,-6.444 7.733,-6.444 0.819,2.97 3.605,6.928 7.249,6.928 4.271,0 7.733,-3.029 7.733,-6.766 0,-1.413 -0.497,-2.722 -1.343,-3.806 0.463,-0.04 0.91,-0.061 1.343,-0.061 6.766,0 22.231,11.599 22.231,11.599 0,0 26.581,8.7 26.581,18.366 0,9.666 0.643,23.356 0.643,23.356 0,0 30.931,2.577 33.508,-15.466 2.577,-18.043 -12.887,-43.82 -5.154,-43.82 7.733,0 22.557,-21.261 22.557,-21.261 0,0 -7.732,6.444 -25.135,8.374 7.732,-2.578 18.044,-25.776 18.044,-36.086 0,-10.31 5.154,-15.466 -18.044,-25.776 15.465,-7.733 15.465,-38.664 -2.577,-61.862 -18.043,-23.199 -25.775,-7.733 -25.775,-7.733 0,0 9.024,-25.127 -7.085,-41.237 -15.678,-15.679 -31.579,-10.314 -31.579,-10.314 0,0 3.227,-19.972 -17.396,-27.705 -20.621,-7.733 -39.953,18.043 -35.443,7.732 5.166,-11.808 -14.176,-36.086 -14.176,-36.086 0,0 2.577,18.043 -10.31,28.998 -18.526,15.749 -33.514,-14.182 -56.712,-16.76 -23.198,-2.578 -30.931,12.889 -30.931,12.889 0,0 -5.434,-9.285 -25.126,-1.285 -20.622,8.377 -19.978,23.198 -19.978,23.198 0,0 -14.174,-1.932 -32.219,10.956 -18.045,12.888 -15.472,36.726 -15.472,36.726 0,0 -13.022,5.827 -23.198,23.198 -10.95,18.692 -5.154,48.974 -5.154,48.974 0,0 -12.889,10.311 -15.466,25.776 -2.577,15.466 15.466,33.509 15.466,33.509 0,0 -12.889,5.155 -15.466,12.888 -2.577,7.733 0,28.354 20.62,43.819 -7.732,12.888 0,28.354 5.156,38.664 5.156,10.31 25.775,15.466 25.775,15.466 0,0 12.889,20.621 2.579,23.198 -10.31,2.577 -23.199,7.734 -23.199,25.777 0,18.043 -15.465,69.595 -20.621,90.216 -20.622,5.155 -28.353,28.354 -28.353,28.354 0,0 2.577,10.31 -12.889,15.465 -15.465,5.156 -56.707,43.818 -64.439,54.13 -7.732,10.312 -43.82,33.509 -56.708,51.551 -12.889,18.045 -53.11,87.379 -54.13,136.613 -1.125,54.294 -4.029,128.715 -2.577,134.035 1.452,5.319 25.777,7.736 43.822,12.892 18.044,5.156 76.041,29.643 101.816,34.798 25.775,5.156 68.306,25.777 81.194,24.488 12.889,-1.29 11.6,-41.243 11.6,-48.976 0,-7.733 -6.443,-37.377 -7.733,-50.264 -1.29,-12.887 -2.577,-36.087 0,-50.263 2.577,-14.177 10.312,-37.373 9.022,-47.685 -1.289,-10.312 -16.576,-35.107 -14.178,-33.51 34.797,23.198 14.178,94.083 14.178,108.259 0,14.177 6.443,68.308 1.288,106.972 -5.155,38.664 5.156,27.064 27.065,34.798 21.909,7.732 70.885,5.153 118.57,9.021 47.687,3.866 112.124,2.739 131.456,-6.283 0,-11.6 2.901,-29.803 1.934,-42.53 -0.969,-12.729 -3.221,-58.155 -3.221,-60.733 0,-2.579 -12.887,-1.29 -12.887,-1.29 0,0 -4.648,12.185 -9.022,15.466 -7.732,5.8 -28.354,5.154 -31.577,0 -3.223,-5.154 -9.664,-23.196 0.646,-32.219 10.311,-9.022 23.056,-9.347 28.353,-1.934 6.445,9.021 21.266,8.377 21.266,8.377 0,0 -4.511,-27.712 -7.087,-37.376 -2.577,-9.664 -16.754,-43.816 -18.043,-48.973 -1.289,-5.155 -6.445,-29.644 -9.022,-33.51 -2.577,-3.866 -12.889,-2.579 -16.755,-1.289 -3.866,1.289 -1.752,9.707 -10.31,16.755 -10.956,9.022 -28.062,-0.977 -30.288,-5.8 -3.866,-8.376 0,-28.998 14.177,-30.287 14.176,-1.29 17.398,-0.644 19.978,7.089 2.58,7.733 14.176,-1.936 14.176,-4.512 0,-2.577 -15.465,-37.377 -21.908,-50.264 -6.443,-12.887 -19.332,-45.109 -27.065,-54.13 -7.732,-9.021 -15.466,-2.577 -15.466,-2.577 0,0 1.934,16.756 -5.799,26.422 -3.601,4.498 -25.929,11.886 -30.288,-0.646 -5.156,-14.819 -6.443,-25.775 7.733,-30.931 14.176,-5.154 18.688,3.866 25.131,-3.866 5.219,-6.261 9.666,-9.666 3.223,-21.909 -1.2,-2.282 0.002,-9.022 -10.31,-11.6 -10.312,-2.578 -19.332,-18.042 -22.554,-33.508 -2.904,-13.937 -21.263,-60.574 -27.708,-70.885 -6.445,-10.311 -3.867,-28.353 -7.733,-30.931 -3.867,-2.578 -28.356,-18.043 -45.109,-25.776 -16.753,-7.733 -28.353,-19.331 -33.508,-32.22 -5.155,-12.889 -6.443,-18.044 0,-24.488 0,0 25.773,22.554 28.351,28.998 2.578,6.444 48.976,38.664 52.842,43.819 3.867,5.155 11.6,23.199 11.602,26.421 0,0 25.775,29.643 32.219,37.375 6.443,7.733 11.76,34.638 19.492,51.391 7.732,16.753 21.75,25.938 34.637,22.071 12.887,-3.867 56.547,-6.285 66.856,-11.438 10.31,-5.154 4.833,-25.132 2.899,-53.163 -1.795,-26.034 11.439,-43.658 15.306,-55.257 l 10.312,-11.599 c 13.047,4.027 26.58,9.826 27.064,47.685 0.149,11.599 18.043,61.863 19.332,72.173 1.29,10.311 1.29,27.063 3.867,29.643 2.576,2.578 32.219,28.354 37.374,28.354 1.29,20.622 2.577,42.528 3.866,60.573 1.289,18.045 7.894,68.146 2.737,79.744 -5.155,11.6 -19.49,24.648 -23.356,37.537 -3.867,12.889 -21.909,50.264 -27.064,57.996 -5.156,7.733 -17.883,9.506 -18.045,15.466 -0.162,5.96 10.312,10.31 10.312,27.064 0,16.754 1.288,42.53 1.288,50.264 0,7.732 2.254,24.648 2.254,31.092 0,0 67.986,-7.57 89.894,-19.332 21.908,-11.762 64.763,-57.996 64.763,-57.996 12.889,-9.021 40.275,-25.937 38.986,-37.535 -2.122,-19.093 -6.334,-101.612 -7.089,-108.422 -1.288,-11.599 -18.687,-68.146 -27.709,-72.012 -9.022,-3.866 -56.706,-100.526 -61.86,-105.681 -5.154,-5.155 -48.976,-24.487 -55.419,-27.064 -6.443,-2.579 -27.064,-92.794 -27.064,-95.372 0,0 -47.041,-31.575 -48.33,-36.086 -1.29,-4.511 13.853,-98.754 11.599,-100.526 -5.477,40.759 -21.91,112.771 -58.646,131.454 -18.042,7.733 -51.547,14.825 -95.366,-13.528 -43.82,-28.354 -67.017,-36.731 -82.482,-47.042 -15.465,-10.311 -16.111,-26.42 -16.111,-34.153 -14.178,-1.289 -16.749,-6.44 -21.265,-16.11 -6.983,-14.954 -16.753,-18.688 -21.909,-34.153 -5.156,-15.466 -5.16,-38.024 10.306,-30.292 15.466,7.733 20.625,12.893 28.358,30.936 7.732,18.043 9.658,-1.289 9.666,-19.332 0.003,-8.374 1.289,-10.956 5.799,-14.822 4.51,-3.866 43.495,-10.149 43.495,-10.149 10.149,-13.532 27.548,-25.131 43.014,-25.131 15.465,0 26.581,11.116 28.031,15.465 1.449,4.35 -4.673,13.694 -8.699,15.466 -3.957,1.741 -9.666,5.799 -23.199,6.766 -13.532,0.967 -23.198,-1.933 -30.931,-1.933 6.285,-8.86 12.226,-11.388 18.094,-14.975 l 0.271,0.476 c 0,4.271 3.895,7.733 8.699,7.733 4.804,0 8.7,-3.462 8.7,-7.733 0,-1.068 -0.244,-2.084 -0.684,-3.009 l 1.584,-0.213 c 6.027,0.915 11.665,3.223 16.498,6.123 4.833,2.899 12.405,2.738 14.338,-3.062 1.934,-5.799 -1.772,-12.87 -1.772,-24.487 0,-7.25 3.384,-11.277 2.417,-14.177 -0.967,-2.899 -19.336,-3.552 -32.864,-3.222 -19.815,0.483 -37.214,8.216 -47.847,14.016 l -35.281,27.548 c 0,-10.311 11.597,-33.834 -1.292,-38.99 -12.889,-5.156 -18.042,-28.354 -15.465,-36.087 15.465,7.733 39.957,14.825 46.4,9.67 6.443,-5.155 -28.354,-5.8 -30.931,-26.42 -2.577,-20.62 18.635,12.244 34.154,12.244 17.399,0 -23.198,-17.399 -13.532,-27.709 6.417,-6.845 22.229,-25.132 22.229,-25.132 0,0 -1.608,35.441 28.034,30.287 29.641,-5.155 47.686,-21.91 51.552,-27.065 18.045,-1.289 15.468,3.867 29.644,11.599 14.177,7.733 24.488,36.086 18.045,46.397 l 10.313,-24.487 c 5.155,-11.599 7.742,27.065 21.918,33.509 14.177,6.443 27.08,3.866 27.08,3.866 1.288,7.088 3.894,36.087 4.539,42.53 -10.954,-15.465 -11.579,-20.943 -20.399,-26.259 -8.82,-5.316 -32.019,-5.8 -40.476,-1.934 -8.458,3.867 -16.19,19.332 -16.19,27.065 0,0 -1.934,6.283 0,10.633 1.933,4.35 9.609,34.934 11.277,39.47 3.144,8.539 10.471,24.325 11.438,30.125 0.967,5.799 4.028,16.271 -3.867,19.332 -9.707,3.762 -8.699,1.933 -4.832,-4.833 3.866,-6.767 -2.37,-7.766 -5.316,-1.45 -3.384,7.25 -11.116,11.599 -15.949,7.733 -4.833,-3.866 0.967,-10.149 0,-12.083 -0.967,-1.934 -14.499,-2.9 -15.466,3.866 -0.967,6.767 -10.251,5.259 -13.532,-0.966 -4.671,-8.861 6.285,-16.271 6.285,-21.104 -7.733,5.8 -18.332,11.868 -27.709,21.909 -13.691,14.66 -20.815,42.976 -19.979,45.108 -0.005,10e-4 2.251,-2.899 9.985,-10.148 z"


monitor = get_monitors()[0]
w = monitor.width
h = monitor.height


# ===============================================

class styleOptions:
    def __init__(self,
                 line_color='white',
                 circle_color='white',
                 path_color='white',
                 line_size=2,
                 circle_size=2,
                 path_size=2,
                 width=w,
                 height=h):
        self.lineColor = line_color
        self.circColor = circle_color
        self.pathColor = path_color
        self.lineSize = line_size
        self.circSize = circle_size
        self.pathSize = path_size
        self.width = width
        self.height = height


class controlAnimation:
    def __init__(self,
                 nbr_item,
                 origin=(50, 0),
                 path_max=1,
                 speed=25,
                 loop=False,
                 pause=True,
                 show_circ=True,
                 anim=None):
        self.loop = loop
        self.speed = speed
        self.pause = pause
        self.nbrItems = nbr_item
        self.pathMax = path_max
        self.showCirc = show_circ
        self.origin = origin
        self.anim = anim

    def setPause(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True

    def setSpeed(self, value):
        self.speed = int(value)

    def setNbrItems(self, value):
        self.nbrItems = int(value)

    def restart(self):
        self.anim.t = 0

    def hideCirclesCheck(self):
        if self.showCirc:
            self.showCirc = False
            for circle in self.anim.circles:
                self.anim.canvas.itemconfigure(circle, state='hidden')
        elif not self.showCirc:
            self.showCirc = True
            for i in range(self.nbrItems - 1):
                circle = self.anim.circles[i]
                self.anim.canvas.itemconfigure(circle, state='normal')
        self.anim.manageCircles()

    def loopCheck(self):
        if not self.loop:
            self.loop = True
        else:
            self.loop = False


class Animation:
    def __init__(self, canvas, data, styleOptions, controlOptions):
        self.canvas = canvas
        self.data = data
        self.styleOptions = styleOptions
        self.controlOptions = controlOptions
        self.controlOptions.anim = self

        self.lines = []
        self.circles = []
        self.path = []
        self.path_line = []
        self.prevNbr = self.controlOptions.nbrItems
        self.maxItem = self.prevNbr
        self.t = 0
        self.dt = 2 * np.pi / len(data)
        # -------------------------------------------

        self.parentsize = min(self.styleOptions.width, self.styleOptions.height)

        w, h = getPathDimension(data)
        self.figsize = max(w, h)

    # -------------------------------------------

    def init(self):
        x = map(self.controlOptions.origin[0], 0, self.figsize, 0, self.parentsize)
        y = map(self.controlOptions.origin[1], 0, self.figsize, 0, self.parentsize)
        prevx, prevy = (x, y)
        for i in range(self.maxItem):
            # get the values {rad, arg, freq} of the i-th coefficient
            rad = self.data[i][0]
            arg = self.data[i][1]
            freq = self.data[i][2]
            # add the coordinates of the i-th point according to the values of its coefficient
            x += map(rad * np.cos(freq * self.t + arg), 0, self.figsize, 0, self.parentsize)
            y += map(rad * np.sin(freq * self.t + arg), 0, self.figsize, 0, self.parentsize)
            # we skip the first coefficient (largest in magnitude) in order to easily scale the figure
            if i != 0:
                radm = map(rad, 0, self.figsize, 0, self.parentsize)
                # create the i-th circle centered on the (i-1)-th coefficient's position
                # and of the radius the i-th coefficient's radius
                circ = self.canvas.create_oval(prevx - radm, prevy - radm, prevx + radm, prevy + radm,
                                               outline=self.styleOptions.circColor)
                # create a line between the (i-1)-th and the i-th coefficient's positions
                line = self.canvas.create_line(prevx, prevy, x, y,
                                               fill=self.styleOptions.lineColor,
                                               arrow=tk.LAST,
                                               arrowshape=(0.09 * radm, 0.09 * radm, 0.08 * radm))
                # store each indexes in order to manipulate the objects later
                self.circles.append(circ)
                self.lines.append(line)
            prevx, prevy = (x, y)
        if not self.controlOptions.showCirc:
            for circ in self.circles:
                self.canvas.itemconfigure(circ, state='hidden')
        self.animate()

    def animate(self):

        if not self.controlOptions.pause:
            if self.t != 0 and self.t % 2 * np.pi == 0 and not self.controlOptions.loop:
                self.controlOptions.pause = True
            # if the number of item to be displayed is changed then we hide the lines and circles
            if self.prevNbr != self.controlOptions.nbrItems:
                self.manageCircles()

            x = map(self.controlOptions.origin[0], 0, self.figsize, 0, self.parentsize)
            y = map(self.controlOptions.origin[1], 0, self.figsize, 0, self.parentsize)
            prevx, prevy = (x, y)
            for i in range(self.controlOptions.nbrItems):
                rad = self.data[i][0]
                arg = self.data[i][1]
                freq = self.data[i][2]
                x += map(rad * np.cos(freq * self.t + arg), 0, self.figsize, 0, self.parentsize)
                y += map(rad * np.sin(freq * self.t + arg), 0, self.figsize, 0, self.parentsize)
                if i != 0:
                    radm = map(rad, 0, self.figsize, 0, self.parentsize)
                    self.canvas.coords(self.lines[i - 1], prevx, prevy, x, y)
                    self.canvas.coords(self.circles[i - 1], prevx - radm, prevy - radm, prevx + radm, prevy + radm)
                prevx, prevy = (x, y)
            self.path.append((x, y))
            if len(self.path) > 2:
                line = self.canvas.create_line(self.path[-2][0], self.path[-2][1], self.path[-1][0], self.path[-1][1],
                                               fill=self.styleOptions.lineColor,
                                               width=3)
                self.path_line.append(line)
            #If the past is more than 95% drawn then we start deleting the first line of self.path_line
            if len(self.path) > self.maxItem * 0.95:
                self.canvas.delete(self.path_line[0])
                self.path_line.pop(0)
            self.t += self.dt

        self.canvas.after(self.controlOptions.speed, self.animate)
    #used to show/hide the circles
    def manageCircles(self):
        if self.prevNbr - self.controlOptions.nbrItems > 0:
            for i in range(self.controlOptions.nbrItems, self.maxItem):
                line = self.lines[i - 1]
                circle = self.circles[i - 1]
                self.canvas.itemconfigure(line, state='hidden')
                self.canvas.itemconfigure(circle, state='hidden')
        if self.prevNbr - self.controlOptions.nbrItems < 0:
            for i in range(self.prevNbr, self.controlOptions.nbrItems):
                line = self.lines[i - 1]
                circle = self.circles[i - 1]
                self.canvas.itemconfigure(line, state='normal')
                if self.controlOptions.showCirc:
                    self.canvas.itemconfigure(circle, state='normal')
        self.prevNbr = self.controlOptions.nbrItems


# ===============================================
#mapping value n in [start1, stop1] into [start2, stop2]
def map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2

#get the dimensions of the path to animate in order to scale it.
def getPathDimension(data):
    X, Y = [], []
    t = 0
    dt = 2 * np.pi / len(data)
    while t < 2 * np.pi:
        x, y = (0, 0)
        for i in range(len(data)):
            rad = data[i][0]
            arg = data[i][1]
            freq = data[i][2]
            x += rad * np.cos(freq * t + arg)
            y += rad * np.sin(freq * t + arg)
        X.append(x)
        Y.append(y)
        t += 2 * dt
    return max(X), max(Y)
