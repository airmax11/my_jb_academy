import math
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-t", "--type", type=str)
parser.add_argument("-p", "--principal", default=None, type=float)
parser.add_argument("-pe", "--periods", default=None, type=float)
parser.add_argument("-i", "--interest", default=None, type=float)
parser.add_argument("-pa", "--payment", default=None, type=float)
args = parser.parse_args()

p = args.principal
pe = args.periods
pa = args.payment

if args.type == "diff" and args.principal is not None \
        and args.periods is not None and args.interest is not None:
    over = 0
    i = (args.interest / 100) / 12
    for a in range(1, int(pe + 1)):
        dm = math.ceil((p / pe) + i * (p - (p * (a - 1) / pe)))
        over += dm
        print(f"Month {a}: paid out {dm}")
    print()
    print(f"Overpayment = {int(over - p)}")

elif args.type == "annuity" and args.principal is not None \
        and args.periods is not None and args.interest is not None and args.payment is None:
    i = (args.interest / 100) / 12
    a = math.ceil((p * (i * ((1 + i) ** pe)) / (((1 + i) ** pe) - 1)))
    over = (a * pe) - p
    print(f"Your annuity payment = {a}!")
    print(f"Overpayment = {int(over)}")

elif args.type == "annuity" and args.principal is None \
        and args.periods is not None and args.interest is not None and args.payment is not None:
    i = (args.interest / 100) / 12
    a = math.ceil(pa / ((i * ((1 + i) ** pe)) / (((1 + i) ** pe) - 1)))
    print(f"Your credit principal = {a}!")
    over = (pa * pe) - a
    print(f"Overpayment = {int(over)}")

elif args.type == "annuity" and args.principal is not None \
        and args.periods is None and args.interest is not None and args.payment is not None:
    i = (args.interest / 100) / 12
    res = math.log((pa / (pa - i * p)), i + 1)
    rd = math.ceil(res)
    years = rd // 12
    months = rd % 12

    if months == 0 and years > 1:
        print(f"You need {years} years to repay this credit!")
    elif months == 0 and years == 1:
        print(f"You need {years} year to repay this credit!")
    elif months > 1 and years == 0:
        print(f"You need {months} months to repay this credit!")
    elif months == 1 and years == 0:
        print(f"You need {months} month to repay this credit!")
    elif months > 1 and years > 1:
        print(f"You need {years} years and {months} months to repay this credit!")
    elif months == 1 and years == 1:
        print(f"You need {years} year and {months} month to repay this credit!")
    elif months == 1 and years > 1:
        print(f"You need {years} years and {months} month to repay this credit!")
    elif months > 1 and years == 1:
        print(f"You need {years} year and {months} months to repay this credit!")

    over = (rd * pa) - p
    print(f"Overpayment = {int(over)}")

else:
    print("Incorrect parameters.")


def user_choice():
    print('What do you want to calculate?')
    print('type "n" - for count of months,')
    print('type "a" - for annuity monthly payment,')
    print('type "p" - for credit principal:\n')
    return input()

def calc_interest(interest):
    return (interest / 100) / 12


def calc_count_month():
    credit = int(input("Enter credit principal:\n"))
    periods = int(input("Enter monthly payment:\n"))
    interest = float(input("Enter credit interest:\n"))
    c_interest = calc_interest(interest)
    res = math.log((periods / (periods - c_interest * credit)), c_interest + 1)
    rd = math.ceil(res)
    years = rd // 12
    months = rd % 12

    if months == 0 and years > 1:
        print(f"You need {years} years to repay this credit!")
    elif months == 0 and years == 1:
        print(f"You need {years} year to repay this credit!")
    elif months > 1 and years == 0:
        print(f"You need {months} months to repay this credit!")
    elif months == 1 and years == 0:
        print(f"You need {months} month to repay this credit!")
    elif months > 1 and years > 1:
        print(f"You need {years} years and {months} months to repay this credit!")
    elif months == 1 and years == 1:
        print(f"You need {years} year and {months} month to repay this credit!")
    elif months > 1 and years == 1:
        print(f"You need {years} year and {months} months to repay this credit!")


def calc_annu_mnt_payment():
    credit = int(input("Enter credit principal:\n"))
    periods = int(input("Enter count of periods:\n"))
    interest = float(input("Enter credit interest:\n"))
    c_interest = calc_interest(interest)
    a = math.ceil((credit * (c_interest * ((1 + c_interest) ** periods)) / (((1 + c_interest) ** periods) - 1)))
    print(f"Your annuity payment = {a}!")

def calc_credit_principal():
    mnt_pay = float(input("Enter monthly payment:\n"))
    periods = int(input("Enter count of periods:\n"))
    interest = float(input("Enter credit interest:\n"))

    c_interest = calc_interest(interest)
    a = round(mnt_pay / ((c_interest * ((1 + c_interest) ** periods)) / (((1 + c_interest) ** periods) - 1)))
    print(f"Your credit principal = {a}!")

def start():
    user_ch = user_choice()
    if user_ch == "n":
        calc_count_month()
    elif user_ch == "a":
        calc_annu_mnt_payment()
    elif user_ch == "p":
        calc_credit_principal()
