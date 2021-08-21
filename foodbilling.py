from tkinter import *
import tkinter.ttk as ttk
import time
import datetime
import random

root = Tk()
root.geometry("1350x700+0+0")
root.title("Food Billing System")
root.configure(background='#966F33')

Tops = Frame(root, bg='black', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 60, 'bold'), text='Food Billing System', bd=21, bg='black',
                 fg='cornsilk', justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root, bg='#966F33', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F, bg='#966F33', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F = Frame(ReceiptCal_F, bg='#966F33', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F = Frame(ReceiptCal_F, bg='#966F33', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='#966F33', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F = Frame(MenuFrame, bg='#966F33', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(MenuFrame, bg='#966F33', bd=4)
Drinks_F.pack(side=TOP)


Drinks_F = Frame(MenuFrame, bg='#966F33', bd=4, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F = Frame(MenuFrame, bg='#966F33', bd=4, relief=RIDGE)
Food_F.pack(side=RIGHT)
###################################################variables################################################

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Sprite = StringVar()
E_Pepsi = StringVar()
E_DietCoke = StringVar()
E_Mojito = StringVar()
E_Cappuccino = StringVar()
E_Fanta = StringVar()
E_CocaCola = StringVar()
E_ColdCoffee = StringVar()

E_HotDog = StringVar()
E_VegBurger = StringVar()
E_Pasta = StringVar()
E_HamBurger = StringVar()
E_Sandwich = StringVar()
E_Fires = StringVar()
E_Spagetti = StringVar()
E_Fazitas = StringVar()

E_Sprite.set("0")
E_Pepsi.set("0")
E_DietCoke.set("0")
E_Mojito.set("0")
E_Cappuccino.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_ColdCoffee.set("0")

E_HotDog.set("0")
E_VegBurger.set("0")
E_Pasta.set("0")
E_HamBurger.set("0")
E_Sandwich.set("0")
E_Fires.set("0")
E_Spagetti.set("0")
E_Fazitas.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################


def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_DietCoke.set("0")
    E_Mojito.set("0")
    E_Cappuccino.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_ColdCoffee.set("0")

    E_HotDog.set("0")
    E_VegBurger.set("0")
    E_Pasta.set("0")
    E_HamBurger.set("0")
    E_Sandwich.set("0")
    E_Fires.set("0")
    E_Spagetti.set("0")
    E_Fazitas.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtSprite.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtDietCoke.configure(state=DISABLED)
    txtMojito.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtHotDog.configure(state=DISABLED)
    txtVegBurger.configure(state=DISABLED)
    txtPasta.configure(state=DISABLED)
    txtHamBurger.configure(state=DISABLED)
    txtSandwich.configure(state=DISABLED)
    txtFires.configure(state=DISABLED)
    txtSpagetti.configure(state=DISABLED)
    txtFazitas.configure(state=DISABLED)


def CostofItem():
    Item1 = float(E_Sprite.get())
    Item2 = float(E_Pepsi.get())
    Item3 = float(E_DietCoke.get())
    Item4 = float(E_Mojito.get())
    Item5 = float(E_Cappuccino.get())
    Item6 = float(E_Fanta.get())
    Item7 = float(E_CocaCola.get())
    Item8 = float(E_ColdCoffee.get())

    Item9 = float(E_HotDog.get())
    Item10 = float(E_VegBurger.get())
    Item11 = float(E_Pasta.get())
    Item12 = float(E_HamBurger.get())
    Item13 = float(E_Sandwich.get())
    Item14 = float(E_Fires.get())
    Item15 = float(E_Spagetti.get())
    Item16 = float(E_Fazitas.get())

    PriceofFood = (Item1 * 65) + (Item2 * 75) + (Item3 * 99) + (Item4 * 130) + \
        (Item5 * 180) + (Item6 * 75) + (Item7 * 75) + (Item8 * 89) + (Item9 * 260) + (Item10 * 175) + (Item11 * 255) + (Item12 * 480) + \
        (Item13 * 240) + (Item14 * 110) + (Item15 * 340) + (Item16 * 213)

    FoodPrice = "Rs", str('%.2f' % (PriceofFood))
    CostofFood.set(FoodPrice)
    SC = "Rs", str('%.2f' % (1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs", str('%.2f' % (PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs", str('%.2f' % ((PriceofFood + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT = ((PriceofFood + 1.59) * 0.15)
    TC = "Rs", str('%.2f' % (PriceofFood + 1.59 + TT))
    TotalCost.set(TC)


def chkSprite():
    if(var1.get() == 1):
        txtSprite.configure(state=NORMAL)
        txtSprite.focus()
        txtSprite.delete('0', END)
        E_Sprite.set("")
    elif(var1.get() == 0):
        txtSprite.configure(state=DISABLED)
        E_Sprite.set("0")


def chkPepsi():
    if(var2.get() == 1):
        txtPepsi.configure(state=NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0', END)
        E_Pepsi.set("")
    elif(var2.get() == 0):
        txtPepsi.configure(state=DISABLED)
        E_Pepsi.set("0")


def chk_DietCoke():
    if(var3.get() == 1):
        txtDietCoke.configure(state=NORMAL)
        txtDietCoke.delete('0', END)
        txtDietCoke.focus()
    elif(var3.get() == 0):
        txtDietCoke.configure(state=DISABLED)
        E_DietCoke.set("0")


def chk_Mojito():
    if(var4.get() == 1):
        txtMojito.configure(state=NORMAL)
        txtMojito.delete('0', END)
        txtMojito.focus()
    elif(var4.get() == 0):
        txtMojito.configure(state=DISABLED)
        E_Mojito.set("0")


def chk_Cappuccino():
    if(var5.get() == 1):
        txtCappuccino.configure(state=NORMAL)
        txtCappuccino.delete('0', END)
        txtCappuccino.focus()
    elif(var5.get() == 0):
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")


def chk_Fanta():
    if(var6.get() == 1):
        txtFanta.configure(state=NORMAL)
        txtFanta.delete('0', END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state=DISABLED)
        E_Fanta.set("0")


def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state=NORMAL)
        txtCocaCola.delete('0', END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state=DISABLED)
        E_CocaCola.set("0")


def chk_ColdCoffee():
    if(var8.get() == 1):
        txtColdCoffee.configure(state=NORMAL)
        txtColdCoffee.delete('0', END)
        txtColdCoffee.focus()
    elif(var8.get() == 0):
        txtColdCoffee.configure(state=DISABLED)
        E_ColdCoffee.set("0")


def chk_HotDog():
    if(var9.get() == 1):
        txtHotDog.configure(state=NORMAL)
        txtHotDog.delete('0', END)
        txtHotDog.focus()
    elif(var9.get() == 0):
        txtHotDog.configure(state=DISABLED)
        E_HotDog.set("0")


def chk_VegBurger():
    if(var10.get() == 1):
        txtVegBurger.configure(state=NORMAL)
        txtVegBurger.delete('0', END)
        txtVegBurger.focus()
    elif(var10.get() == 0):
        txtVegBurger.configure(state=DISABLED)
        E_VegBurger.set("0")


def chk_Pasta():
    if(var11.get() == 1):
        txtPasta.configure(state=NORMAL)
        txtPasta.delete('0', END)
        txtPasta.focus()
    elif(var11.get() == 0):
        txtPasta.configure(state=DISABLED)
        E_Pasta.set("0")


def chk_HamBurger():
    if(var12.get() == 1):
        txtHamBurger.configure(state=NORMAL)
        txtHamBurger.delete('0', END)
        txtHamBurger.focus()
    elif(var12.get() == 0):
        txtHamBurger.configure(state=DISABLED)
        E_HamBurger.set("0")


def chk_Sandwich():
    if(var13.get() == 1):
        txtSandwich.configure(state=NORMAL)
        txtSandwich.delete('0', END)
        txtSandwich.focus()
    elif(var13.get() == 0):
        txtSandwich.configure(state=DISABLED)
        E_Sandwich.set("0")


def chk_Fires():
    if(var14.get() == 1):
        txtFires.configure(state=NORMAL)
        txtFires.delete('0', END)
        txtFires.focus()
    elif(var14.get() == 0):
        txtFires.configure(state=DISABLED)
        E_Fires.set("0")


def chk_Spagetti():
    if(var15.get() == 1):
        txtSpagetti.configure(state=NORMAL)
        txtSpagetti.delete('0', END)
        txtSpagetti.focus()
    elif(var15.get() == 0):
        txtSpagetti.configure(state=DISABLED)
        E_Spagetti.set("0")


def chk_Fazitas():
    if(var16.get() == 1):
        txtFazitas.configure(state=NORMAL)
        txtFazitas.delete('0', END)
        txtFazitas.focus()
    elif(var16.get() == 0):
        txtFazitas.configure(state=DISABLED)
        E_Fazitas.set("0")


def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' +
                      Receipt_Ref.get() + '\t' + DateofOrder.get() + '\n')
    txtReceipt.insert(END, 'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END, 'Sprite:\t\t\t\t\t' + E_Sprite.get() + '\n')
    txtReceipt.insert(END, 'Pepsi:\t\t\t\t\t' + E_Pepsi.get()+'\n')
    txtReceipt.insert(END, 'DietCoke:\t\t\t\t\t' + E_DietCoke.get()+'\n')
    txtReceipt.insert(END, 'Mojito:\t\t\t\t\t' + E_Mojito.get()+'\n')
    txtReceipt.insert(END, 'Cappuccino:\t\t\t\t\t' + E_Cappuccino.get()+'\n')
    txtReceipt.insert(END, 'Fanta:\t\t\t\t\t' + E_Fanta.get()+'\n')
    txtReceipt.insert(END, 'CocaCola:\t\t\t\t\t' + E_CocaCola.get()+'\n')
    txtReceipt.insert(END, 'ColdCoffee:\t\t\t\t\t' + E_ColdCoffee.get()+'\n')
    txtReceipt.insert(END, 'HotDog:\t\t\t\t\t' + E_HotDog.get()+'\n')
    txtReceipt.insert(END, 'VegBurger:\t\t\t\t\t' + E_VegBurger.get()+'\n')
    txtReceipt.insert(END, 'Pasta:\t\t\t\t\t' + E_Pasta.get()+'\n')
    txtReceipt.insert(END, 'HamBurger:\t\t\t\t\t' + E_HamBurger.get()+'\n')
    txtReceipt.insert(END, 'Sandwich:\t\t\t\t\t' + E_Sandwich.get()+'\n')
    txtReceipt.insert(END, 'Fires:\t\t\t\t\t' + E_Fires.get()+'\n')
    txtReceipt.insert(END, 'Spagetti:\t\t\t\t\t' + E_Spagetti.get()+'\n')
    txtReceipt.insert(END, 'Fazitas:\t\t\t\t\t' + E_Fazitas.get()+'\n')
    # txtReceipt.insert(END, 'Cost of Drinks:\t\t\t\t\t' +
    #                   CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Cost of Foods:\t\t\t\t' + CostofFood.get() +
                      '\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get() +
                      '\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


#########################################Drinks####################################################################
Sprite = Checkbutton(Drinks_F, text='Sprite', variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                     bg='#966F33', command=chkSprite).grid(row=0, sticky=W)
Pepsi = Checkbutton(Drinks_F, text='Pepsi', variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg='#966F33', command=chkPepsi).grid(row=1, sticky=W)
DietCoke = Checkbutton(Drinks_F, text='DietCoke', variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                       bg='#966F33', command=chk_DietCoke).grid(row=2, sticky=W)
Mojito = Checkbutton(Drinks_F, text='Mojito', variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                     bg='#966F33', command=chk_Mojito).grid(row=3, sticky=W)
Cappuccino = Checkbutton(Drinks_F, text='Cappuccino', variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                         bg='#966F33', command=chk_Cappuccino).grid(row=4, sticky=W)
Fanta = Checkbutton(Drinks_F, text='Fanta', variable=var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg='#966F33', command=chk_Fanta).grid(row=5, sticky=W)
CocaCola = Checkbutton(Drinks_F, text='CocaCola', variable=var7, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                       bg='#966F33', command=chk_CocaCola).grid(row=6, sticky=W)
ColdCoffee = Checkbutton(Drinks_F, text='ColdCoffee', variable=var8, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                         bg='#966F33', command=chk_ColdCoffee).grid(row=7, sticky=W)
##############################################Drink Entry###############################################################

txtSprite = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                  width=6, justify=LEFT, state=DISABLED, textvariable=E_Sprite)
txtSprite.grid(row=0, column=1)

txtPepsi = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                 width=6, justify=LEFT, state=DISABLED, textvariable=E_Pepsi)
txtPepsi.grid(row=1, column=1)

txtDietCoke = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                    width=6, justify=LEFT, state=DISABLED, textvariable=E_DietCoke)
txtDietCoke.grid(row=2, column=1)

txtMojito = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                  width=6, justify=LEFT, state=DISABLED, textvariable=E_Mojito)
txtMojito.grid(row=3, column=1)

txtCappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                      width=6, justify=LEFT, state=DISABLED, textvariable=E_Cappuccino)
txtCappuccino.grid(row=4, column=1)

txtFanta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                 width=6, justify=LEFT, state=DISABLED, textvariable=E_Fanta)
txtFanta.grid(row=5, column=1)

txtCocaCola = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                    width=6, justify=LEFT, state=DISABLED, textvariable=E_CocaCola)
txtCocaCola.grid(row=6, column=1)

txtColdCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8,
                      width=6, justify=LEFT, state=DISABLED, textvariable=E_ColdCoffee)
txtColdCoffee.grid(row=7, column=1)
#############################################Foods######################################################################

HotDog = Checkbutton(Food_F, text="HotDog\t\t\t ", variable=var9, onvalue=1, offvalue=0,
                     font=('arial', 16, 'bold'), bg='#966F33', command=chk_HotDog).grid(row=0, sticky=W)
VegBurger = Checkbutton(Food_F, text="VegBurger", variable=var10, onvalue=1, offvalue=0,
                        font=('arial', 16, 'bold'), bg='#966F33', command=chk_VegBurger).grid(row=1, sticky=W)
Pasta = Checkbutton(Food_F, text="Pasta ", variable=var11, onvalue=1, offvalue=0,
                    font=('arial', 16, 'bold'), bg='#966F33', command=chk_Pasta).grid(row=2, sticky=W)
HamBurger = Checkbutton(Food_F, text="Rice Plate ", variable=var12, onvalue=1, offvalue=0,
                        font=('arial', 16, 'bold'), bg='#966F33', command=chk_HamBurger).grid(row=3, sticky=W)
Sandwich = Checkbutton(Food_F, text="Sandwich ", variable=var13, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'), bg='#966F33', command=chk_Sandwich).grid(row=4, sticky=W)
Fires = Checkbutton(Food_F, text="Fires ", variable=var14, onvalue=1, offvalue=0,
                    font=('arial', 16, 'bold'), bg='#966F33', command=chk_Fires).grid(row=5, sticky=W)
Spagetti = Checkbutton(Food_F, text="Spagetti ", variable=var15, onvalue=1, offvalue=0,
                       font=('arial', 16, 'bold'), bg='#966F33', command=chk_Spagetti).grid(row=6, sticky=W)
Fazitas = Checkbutton(Food_F, text="Fazitas ", variable=var16, onvalue=1, offvalue=0,
                      font=('arial', 16, 'bold'), bg='#966F33', command=chk_Fazitas).grid(row=7, sticky=W)
################################################Entry Box For Cake##########################################################
txtHotDog = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                  textvariable=E_HotDog)
txtHotDog.grid(row=0, column=1)

txtVegBurger = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                     textvariable=E_VegBurger)
txtVegBurger.grid(row=1, column=1)

txtPasta = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                 textvariable=E_Pasta)
txtPasta.grid(row=2, column=1)

txtHamBurger = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                     textvariable=E_HamBurger)
txtHamBurger.grid(row=3, column=1)

txtSandwich = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                    textvariable=E_Sandwich)
txtSandwich.grid(row=4, column=1)

txtFires = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                 textvariable=E_Fires)
txtFires.grid(row=5, column=1)

txtSpagetti = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                    textvariable=E_Spagetti)
txtSpagetti.grid(row=6, column=1)

txtFazitas = Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                   textvariable=E_Fazitas)
txtFazitas.grid(row=7, column=1)
###########################################ToTal Cost################################################################################

lblCostofFood = Label(Cost_F, font=('arial', 14, 'bold'), text='Cost of Foods  ', bg='#966F33',
                      fg='black', justify=CENTER)
lblCostofFood.grid(row=0, column=0, sticky=W)
txtCostofFood = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                      insertwidth=2, justify=RIGHT, textvariable=CostofFood)
txtCostofFood.grid(row=0, column=1)

lblServiceCharge = Label(Cost_F, font=('arial', 14, 'bold'), text='Service Charge', bg='#966F33',
                         fg='black', justify=CENTER)
lblServiceCharge.grid(row=1, column=0, sticky=W)
txtServiceCharge = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                         insertwidth=2, justify=RIGHT, textvariable=ServiceCharge)
txtServiceCharge.grid(row=1, column=1)
###########################################################Payment information###################################################

lblPaidTax = Label(Cost_F, font=('arial', 14, 'bold'), text='\tPaid Tax', bg='#966F33', bd=7,
                   fg='black', justify=CENTER)
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                   insertwidth=2, justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F, font=('arial', 14, 'bold'), text='\tSub Total', bg='#966F33', bd=7,
                    fg='black', justify=CENTER)
lblSubTotal.grid(row=1, column=2, sticky=W)
txtSubTotal = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                    insertwidth=2, justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F, font=('arial', 14, 'bold'), text='\tTotal', bg='#966F33', bd=7,
                     fg='black', justify=CENTER)
lblTotalCost.grid(row=2, column=2, sticky=W)
txtTotalCost = Entry(Cost_F, bg='white', bd=7, font=('arial', 14, 'bold'),
                     insertwidth=2, justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)

#############################################RECEIPT###############################################################################
txtReceipt = Text(Receipt_F, width=46, height=12, bg='white',
                  bd=4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)


expression = ""


def openCalc():

    def press(num):
        global expression

        expression = expression + str(num)
        equation.set(expression)

    def equalpress():
        try:
            global expression
            total = str(eval(expression))
            equation.set(total)
            expression = ""
        except:
            equation.set(" error ")
            expression = ""

    def clear():
        global expression
        expression = ""
        equation.set("")

    cal_win = Toplevel(root)
    cal_win.title("Calculator")
    equation = StringVar()
    entry_box = Entry(cal_win, textvariable=equation)
    entry_box.grid(columnspan=4, ipady=5, ipadx=80, pady=10)
    button1 = ttk.Button(cal_win, text=' 1 ',
                         command=lambda: press(1))
    button1.grid(row=2, column=0)
    button2 = ttk.Button(cal_win, text=' 2 ',
                         command=lambda: press(2))
    button2.grid(row=2, column=1)
    button3 = ttk.Button(cal_win, text=' 3 ',
                         command=lambda: press(3))
    button3.grid(row=2, column=2)
    button4 = ttk.Button(cal_win, text=' 4 ',
                         command=lambda: press(4))
    button4.grid(row=3, column=0)
    button5 = ttk.Button(cal_win, text=' 5 ',
                         command=lambda: press(5),)
    button5.grid(row=3, column=1)
    button6 = ttk.Button(cal_win, text=' 6 ',
                         command=lambda: press(6),)
    button6.grid(row=3, column=2)
    button7 = ttk.Button(cal_win, text=' 7 ',
                         command=lambda: press(7),)
    button7.grid(row=4, column=0)
    button8 = ttk.Button(cal_win, text=' 8 ',
                         command=lambda: press(8),)
    button8.grid(row=4, column=1)
    button9 = ttk.Button(cal_win, text=' 9 ',
                         command=lambda: press(9),)
    button9.grid(row=4, column=2)
    button0 = ttk.Button(cal_win, text=' 0 ',
                         command=lambda: press(0),)
    button0.grid(row=5, column=0)
    plus = ttk.Button(cal_win, text=' + ',
                      command=lambda: press("+"),)
    plus.grid(row=2, column=3)
    minus = ttk.Button(cal_win, text=' - ',
                       command=lambda: press("-"))
    minus.grid(row=3, column=3)
    multiply = ttk.Button(cal_win, text=' * ',
                          command=lambda: press("*"))
    multiply.grid(row=4, column=3)
    divide = ttk.Button(cal_win, text=' / ',
                        command=lambda: press("/"))
    divide.grid(row=5, column=3)
    equal = Button(cal_win, text=' = ', width=42, bg='grey', highlightthickness=0, bd=0,
                   command=equalpress)
    equal.grid(row=6, column=0, columnspan=4, pady=1)
    clear = ttk.Button(cal_win, text='Clear',
                       command=clear)
    clear.grid(row=5, column=1)
    decimal = ttk.Button(cal_win, text='.',
                         command=lambda: press('.'))
    decimal.grid(row=5, column=2)
    cal_win.mainloop()


###########################################BUTTONS################################################################################
btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Total',
                  bg='#966F33', command=CostofItem).grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Receipt',
                    bg='#966F33', command=Receipt).grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Reset',
                  bg='#966F33', command=Reset).grid(row=0, column=2)
btnCalc = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text='Calc',
                 bg='#966F33', command=openCalc).grid(row=0, column=3)

###################################Calculator Display################################################################################


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_Input.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


root.mainloop()
