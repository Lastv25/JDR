from tkinter import *
from tkinter import ttk
import functions


def validate_character(master, name, buff_type, duration):
    if len(name) == 0:
        name = 'No name'
    if len(buff_type) == 0:
        buff_type = 'None'
    if len(duration) == 0:
        duration = '0'
    functions.WriteNewCharacter(name, buff_type, duration)
    master.addCharacter(name)


def openCharacWindow(master):

    newWindow = Toplevel(master)
    newWindow.title("Character Window")

    name = StringVar()
    buff = StringVar()
    duration = StringVar()

    name_l = Label(newWindow, text="Name").grid(row=0, column=0)
    name_entry = Entry(newWindow, textvariable=name).grid(row=0, column=1, sticky=(N, W, E, S))

    buff_type_l = Label(newWindow, text="Buff Type").grid(row=1, column=0)
    buff_type_entry = Entry(newWindow, textvariable=buff).grid(row=1, column=1, sticky=(N, W, E, S))

    turn_number_L = Label(newWindow, text="Duration").grid(row=2, column=0)
    turn_number_entry = Entry(newWindow, textvariable=duration).grid(row=2, column=1, sticky=(N, W, E, S))

    validation_button = Button(newWindow, text="OK", command=lambda: validate_character(master, name.get(), buff.get(),
                                                                                        duration.get()))\
        .grid(column=3, row=0, rowspan=3, sticky=(N, W, E, S))



class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label1 = Label(self, text="URL").grid(row=0, sticky=(N, W, E, S))
        url_entry = Entry(self).grid(row=0, column=1, sticky=(N, W, E, S))
        ok_url = Button(self, text="Go").grid(column=2, row=0, sticky=(N, W, E, S))

        label2 = Label(self, text="Characters").grid(row=1, sticky=(N, W, E, S))
        self.listCharacters = Listbox(self, selectmode=SINGLE)
        self.listCharacters.grid(row=2, sticky=(N, W, E, S))
        self.current = None  # parameter used for the list selection
        self.poll()

        label3 = Label(self, text="Info").grid(row=1, column=1, sticky=(N, W, E, S))
        label31 = Label(self, text="Turn").grid(row=2, column=1, sticky=(N, W))
        label32 = Label(self, text="Buf Type").grid(row=2, column=1, sticky=W)
        label33 = Label(self, text="Turns Left").grid(row=2, column=1, sticky=(S, W))

        self.turn = '0'
        self.buff = 'None'
        self.duration = '0'
        self.label311 = Label(self, text=self.turn)   #turn value
        self.label311.grid(row=2, column=1, sticky=(N, E))
        self.label321 = Label(self, text=self.buff)   #buff value
        self.label321.grid(row=2, column=1, sticky=E)
        self.label331 = Label(self, text=self.duration) #duration value
        self.label331.grid(row=2, column=1, sticky=(S, E))

        label4 = Label(self, text="Buttons").grid(row=1, column=2, sticky=(N, W, E, S))
        button1 = Button(self, text="Add Character", command=lambda: openCharacWindow(self)).grid(
            column=2, row=2, sticky=(N, W))
        button2 = Button(self, text="Next Turn", command=self.nextButton).grid(column=2, row=2, sticky=W)
        button3 = Button(self, text="Reset", command=self.resetButton).grid(column=2, row=2, sticky=(S, W))

        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

    def ChangeCharacterInfos(self):
        self.label321.config(text=self.buff)
        self.label331.config(text=self.duration)

    def addCharacter(self, name):
        self.listCharacters.insert(END, name)

    def character_selected(self, selection):
        if len(selection) != 0:
            _, self.buff, self.duration = functions.getCharacterInfoWithIndex(selection[0])
            self.ChangeCharacterInfos()

    def poll(self):   # Fuction that listen to changes in the selection of characters
        now = self.listCharacters.curselection()
        if now != self.current:
            self.character_selected(now)
            self.current = now
        self.after(250, self.poll)

    def nextButton(self):
        functions.nextTurn()
        self.turn = str(int(self.turn)+1)
        self.label311.config(text=self.turn)
        self.character_selected(self.current)

    def resetButton(self):
        functions.CleanCharacterFile()
        self.turn = '0'
        self.buff = 'None'
        self.duration = '0'
        self.listCharacters.delete(0, 'end')
        self.label311.config(text=self.turn)
        self.label321.config(text=self.buff)
        self.label331.config(text=self.duration)


if __name__ == "__main__":
    root = Tk()
    root.title("Bufs counter")
    MainApplication(root).grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()