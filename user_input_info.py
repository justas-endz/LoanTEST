from tabulate import tabulate


class Loan:
    def __init__(self):
        self.total_interest = 0
        self.pay_per_month = 0
        self.total_pay = 0
        self.monthly_interest = None
        self.payment_month = None
        self.loan_sum = None
        self.loan_interest = None
        self.loan_term = None

    def inputInfo(self):
        self.loan_sum = int(input("Enter loan sum: "))
        self.loan_interest = int(input("Enter loan interest: "))
        self.loan_term = int(input("Enter load term (months): "))

    def printLoanInfo(self):
        print(f"""
        Loan: {self.loan_sum}.
        Interest: {self.loan_interest}.
        Term: {self.loan_term} months.
        Total payable sum: {self.total_pay}
        Total payable interest: {self.total_interest}
    """)

    def loanTable(self):
        self.payment_month = self.loan_sum / self.loan_term
        for i in range(self.loan_term):
            self.monthly_interest = self.loan_sum * (self.loan_interest / 100) / 12
            self.loan_sum -= self.payment_month
            self.pay_per_month = self.payment_month + self.monthly_interest
            self.total_pay += self.pay_per_month
            self.total_interest += self.monthly_interest
            table = [['Month no.', i + 1],
                     ['Repayment', "{0:.2f}".format(self.payment_month)],
                     ['Remainder', "{0:.2f}".format(self.loan_sum)],
                     ['Interest EUR', "{0:.2f}".format(self.monthly_interest)],
                     ['Total Sum', "{0:.2f}".format(self.total_pay)],
                     ['Total interest EUR', "{0:.2f}".format(self.total_interest)]]
            print(tabulate(table, tablefmt='orgtbl'))
