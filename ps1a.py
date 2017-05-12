# pylint: disable=invalid-name

DOWN_PAYMENT_PERCENT = 0.25
RETURN_RATE = 0.04

def ask():
    """
    docstring
    """
    a_s = int(input("Enter your annual salary: "))
    per = float(input("Enter the percent of your salary to save, as a decimal:  "))
    cost_ = float(input("Enter the cost of your dream home:​ "))
    return (a_s, per, cost_)

if __name__ == "__main__":
    salary, percent, cost = ask()
    # for debugging purpose
    # salary, percent, cost, rise = (80000, 1500, 500000, 0.05)
    savings = 0
    month_needed = 0
    anual = salary/12*(percent*0.0001)
    down_payment = cost * DOWN_PAYMENT_PERCENT
    while savings <= down_payment:
        savings += (savings*RETURN_RATE/12)+anual
        month_needed += 1

    print("Needed month: {}".format(month_needed))




