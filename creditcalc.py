import argparse
import math
import sys

parser = argparse.ArgumentParser(
    description="This program helps to calculate your loan"
)
parser.add_argument("--type", help="You need specify 'diff' or 'annuity'")
parser.add_argument("--principal", help="You need specify loan principal", type=int)
parser.add_argument("--periods", help="You need specify number of periods", type=int)
parser.add_argument("--interest", help="You need loan interest", type=float)
parser.add_argument("--payment", help="You need specify monthly payment", type=int)

args = parser.parse_args()


def nominal_interest(x: float) -> float:
    return x / (12 * 100)


def get_number_monthly_payment(principal, monthly_payment, interest):
    interest = nominal_interest(interest)
    n = math.log(
        monthly_payment / (monthly_payment - interest * principal),
        1 + interest,
    )
    n = math.ceil(n)
    years = n // 12
    months = n % 12
    if years == 0:
        if months == 1:
            print(f"It will take {months} month to repay this loan!")
        else:
            print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        if years == 1:
            print(f"It will take {years} year to repay this loan!")
        else:
            print(f"It will take {years} years to repay this loan!")
    else:
        if years == 1 and months == 1:
            print(f"It will take {years} year and {months} month to repay this loan!")
        elif years == 1:
            print(f"It will take {years} year and {months} months to repay this loan!")
        elif months == 1:
            print(f"It will take {years} years and {months} month to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
    overpayment = n * monthly_payment - principal
    print(f"Overpayment = {overpayment}")


def get_monthly_payment(principal, number_monthly_payments, interest):
    interest = nominal_interest(interest)
    monthly_payment = (
        principal
        * (interest * (math.pow(1 + interest, number_monthly_payments)))
        / ((math.pow(1 + interest, number_monthly_payments)) - 1)
    )
    overpayment = number_monthly_payments * math.ceil(monthly_payment) - principal
    print(f"Your annuity payment = {math.ceil(monthly_payment)}!")
    print(f"Overpayment = {overpayment}")


def get_loan_principal(annuity_payment, number_monthly_payments, interest):
    interest = nominal_interest(interest)
    loan_principal = annuity_payment / (
        interest
        * (math.pow(1 + interest, number_monthly_payments))
        / (math.pow(1 + interest, number_monthly_payments) - 1)
    )
    overpayment = number_monthly_payments * annuity_payment - loan_principal
    print(f"Your loan principal = {math.floor(loan_principal)}!")
    print(f"Overpayment = {math.ceil(overpayment)}")


def get_diff_payment(principal, number_monthly_payments, interest):
    count = 0
    for i in range(1, number_monthly_payments + 1):
        diff_payment = math.ceil(
            principal / number_monthly_payments
            + nominal_interest(interest)
            * (principal - (principal * (i - 1)) / number_monthly_payments)
        )
        count += diff_payment
        print(f"Month {i}: payment is {diff_payment}")
    print(f"\nOverpayment = {count - principal}")


def main():
    if args.type == "diff" and len(sys.argv) == 5:
        if not args.payment and args.periods > 0 and args.interest > 0:
            get_diff_payment(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    elif args.type == "annuity" and len(sys.argv) == 5 and not args.principal:
        if args.payment > 0 and args.periods > 0 and args.interest > 0:
            get_loan_principal(args.payment, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    elif args.type == "annuity" and len(sys.argv) == 5 and not args.periods:
        if args.principal >= 0 and args.payment >= 0 and args.interest >= 0:
            get_number_monthly_payment(args.principal, args.payment, args.interest)
        else:
            print("Incorrect parameters")
    elif args.type == "annuity" and len(sys.argv) == 5 and not args.payment:
        if args.principal >= 0 and args.periods >= 0 and args.interest >= 0:
            get_monthly_payment(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")


if __name__ == "__main__":
    main()
