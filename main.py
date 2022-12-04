import widgets
import customtkinter as ct
from screeninfo import get_monitors

#Creating the main window as a class
class fourierDrawingApp(ct.CTk):
    def __init__(self, w, h):
        super().__init__()
        self.width = w
        self.height = h
        self.title('Fourier Drawing')
        self.geometry(f"{w}x{h}")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.currentPage = None
        self.switchPage('Menu')
    #used to switch between the different Pages of the app. Destroys and Creates the pages
    def switchPage(self, frameName):
        if self.currentPage is not None:
            self.currentPage.destroy()
        if frameName == "Menu":
            self.currentPage = widgets.mainMenu(self)
        if frameName == "Draw":
            self.currentPage = widgets.Draw(self)
        if frameName == "Import":
            self.currentPage = widgets.Import(self)
        if frameName == "Gallery":
            self.currentPage = widgets.Gallery(self)
        self.currentPage.grid(row=0, column=0, pady=10, padx=10, sticky="nswe")


if __name__ == '__main__':
    w, h = (get_monitors()[0].width, get_monitors()[0].height)
    ct.set_appearance_mode("Light")
    ct.set_default_color_theme("theme.json")
    app = fourierDrawingApp(w, h)
    app.minsize(w * 0.90, h * 0.90)
    app.mainloop()
