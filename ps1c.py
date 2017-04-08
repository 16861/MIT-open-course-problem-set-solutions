# pylint: disable=invalid-name

RETURN_RATE = 0.04
RISE = 0.07
DOWN_PAYMENT_PERCENT = 0.25
RETURN_RATE = 0.04
COST = 1000000
MAX_ITER_TRIES = 20

def ask():
    """
    docstring
    """
    a_s = int(input("Enter your annual salary: "))
    return a_s

def bisection(salary=300000):
    """
    docstring
    """
    tries = 0
    saving_rate = 10000
    target_amount = COST*DOWN_PAYMENT_PERCENT
    upperBound = 10000
    lowerBound = 1
    saving_rate = upperBound
    while tries < MAX_ITER_TRIES:
        month = 36
        savings = 0
        for_iter_salary = salary
        while month > 0:
            if savings >= target_amount:
                break
            savings += (savings*RETURN_RATE/12)+for_iter_salary/12*(saving_rate*0.0001)
            month -= 1
            if month % 6 == 0:
                for_iter_salary += for_iter_salary*RISE
        if savings > target_amount-100 and savings < target_amount+100:
            return (round(saving_rate*0.0001, 4), tries)
        elif savings > target_amount:
            if saving_rate == upperBound:
                saving_rate -= int(upperBound/2)
            else:
                upperBound = saving_rate
                saving_rate -= int((upperBound-lowerBound)/2)
        else:
            if saving_rate == lowerBound:
                saving_rate += int((upperBound-lowerBound)/2)
            else:
                lowerBound = saving_rate
                saving_rate += int((upperBound-lowerBound)/2)

        tries += 1
    return (None, None)

if __name__ == "__main__":
    rate, tries_ = bisection(ask())
    # for debugging purpose
    # rate, tries_ = bisection()
    if rate:
        print("Best savings rate: {}\nSteps in bisection search: {}".format(rate, tries_))
    else:
        print("It is not possible to pay the down payment in three years.")

