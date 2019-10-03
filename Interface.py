from tkinter import *
from tkinter import font, scrolledtext
import fileClassTAD as TAD
import fileClass as fc
import random

LIST_CLIENT = list()
LIST_DOCTOR = list()
AGENDA = TAD.Agenda(2019)


class TelaRoot:
    def __init__(self):
        self.root = Tk()

        self.image = PhotoImage(file="MaisSaude.png")
        self.labelTitle = Label(self.root, image=self.image, bg="Black", highlightbackground="Black")

        self.canv = Canvas(self.root, width=35, height=200, bg="Black", highlightbackground="Black")

        self.btADDcli = Button(self.canv, width=35, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                               text="ADD CLIENTE", font=font.Font(family='Fixedsys', size=15))
        self.btADDdoc = Button(self.canv, width=35, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                               text="ADD DOUTOR", font=font.Font(family='Fixedsys', size=15))
        self.btADDevn = Button(self.canv, width=35, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                               text="ADD CONSULTA", font=font.Font(family='Fixedsys', size=15))

        self.listaBt = [self.btADDcli, self.btADDdoc, self.btADDevn]
        # Canvas ADD CLIENTE

        self.canvCli = Canvas(self.root, width=100, height=80, bg="Black", highlightbackground="Black")

        self.name_cli = Label(self.canvCli, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                              text="Nome", font=font.Font(family='Fixedsys', size=15))
        self.name_cli_dd = Text(self.canvCli, width=20, height=2, bg="White", fg="Black", highlightbackground="Black"
                                , font=font.Font(family='Fixedsys', size=15))

        self.btCli = Button(self.canvCli, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                            text="Cadastrar", font=font.Font(family='Fixedsys', size=15))

        self.status_cli = Label(self.canvCli, width=20, height=2, bg="Black", highlightbackground="Black", fg="Green",
                                text="add", font=font.Font(family='Fixedsys', size=15))

        self.name_cli.pack(side=LEFT)
        self.name_cli_dd.pack(side=LEFT, anchor=CENTER)
        self.btCli.pack()

        # Canvas ADD DOCTOR

        self.canvDoc = Canvas(self.root, width=100, height=100, bg="Black", highlightbackground="Black")

        self.name_Doc = Label(self.canvDoc, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                              text="Nome", font=font.Font(family='Fixedsys', size=15))
        self.name_doc_dd = Text(self.canvDoc, width=20, height=2, bg="White", fg="Black", highlightbackground="Black"
                                , font=font.Font(family='Fixedsys', size=15))
        self.btDoc = Button(self.canvDoc, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                            text="Cadastrar", font=font.Font(family='Fixedsys', size=15))

        self.status_Doc = Label(self.canvDoc, width=20, height=2, bg="Black", highlightbackground="Black", fg="Green",
                                text="add", font=font.Font(family='Fixedsys', size=15))

        self.name_Doc.pack(side=LEFT)
        self.name_doc_dd.pack(side=LEFT)
        self.btDoc.pack(side=LEFT)

        # Canvas ADD event

        self.canvEven = Canvas(self.root, width=100, height=100, bg="Black", highlightbackground="Black")

        self.data = Label(self.canvEven, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                          text="Data", font=font.Font(family='Fixedsys', size=15))
        self.data_dd = Text(self.canvEven, width=20, height=2, bg="White", fg="Black", highlightbackground="Black",
                            font=font.Font(family='Fixedsys', size=15))
        self.doc = Label(self.canvEven, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                          text="Doutor", font=font.Font(family='Fixedsys', size=15))
        self.doc_dd = Text(self.canvEven, width=20, height=2, bg="White", fg="Black", highlightbackground="Black",
                            font=font.Font(family='Fixedsys', size=15))
        self.cli = Label(self.canvEven, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                        text="Data", font=font.Font(family='Fixedsys', size=15))
        self.cli_dd = Text(self.canvEven, width=20, height=2, bg="White", fg="Black", highlightbackground="Black",
                        font=font.Font(family='Fixedsys', size=15))

        self.btEve = Button(self.canvEven, width=20, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                            text="Cadastrar", font=font.Font(family='Fixedsys', size=15))

        self.data.pack()
        self.data_dd.pack()
        self.doc.pack()
        self.doc_dd.pack()
        self.cli.pack()
        self.cli_dd.pack()
        self.btEve.pack()

        self.listaCanvas = [[self.canvCli, 650, 400], [self.canvDoc, 650, 400], [self.canvEven, 800, 400]]

    def placeCanvas(self, canvas, x, y):
        # LIMPAR A ROOT
        for lineClearCanvas in range(len(self.listaCanvas)):
            self.listaCanvas[lineClearCanvas][0].place_forget()

        # PLACE CANVAS
        canvas.place(x=x, y=y)

    def cadEve(self):
        data = self.data_dd.get("1.0", "end-1c")
        doc = None
        for med in LIST_DOCTOR:
            if med.name == self.doc_dd.get("1.0", "end-1c"): doc = med
        cli = None
        for pac in LIST_CLIENT:
            if pac.name == self.cli_dd.get("1.0", "end-1c"): cli = pac

        event = fc.Event(random.randint(0, 100),doc, cli, data)

        self.data.pack_forget()
        self.data_dd.pack_forget()
        self.doc.pack_forget()
        self.doc_dd.pack_forget()
        self.cli.pack_forget()
        self.cli_dd.pack_forget()

        self.status_cli.pack()
        self.status_cli["text"] = "Evento Cadastrado"

    def cadCli(self):
        text = self.name_cli_dd.get("1.0", "end-1c")
        print(text)
        cli = fc.Client(random.randint(0, 100), text)
        LIST_CLIENT.append(cli)
        self.name_cli_dd.delete('1.0', "end-1c")

        # Limpar Canvas
        self.name_cli_dd.pack_forget()
        self.name_cli.pack_forget()
        self.btCli.pack_forget()

        self.status_cli.pack()
        self.status_cli["text"] = "Cliente Cadastrado"

    def cadDoc(self):
        text = self.name_doc_dd.get("1.0", "end-1c")
        print(text)
        doc = fc.Client(random.randint(0, 100), text)
        LIST_DOCTOR.append(doc)
        self.name_doc_dd.delete('1.0', "end-1c")

        # Limpar Canvas
        self.name_doc_dd.pack_forget()
        self.name_Doc.pack_forget()
        self.btDoc.pack_forget()

        self.status_Doc.pack()
        self.status_Doc["text"] = "Doutor Cadastrado"

    def construto(self):
        self.root.attributes('-fullscreen', True)
        self.root.focus_force()
        self.root.title("Clinica")
        self.root["bg"] = "Black"

        self.labelTitle.pack()

        for index in range(len(self.listaCanvas)):
            canvas, X, Y = self.listaCanvas[index]
            self.listaBt[index]["command"] = lambda c=canvas, x=X, y=Y: self.placeCanvas(c, x, y)

        self.btADDcli.pack()
        self.btADDdoc.pack()
        self.btADDevn.pack()
        self.canv.pack(side=LEFT)

        self.btCli["command"] = self.cadCli
        self.btDoc["command"] = self.cadDoc
        self.btEve["command"] = self.cadEve
        self.root.mainloop()


TelaRoot().construto()
