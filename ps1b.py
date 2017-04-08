# pylint: disable=invalid-name
RETURN_RATE = 0.04
DOWN_PAYMENT_PERCENT = 0.25



def ask():
    """
    some func explanation here )
    """
    a_s = int(input("Enter your annual salary: "))
    per = float(input("Enter the percent of your salary to save, as a decimal:  "))
    cost_ = float(input("Enter the cost of your dream home:​ "))
    rise_ = float(input("Enter the cost of your dream home:​ "))
    return (a_s, per, cost_, rise_)

if __name__ == "__main__":
    salary, percent, cost, rise = ask()

    # for debugging purpose
    # salary, percent, cost, rise = (80000, 0.1, 800000, 0.03)
    savings = 0
    month_needed = 0
    down_payment = cost * DOWN_PAYMENT_PERCENT
    while savings <= down_payment:
        savings += (savings*RETURN_RATE/12)+salary/12*percent
        month_needed += 1
        if month_needed % 6 == 0:
            salary += salary*rise


    print("Needed month: {}".format(month_needed))

