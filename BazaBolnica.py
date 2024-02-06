import tkinter as tk
import pyodbc
from tkinter.ttk import *
from tkinter import *

root=tk.Tk()
root.geometry("1000x800")
root.title("Bolnica-Laboratorija")

class GUI:

    def __init__(self): 
            
            self.left_frame= tk.Frame(root, width=200, height=600, bg="white")
            self.left_frame.pack(side="left", fill="y")
            self.canvas = tk.Canvas(root, width=700, height=600)
            self.canvas.pack(padx= 30, pady=40)
            button = tk.Button(self.left_frame, text="Pretrazi pacijenta", font=('Arial', 12), command=self.pretrazi)
            button.pack(padx=20, pady=10)
            button1 = tk.Button(self.left_frame, text="Obrisi pacijenta", font=('Arial', 12), command=self.obrisi)
            button1.pack(padx=20, pady=20)
            self.text=tk.Label(self.left_frame, text=f"Upisite broj knjizice pacijenta")
            self.text.pack(padx=20, pady=20)
            self.tb= tk.Entry(self.left_frame, font=('Arial'), width=20)
            self.tb.pack(padx=20, pady=25)
            button2 = tk.Button(self.left_frame, text="Unesi/izmeni pacijenta", font=('Arial', 12), command=self.Noviprozor)
            button2.pack(padx=20, pady=20)
            self.info=tk.Label(self.canvas, text=f"1-HDL, 2-LDL, 3-TRIGLICERIDI, 4-UREA")
            self.info.pack(padx=20, pady=10)
            self.listbox=tk.Listbox(self.canvas, height=4,selectmode=tk.EXTENDED)
            self.listbox.pack(padx=20, pady=20)
            self.rez=tk.Label(self.canvas, text=f"")
            self.rez.pack(padx=20, pady=30)
            
    
    def pretrazi(self):

            e_text=self.tb.get()
               
            try:
                connection_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=D:\InformacioniSistemiIBazePodataka\bolnicaLab.accdb;'
                db = pyodbc.connect(connection_string)
                
                cur=db.cursor()
                cur.execute(f'SELECT HDL,LDL,TRIGLICERIDI,UREA FROM REZULTATI WHERE BR_KNJ={e_text};')

                
                result = cur.fetchall()
                if result:
            
                    values = result[0]

                    self.listbox.delete(0, tk.END)

                    for value in values:
                        self.listbox.insert(tk.END, value)

                    self.rez.config(text="Rezultati ucitani u listu")
                else:
              
                    self.listbox.delete(0, tk.END)
                
                    self.rez.config(text="Nema rezultata")
                    
            except pyodbc.Error as e:
                print(f"Error connecting to the database: {e}")
    
    def obrisi(self):

            e_text=self.tb.get()
               
            try:
                connection_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=D:\InformacioniSistemiIBazePodataka\bolnicaLab.accdb;'
                db = pyodbc.connect(connection_string)
                
                cur=db.cursor()
                cur.execute(f'DELETE FROM REZULTATI WHERE BR_KNJ={e_text};')
                db.commit()            
                self.rez.config(text="Obrisano")
                
                

            except pyodbc.Error as e:
                print(f"Error connecting to the database: {e}")
    def Noviprozor(self):

        newWindow = Toplevel(root)
 
        newWindow.title("Unos pacijenata")
 
        newWindow.geometry("600x600")
 
        Label(newWindow, text ="Unesi rezultate pacijenta").pack()
        bk1=tk.Label(newWindow, text ="Broj knjizice").pack(pady=5)
        self.tb11= tk.Entry(newWindow, font=('Arial'), width=20)
        self.tb11.pack()
        idrez1=tk.Label(newWindow, text ="ID rezultata").pack(pady=5)
        self.tb1= tk.Entry(newWindow, font=('Arial'), width=20)
        self.tb1.pack()
        hdl1=tk.Label(newWindow, text ="HDL").pack(pady=5)
        self.tb2= tk.Entry(newWindow, font=('Arial'), width=20)
        self.tb2.pack()
        ldl1=tk.Label(newWindow, text ="LDL").pack(pady=5)
        self.tb3= tk.Entry(newWindow, font=('Arial'), width=20)
        self.tb3.pack()
        trig1=tk.Label(newWindow, text ="Trigliceridi").pack(pady=5)
        self.tb4= tk.Entry(newWindow, font=('Arial'), width=20)
        self.tb4.pack()
        urea1=tk.Label(newWindow, text ="Urea").pack(pady=5)
        self.tb5= tk.Entry(newWindow, font=('Arial'), width=20)
        self.tb5.pack()
        self.idLab1=tk.Label(newWindow, text ="ID Laboratorije").pack(pady=5)
        self.tb6= tk.Entry(newWindow, font=('Arial'), width=20)
        self.tb6.pack()
        bt=tk.Button(newWindow,font=('Arial'), text="Unesi", command=self.unesi).pack(pady=15)
        bt1=tk.Button(newWindow,font=('Arial'), text="Izmeni", command=self.izmeni).pack(pady=5)

    def unesi(self):

        bk=self.tb11.get()
        idrez=self.tb1.get()
        hdl=self.tb2.get()
        ldl=self.tb3.get()
        trig=self.tb4.get()
        urea=self.tb5.get()
        idLab=self.tb6.get()

        try:
                connection_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=D:\InformacioniSistemiIBazePodataka\bolnicaLab.accdb;'
                db = pyodbc.connect(connection_string)
                
                cur=db.cursor()
                cur.execute(f'INSERT INTO REZULTATI VALUES ({idrez},{hdl},{ldl},{trig},{urea},{idLab},{bk});')
                db.commit()

        except:
               print(f"Error connecting to the database: {e}") 

    def izmeni(self):
        bk=self.tb11.get()
        idrez=self.tb1.get()
        hdl=self.tb2.get()
        ldl=self.tb3.get()
        trig=self.tb4.get()
        urea=self.tb5.get()
        idLab=self.tb6.get()

        try:
                connection_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=D:\InformacioniSistemiIBazePodataka\bolnicaLab.accdb;'
                db = pyodbc.connect(connection_string)
                
                cur=db.cursor()
                cur.execute(f'UPDATE REZULTATI SET HDL={hdl}, LDL={ldl}, TRIGLICERIDI={trig}, UREA={urea} WHERE BR_KNJ={bk};')
                db.commit()

        except pyodbc.Error as e:
               print(f"Error connecting to the database: {e}")
gui = GUI()
root.mainloop()