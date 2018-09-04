# Hands on 1
# Haoyu Shi
# 9/2/2018


while(True):
    print ('Enter the amount for withdrawal: ')
    amount = input()
    if amount.isdigit():
        bills = [100, 50, 20, 10, 5]
        amount = int(amount)
        if amount % 5 != 0:
            print("The amount cannot be withdrawn.")
            continue

        number_of_bills = {}
        number = []
        money = amount

        a = money // bills[0]
        money = money - a * bills[0]
        b = money // bills[1]
        money = money - b * bills[1]
        c = money // bills[2]
        money = money - c * bills[2]
        d = money // bills[3]
        money = money - d * bills[3]
        e = money // bills[4]

        output = {"$100": a, "$50": b, "$20": c, "$10": d, "$5":e}
        print('Please collect your bills as follows:')
        for key in output.keys():
            if output[key]:
                print(key + ':' + '\t', output[key])
    else:
        print('please input correct amount type.(number)')
