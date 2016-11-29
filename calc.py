"""
Sales within the US
    2.9% + $0.30 per transaction Discounted
rate for eligible nonprofits
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
