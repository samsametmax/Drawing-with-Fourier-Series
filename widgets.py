import customtkinter as ct
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import fourier
import svgdata
import animation
import numpy as np

#define the common parameters which define the style of the animations
lightColor = {"line_color": "black", "path_color": "black", "circle_color": 'black'}
darkColor = {"line_color": "white", "path_color": "white", "circle_color": 'white'}

#used to add more buttons into the gallery page
galleryNames = {
    "Sol",
    "dear",
    'batman',
    "sigma",
    "iss"
}


# ===============================================

class upBar(ct.CTkFrame):
    #Button used to switch the theme of the app between {light and dark}
    class switchThemeButton(ct.CTkButton):
        def __init__(self, parent):
            super().__init__(parent, text="", image=None, command=self.switchTheme, fg_color=parent.fg_color, width=50,
                             height=50)
            self.parent = parent
            if ct.get_appearance_mode() == 'Light':
                self.img = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/darkmod.png").resize((20, 20)))
            else:
                self.img = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/lightmod.png").resize((20, 20)))
            self.configure(image=self.img)
            self.image = self.img

        def switchTheme(self):
            if ct.get_appearance_mode() == 'Light':
                ct.set_appearance_mode('Dark')
            else:
                ct.set_appearance_mode("Light")
            self.master.destroy()
            self.master.master.master.switchPage('Menu')

    def __init__(self, parent):
        super().__init__(parent, height=1)
        self.grid_columnconfigure([i for i in range(100)], weight=1)
        self.grid_rowconfigure(0, weight=1)
        if ct.get_appearance_mode() == "Light":
            backImg = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/back.png").resize((20, 20)))
            bgDraw = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/draw.png").resize((20, 20)))
            bgImport = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/import.png").resize((20, 20)))
            bgGallery = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/gallery.png").resize((20, 20)))
        else:
            backImg = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/back_light.png").resize((20, 20)))
            bgDraw = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/draw_light.png").resize((20, 20)))
            bgImport = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/import_light.png").resize((20, 20)))
            bgGallery = ImageTk.PhotoImage(Image.open("images/logos/upBarLogos/gallery_light.png").resize((20, 20)))

        #creating buttons that will be used to navigate through the app pages
        backButton = ct.CTkButton(self, text='', height=50, width=50, fg_color=self.fg_color, image=backImg,
                                  command=lambda: self.master.master.switchPage('Menu'))
        drawButton = ct.CTkButton(self, text='', width=50, height=50, fg_color=self.fg_color, image=bgDraw,
                                  command=lambda: self.master.master.switchPage('Draw'))
        importButton = ct.CTkButton(self, text='', width=50, height=50, fg_color=self.fg_color, image=bgImport,
                                    command=lambda: self.master.master.switchPage('Import'))
        galleryButton = ct.CTkButton(self, text='', width=50, height=50, fg_color=self.fg_color, image=bgGallery,
                                     command=lambda: self.master.master.switchPage('Gallery'))

        self.theme = ct.StringVar()
        activemode = ct.get_appearance_mode()

        themeSwitch = self.switchThemeButton(self)

        backButton.grid(column=0, row=0, columnspan=1, padx=15, pady=5, sticky='w')
        drawButton.grid(column=48, row=0, columnspan=1, padx=0, pady=5, sticky='')
        importButton.grid(column=49, row=0, columnspan=1, padx=0, pady=5, sticky='')
        galleryButton.grid(column=50, row=0, columnspan=1, padx=0, pady=5, sticky='')
        themeSwitch.grid(column=98, row=0, columnspan=1, padx=15, pady=5, sticky='e')


class mainMenu(ct.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.w, self.h = parent.width, parent.height
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        logoSize = (150, 70)

        if ct.get_appearance_mode() == 'Light':
            drawImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/draw.png").resize(logoSize))
            importImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/import.png").resize(logoSize))
            galleryImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/gallery.png").resize(logoSize))
        else:
            drawImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/draw_light.png").resize(logoSize))
            importImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/import_light.png").resize(logoSize))
            galleryImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/gallery_light.png").resize(logoSize))

        buttonOptions = {"text": '', 'width': 200, 'height': 90, "fg_color": self.fg_color}
        #Those buttons will be used to go to the corresponding Page on the main menu
        drawButton = ct.CTkButton(self,
                                  image=drawImg,
                                  command=lambda: self.master.switchPage('Draw'),
                                  **buttonOptions).grid(column=3, row=9)
        importButton = ct.CTkButton(self,
                                    image=importImg,
                                    command=lambda: self.master.switchPage('Import'),
                                    **buttonOptions).grid(column=5, row=9)
        galleryButton = ct.CTkButton(self,
                                     image=galleryImg,
                                     command=lambda: self.master.switchPage('Gallery'),
                                     **buttonOptions).grid(column=7, row=9)

        dataCoef = np.loadtxt("preload/fourier.txt")
        # Setting the style and parameters used to build the animation by using styleOptions and controlAnimation objects
        if ct.get_appearance_mode() == "Light":
            animStyle = animation.styleOptions(**lightColor)
        else:
            animStyle = animation.styleOptions(**darkColor)
        animControl = animation.controlAnimation(nbr_item=len(dataCoef),
                                                 origin=(20, 20),
                                                 speed=1,
                                                 loop=False,
                                                 show_circ=False,
                                                 pause=False)
        #We run the animation into the canvas
        self.animation = animation.Animation(self.canvas,
                                             data=dataCoef,
                                             styleOptions=animStyle,
                                             controlOptions=animControl)
        self.animation.init()
        # self.animation.animate()


# Every page {Draw, Import, Gallery} will inherit of the Page class
class Page(ct.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1000)
        self.upBar = upBar(self)
        self.upBar.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
        self.downFrame = None


class Draw(Page):
    # Creating a Frame object where the user can draw using his mouse and run the animation using the path.
    class drawingFrame(ct.CTkFrame):
        def __init__(self, parent):
            super().__init__(parent)
            self.penDown = False
            self.points = []
            self.lines = []
            if ct.get_appearance_mode() == 'Light':
                self.lineColor = 'black'
                imgStart = ImageTk.PhotoImage(Image.open("images/logos/start.png").resize((100, 40)))
                imgErase = ImageTk.PhotoImage(Image.open("images/logos/erase.png").resize((100, 40)))
            else:
                self.lineColor = 'white'
                imgStart = ImageTk.PhotoImage(Image.open("images/logos/start_light.png").resize((100, 40)))
                imgErase = ImageTk.PhotoImage(Image.open("images/logos/erase_light.png").resize((100, 40)))


            self.canvas.bind("<Button-1>", self.pressed)
            self.canvas.bind("<ButtonRelease>", self.released)
            self.canvas.bind("<Motion>", self.move)

            self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=10)
            self.grid_rowconfigure((10, 11), weight=1)
            self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

            self.startButton = ct.CTkButton(self, text='', image = imgStart, width=140, height=60, command=self.start)
            self.eraseButton = ct.CTkButton(self, text='', image=imgErase, width=140, height=60, command=self.erase)

            self.startButton.grid(column=2, row=9, columnspan=3, padx=5, pady=5, sticky='se')
            self.eraseButton.grid(column=5, row=9, columnspan=3, padx=5, pady=5, sticky='sw')

        def start(self):
            if len(self.points) > 2:
                fourierCoef = fourier.dft(self.points)
                dataCoef = fourier.getData(fourierCoef)
                dataCoef = fourier.sort(dataCoef)
                if ct.get_appearance_mode() == 'Light':
                    styleAnim = animation.styleOptions(**lightColor)
                else:
                    styleAnim = animation.styleOptions(**darkColor)

                controlAnim = animation.controlAnimation(nbr_item=len(dataCoef))
                self.master.downFrame.destroy()
                self.master.downFrame = Animation(self.master.master, data=dataCoef, style=styleAnim,
                                                  control=controlAnim, fromwhere=self)
                self.master.downFrame.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

        def erase(self):
            self.penDown = False
            for line in self.lines:
                self.canvas.delete(line)
            self.lines = []
            self.points = []

        def released(self, event):
            self.penDown = False

        def pressed(self, event):
            self.penDown = True

        def move(self, event):
            if self.penDown:
                if len(self.points) > 1:
                    line = self.canvas.create_line(event.x, event.y, self.points[-1][0], self.points[-1][1],
                                                   fill=self.lineColor)
                    self.lines.append(line)
                self.points.append((event.x, event.y))

    def __init__(self, parent):
        super().__init__(parent)
        # configure de Frame by splitting it into an upBar and a downFrame
        self.downFrame = self.drawingFrame(self)
        self.downFrame.grid(column=0, row=1, sticky='nsew', padx=10, pady=10)


class Import(Page):
    class importFrame(ct.CTkFrame):
        def __init__(self, parent):
            self.parent = parent
            super().__init__(parent)
            self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
            self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
            # self.import_button = ct.CTkButton(self, text='Import', command=self.openfile)
            # self.import_button.grid(column=3, columnspan=2, row=2)
            self.name_file = ct.CTkLabel(self, text='', fg_color=self.fg_color)
            self.drawing = None

        def openfile(self):
            self.file = askopenfile(mode='r', filetypes=[("image", ['*.svg'])])
            self.name_file.configure(text='File : ' + str(self.file).split('/')[-1].split("'")[0])
            self.name_file.grid(column=3, columnspan=2, row=4)
            if ct.get_appearance_mode() == 'Light':
                img = ImageTk.PhotoImage(Image.open("images/logos/animate.png").resize((100, 45)))
            else:
                img = ImageTk.PhotoImage(Image.open("images/logos/animate_light.png").resize((100, 45)))
            self.anim_b = ct.CTkButton(self, text='', image=img, command=self.animate, width=200, height=90, fg_color=self.fg_color)
            self.anim_b.grid(column=3, columnspan=2, row=3)
            self.drawing = getDataCoef(str(self.file).split("'")[1])

        def openfile_new(self):
            self.file = askopenfile(mode='r', filetypes=[("image", ['*.svg'])])
            # self.image = tk.PhotoImage(file=str(self.file).split("'")[1])
            self.drawing = getDataCoef(str(self.file).split("'")[1])
            self.animate()

        def animate(self):
            try:
                self.anim_b.grid_forget()
                self.name_file.grid_forget()
            except:
                print("Nothing There !")
            if ct.get_appearance_mode() == 'Light':
                styleAnim = animation.styleOptions(width=1100, height=600, **lightColor)
            else:
                styleAnim = animation.styleOptions(width=1100, height=600, **darkColor)
            controlAnim = animation.controlAnimation(nbr_item=len(self.drawing))
            self.master.downFrame.destroy()
            self.master.downFrame = Animation(self.master.master, data=self.drawing, style=styleAnim,
                                              control=controlAnim, fromwhere=self)
            self.master.downFrame.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

    def __init__(self, parent):
        super().__init__(parent)
        self.downFrame = self.importFrame(self)
        self.downFrame.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')
        self.downFrame.openfile()


class Gallery(Page):
    #creating a button object that can run an animation in background and run it if the button is clicked.
    class buttonGallery(ct.CTkButton):
        def __init__(self,
                     parent,
                     text='',
                     imgBg=None,
                     data=[]
                     ):
            super().__init__(parent, text='', command=lambda: self.startAnimation(data), width=200, height=200)
            self.img = imgBg
            self.data = data

            if ct.get_appearance_mode() == "Light":
                animStyle = animation.styleOptions(width=400, height=270, **lightColor)
            else:
                animStyle = animation.styleOptions(width=400, height=270, **darkColor)

            animControl = animation.controlAnimation(nbr_item=len(self.data),

                                                     speed=1,
                                                     loop=True,
                                                     show_circ=False,
                                                     pause=True)

            self.animation = animation.Animation(self.canvas,
                                                 data=self.data,
                                                 styleOptions=animStyle,
                                                 controlOptions=animControl)
            self.animation.init()
            #having the mouse hover the button will activate a preview of the animation
            #leaving the frame will then set to pause the animation
            self.bind("<Enter>", lambda e: animControl.setPause())
            self.bind("<Leave>", lambda e: animControl.setPause())
        #function used to run the application if the button is pressed.
        def startAnimation(self, data):
            if ct.get_appearance_mode() == 'Light':
                styleAnim = animation.styleOptions(width=1100, height=600, **lightColor)
            else:
                styleAnim = animation.styleOptions(width=1100, height=600, **darkColor)
            controlAnim = animation.controlAnimation(nbr_item=len(data))
            self.destroy()
            self.master.master.downFrame.destroy()
            self.master.master.downFrame = Animation(self.master.master.master,
                                                     data=data,
                                                     style=styleAnim,
                                                     control=controlAnim,
                                                     fromwhere=self)
            self.master.master.downFrame.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

    def __init__(self, parent):
        super().__init__(parent)
        self.ind = 0
        self.downFrame = ct.CTkFrame(self)
        self.downFrame.grid_columnconfigure((0, 1, 2), weight=1)
        self.downFrame.grid_rowconfigure((0, 1, 2), weight=1)
        self.downFrame.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')
        self.buildGallery()
    #creates as many button as there is path data into the dictionnary galleryNames.
    #to add a button just add a txt file that contains the data attached to the Fourier coefficients
    # of the path [(rad, arg, freq)].
    def buildGallery(self):
        for name in galleryNames:
            dataCoef = np.loadtxt("preload/" + str(name) + ".txt")
            button = self.buttonGallery(self.downFrame, text=name, data=dataCoef)
            button.grid(column=self.ind % 3, row=self.ind // 3, padx=10, pady=10, sticky='nesw')
            self.ind += 1

#a class that inherits from Page and will contain a Frame where the animation will run and its control bar.
class Animation(Page):
    class animationFrame(ct.CTkFrame):
        def __init__(self, parent, data, style, control):
            super().__init__(parent)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=100)
            # configure de Frame by splitting it into an upBar and a downFrame
            self.rightFrame = ct.CTkFrame(self)
            self.anim = animation.Animation(self.rightFrame.canvas, data=data, styleOptions=style,
                                            controlOptions=control)
            self.leftFrame = MenuAnimation(self)

            self.rightFrame.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')
            self.leftFrame.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
            self.anim.init()

    def __init__(self, parent, data, style, control, fromwhere=''):
        super().__init__(parent)
        self.fromwhere = fromwhere
        # configure de Frame by splitting it into an upBar and a downFrame
        self.downFrame = self.animationFrame(self, data=data, style=style, control=control)
        self.downFrame.grid(column=0, row=1, sticky='nsew', padx=10, pady=10)

#A control bar using widgets binded to the animation.
class MenuAnimation(ct.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        buttonOptions = {"text": '', 'width': 80, "height": 80, "fg_color": self.fg_color}
        logoSize = (40, 40)
        logoSize2 = (100, 45)
        logoSize3 = (80, 15)
        if ct.get_appearance_mode() == 'Light':
            playButtonImg = ImageTk.PhotoImage(Image.open("images/logos/play.png").resize(logoSize))
            stopButtonImg = ImageTk.PhotoImage(Image.open("images/logos/stop.png").resize(logoSize))
            drawImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/draw.png").resize(logoSize2))
            importImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/import.png").resize(logoSize2))
            galleryImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/gallery.png").resize(logoSize2))
            hideImg = ImageTk.PhotoImage(Image.open("images/logos/hidecircles.png").resize(logoSize3))
        else:
            playButtonImg = ImageTk.PhotoImage(Image.open("images/logos/play_light.png").resize(logoSize))
            stopButtonImg = ImageTk.PhotoImage(Image.open("images/logos/stop_light.png").resize(logoSize))
            drawImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/draw_light.png").resize(logoSize2))
            importImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/import_light.png").resize(logoSize2))
            galleryImg = ImageTk.PhotoImage(Image.open("images/logos/mainMenuLogos/gallery_light.png").resize(logoSize2))
            hideImg = ImageTk.PhotoImage(Image.open("images/logos/hidecircles_light.png").resize(logoSize3))
        hideCircle = ct.IntVar(0)
        animation = self.master.anim
        self.speedSlider = ct.CTkSlider(self,
                                        from_=2,
                                        to=80,
                                        number_of_steps=50,
                                        command=animation.controlOptions.setSpeed)
        self.nbrItemsSlider = ct.CTkSlider(self,
                                           from_=3,
                                           to=len(animation.data),
                                           number_of_steps=100,
                                           command=animation.controlOptions.setNbrItems)
        self.playButton = ct.CTkButton(self,
                                       image=playButtonImg,
                                       command=animation.controlOptions.setPause,
                                       **buttonOptions)
        self.stopButton = ct.CTkButton(self,
                                       image=stopButtonImg,
                                       command=animation.controlOptions.restart,
                                       **buttonOptions)
        self.labelHide = ct.CTkLabel(self, text='Hide Circles', fg_color=self.fg_color)
        self.hideCircleCheck = ct.CTkCheckBox(self,
                                              text="",
                                              command=animation.controlOptions.hideCirclesCheck)
        self.variableButton = ct.CTkButton(self,
                                           **buttonOptions)
        self.labelSpeed = ct.CTkLabel(self, text='Speed', fg_color=self.fg_color)
        self.labelItems = ct.CTkLabel(self, text='Number of Circles', fg_color=self.fg_color)
        type_parent = str(self.master.master.fromwhere)

        if type_parent != None:
            if 'gallery' in type_parent:
                self.variableButton.configure(text='',
                                              image=galleryImg,
                                              width=200,
                                              command=lambda: self.master.master.master.switchPage(
                                                  'Gallery'))  #### Ajouter commande
            elif 'import' in type_parent:
                self.variableButton.configure(text='',
                                              image=importImg,
                                              width=200,
                                              command=self.new_import)
            elif 'draw' in type_parent:
                self.variableButton.configure(text='',
                                              image=drawImg,
                                              width=200,
                                              command=lambda: self.master.master.master.switchPage('Draw'))

        self.variableButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='')
        self.playButton.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.stopButton.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.labelHide.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky='s')
        self.hideCircleCheck.grid(row=3, column=0, columnspan=2, sticky='n')


        self.labelItems.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky='sew')
        self.nbrItemsSlider.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='new')

        self.labelSpeed.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='sew')
        self.speedSlider.grid(row=7, column=0, columnspan=2, padx=5, sticky='new')


        # self.sliderLabel.grid(row=8, column=0, columnspan=2, padx=5, sticky='n')

        self.nbrItemsSlider.set(self.nbrItemsSlider.to)

        self.speedSlider.set(25)

    def new_import(self):
        self.master.master.fromwhere.openfile_new()


# ===============================================

# Map a coordinates n in the range [start1, stop1] into the range [start2, stop2]
def map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2

def getDataCoef(file_svg=None):
    if file_svg != None:
        path = svgdata.getPath(file_svg)
        points = svgdata.getData(path)
    else:
        points = []
    fourierCoef = fourier.dft(points)
    dataCoef = fourier.getData(fourierCoef)
    dataCoef = fourier.sort(dataCoef)
    return dataCoef
# ===============================================
