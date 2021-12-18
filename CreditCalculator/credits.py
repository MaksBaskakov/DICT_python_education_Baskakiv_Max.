import math
import argparse
define = argparse.ArgumentParser()
define.add_argument("--type")
define.add_argument("--principal", type=float)
define.add_argument("--periods", type=int)
define.add_argument("--interest", type=float)
define.add_argument("--payment", type=float)
arguments = define.parse_args()
arguments_type = arguments.type
princ = arguments.principal
payment = arguments.payment
interest = arguments.interest
periods = arguments.periods
tic = interest/1200
month = 0
v = 0


def annuity_pm(princ, payment, tic, month, v):
    pay = int(math.log(payment / (payment - tic * princ), 1 + tic))
    periods2 = pay % 12
    periods1 = (pay - periods2) / 12
    if periods2 == 0:
        print(f"It will take {str(periods1)} years")
    else:
        print(f"It will take {str(periods1)} years and {str(periods2)} months to repay this loan!")
    for y in range(pay):
        month += 1
        d = princ / pay + tic * (princ - (princ * (month - 1)) / pay)
        v += d
    overpayment = v - princ
    print(f"Overpayment = {int(overpayment)}")


def annuity_pa(princ, periods, tic, month, v):
    pay = int((princ * tic * (1 + tic) ** periods) / (((tic + 1) ** periods) - 1))
    print(f"Your monthly payment = {str(pay)}!")
    for y in range(periods):
        month += 1
        d = princ / periods + tic * (princ - (princ * (month - 1)) / periods)
        v += d
    overpayment = v - princ
    print(f"Overpayment = {int(overpayment)}")


def annuity_ppi(payment, periods, tic, month, v):
    princ = int(payment / ((tic * (1 + tic) ** periods) / (((tic + 1) ** periods) - 1)))
    print(f"Your loan principal = {str(princ)}!")
    for y in range(periods):
        month += 1
        d = princ / periods + tic * (princ - (princ * (month - 1)) / periods)
        v += d
    overpayment = v - princ
    print(f"Overpayment = {overpayment}")


def diff_func(princ, periods, tic, month, v):
    for x in range(periods):
        month += 1
        d = princ / periods + tic * (princ - (princ * (month - 1)) / periods)
        v += d
        print(f"Month {month}: payment is {int(d)}")
    overpayment = v - princ
    print(f"Overpayment = {int(overpayment)}")


if arguments.type:
    if arguments_type == "annuity":
        if arguments.principal and arguments.payment and arguments.interest:
            if arguments.principal > 0 and arguments.payment > 0 and arguments.interest > 0:
                annuity_pm(princ, payment, tic, month, v)
            else: print("Incorrect parameters")
        elif arguments.principal and arguments.periods and arguments.interest:
            if arguments.principal > 0 and arguments.periods > 0 and arguments.interest > 0:
                annuity_pa(princ, periods, tic, month, v)
            else: print("Incorrect parameters")
        elif arguments.payment and arguments.periods and arguments.interest:
            if arguments.payment > 0 and arguments.periods > 0 and arguments.interest > 0:
                annuity_ppi(payment, periods, tic, month, v)
            else: print("Incorrect parameters")
        else: print("Incorrect parameters")
    elif arguments_type == "diff":
        if arguments.principal and arguments.periods and arguments.interest:
            if arguments.principal > 0 and arguments.periods > 0 and arguments.interest > 0:
                diff_func(princ, periods, tic, month, v)
            else: print("Incorrect parameters")
        else: print("Incorrect parameters")
    else: print("Incorrect parameters")
else: print("Incorrect parameters")
