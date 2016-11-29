"""
Sales within the US
    2.9% + $0.30 per transaction
Discountedroot = tk.Tk()
root.resizable(0,0)
root.geometry('400x180+500+500')
dFont=tkFont.Font(family="Arial", size=10)

# label / entry pair
l1 = tk.Label(root, text="RTMPin:")
e1 = tk.Entry(root,width=50)

# put in first row
l1.grid(row=0, column=0, sticky="e")
e1.grid(row=0, column=1, sticky="news")

# label / entry pair
l2 = tk.Label(root, text="RTMPout:")
e2 = tk.Entry(root)

# put in first row
l2.grid(row=1, column=0, sticky="e")
e2.grid(row=1, column=1, sticky="news")

# label / entry pair
l3 = tk.Label(root, text="Log:")
e3 = tk.Text(master=root, width=50, height=5, font=dFont)

# put in first row
l3.grid(row=3, column=0, sticky="e")
e3.grid(row=3, column=1, sticky="news")

# label / entry pair
l4 = tk.Label(root)
e4 = tk.Button(root, text="start", command=cbc("1", e3))
e4b = tk.Button(root, text="stop", command=cbcstop("1", e3))

# put in first row
l4.grid(row=2, column=0, sticky="e")
e4.grid(row=4, column=0, sticky="e")
e4b.grid(row=4, column=2, sticky="w")

# label / entry pair
l5 = tk.Label(root)
e5 = tk.Button(root, text='Exit', command=root.destroy)

# put in first row
l5.grid(row=4, column=0, sticky="e")
e5.grid(row=4, column=1, sticky="news")

# column 0 - do not expand
root.columnconfigure(0, weight=0)

# column 1 - expand
root.columnconfigure(1, weight=1)

root.mainloop() rate for eligible nonprofits
    2.2% + $0.30 per transaction
International sales
    3.9% transaction fee plus a fixed fee based on currency received
PayPal HereTM card reader
    2.7% when you swipe a card or 3.5% plus $0.15 for manually entered transactions


* https://www.paypal.com/us/webapps/mpp/paypal-fees
* Fixed fee $0.30 per sale
* Compatible with py2&py3

"""

from sys import version_info

if version_info.major >= 3:
    raw_input = input


def panel():
    return ("""
    1) Sales within the US
    2) Discounted rate for eligible nonprofits
    3) International sales
    4) PayPal HereTM card reader - swipe
    5) PayPal HereTM card reader - manual entry
    """)


SaleswithintheUS = lambda x: ((x * 0.029) + 0.30) + x
Discountedrateforeligiblenonprofits = lambda x: ((x * 0.022) + 0.30) + x
Internationalsales = lambda x: ((x * 0.039) + 0.30) + x
PayPalHereTMcardreaderSWIPE = lambda x: ((x * 0.027)) + x
PayPalHereTMcardreaderMANUAL = lambda x: ((x * 0.035) + 0.15) + x
calculate = ""

while True:
    try:
        print(panel())
        option = raw_input("Select option : ")
        if option == "1":
            calculate = SaleswithintheUS
        elif option == "2":
            calculate = Discountedrateforeligiblenonprofits
        elif option == "3":
            calculate = Internationalsales
        elif option == "4":
            calculate = PayPalHereTMcardreaderSWIPE
        elif option == "5":
            calculate = PayPalHereTMcardreaderMANUAL
        else:
            print("\nThis option is not exists, please try again.")
            continue

        x = raw_input("Please enter amount: ")
        if len(x) != len([_ for _ in x if x.isdigit()]):
            print("You should enter integer")
        else:
            total = calculate(int(x))
            fee = total - int(x)
            print("\nTotal amount : {0} Fee : {1}".format(total, fee))
    except KeyboardInterrupt:
        print ("CTRL+C active leaving ..")
        break
