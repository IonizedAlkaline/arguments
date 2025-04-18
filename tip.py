def calc(bill, percent):
    tip = (percent / 100) * bill
    total_bill = bill + tip
    print("total amount payable is:", total_bill)


calc(1000, 5)
