import random as rnd
import tkinter as Tk 
import sqlite3 as vt
def degistir(numara):
	global tiklama
	global ilk
	tiklama += 1 
	if tiklama == 2:
		ikinci = numara
		ilksat, ilksut, ikincisat, ikincisut = ilk // sut, ilk % sut, ikinci // sut, ikinci % sut
		if (ilksat - ikincisat)**2 + (ilksut -ikincisut)**2 <= 2:
			dugmeler[ilk]["text"], dugmeler[ikinci]["text"] = dugmeler[ikinci]["text"], dugmeler[ilk]["text"]
			dugmeler[ilk]["bg"], dugmeler[ikinci]["bg"] = dugmeler[ikinci]["bg"], dugmeler[ilk]["bg"]
			cumle = "update dugmeler set dgmmetni = '%s', dgmrenk = '%s' where dgmno = %d"%(dugmeler[ilk]["text"],dugmeler[ilk]["bg"],ilk)
			sql.execute(cumle)
			cumle = "update dugmeler set dgmmetni = '%s', dgmrenk = '%s' where dgmno = %d"%(dugmeler[ikinci]["text"],dugmeler[ikinci]["bg"],ikinci)
			sql.execute(cumle)
			bag.commit()
		tiklama = 0
	else:
		ilk = numara


def birhamlegeri(event):

	pass

def birhamleileri(event):

	pass

def girilensayikadarhamlegeri(event):

	pass

def girilensayikadarhamleileri(event):

	pass




bag = vt.connect("veriler.db")
sql = bag.cursor()
cumle = "create table if not exists dugmeler (dgmno int, dgmmetni text, dgmrenk text)"
sql.execute(cumle)

cumle = "delete from dugmeler"
sql.execute(cumle)
bag.commit()

tiklama = 0
renk = ["Yellow", "Red", "Blue", "Green", "Orange", "Brown", "Magenta", "Tomato", "Gray"]

 
sat, sut = 8,8
form = Tk.Tk()
a,b,c,d = 400, 500, (form.winfo_screenwidth()-600)//2, (form.winfo_screenheight()-400)//2
form.title("Puzzle")
form.geometry("%sx%s+%s+%s"%(a,b,c,d))
dugmeler = []
secim = len(renk)-1
yuk, gen = 45, 45
liste = rnd.sample(range(1,sat*sut+1), sat*sut)

panel = Tk.Frame()
panel.place(x=130, y=50)

ahamlegeri = Tk.Button(text="Girilen Sayı Kadar Hamle Geri <--", command=form.quit)
ahamlegeri.place(x=100, y=10, height=30, width=200)
hamlegeri = Tk.Button(text="Bir Hamle Geri <--", command=form.quit)
hamlegeri.place(x=10, y=50, height=30, width=100)
ahamleileri = Tk.Button(text="Girilen Sayı Kadar Hamle İleri -->", command=form.quit)
ahamleileri.place(x=100, y=90, height=30, width=200)
hamleileri = Tk.Button(text="Bir Hamle İleri -->", command=form.quit)
hamleileri.place(x=280, y=50, height=30, width=100)

girilen = Tk.Entry(panel)
girilen.grid(row=1, column = 1)
girilen.config(bg="yellow")

for row in range(sat):
	for column in range(sut):
		dugmeler.append(Tk.Button(text = str(liste[row*sut+column]), bg = renk[rnd.randint(0,secim)], command = lambda x = row*sut+column : degistir(x) ))
		dugmeler[row*sut+column].place(x = column*gen+20, y=yuk*row+20+100,height = yuk, width = gen)
		cumle = "insert into dugmeler values (%d,'%s','%s')"%(row*sut+column,str(liste[row*sut+column]),dugmeler[row*sut+column]["bg"])
		sql.execute(cumle)
bag.commit()
Tk.mainloop()