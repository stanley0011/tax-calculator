def tax3(income):
    net = 0
    if income <= 12570:
        net = income
    if 12570 < income <= 50270:  # if income over basic rate
        net += 12570  # tax free
        income -= 12570
        net += (income*0.8)
    if 50270 < income <= 150000:  # if remaining income over higher rate
        net += 12570  # tax free
        income -= 12570
        net += (37700*0.8)
        income -= 37700
        net += (income*0.6)  # taxes the remaining money
    if income > 150000:
        net += 12570  # tax free
        income -= 12570
        net += (37700*0.8)
        income -= 37700
        net += (99730*0.6)
        income -= 99730
        net += (income*0.55)

    print(net)


if __name__ == "__main__":
    gross = int(input("Enter gross income: "))
    tax3(gross)
