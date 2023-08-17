class Category:

    def __init__(self, category):
        self.category = category  # like "food", "clothing", "entertainment" etc.
        self.ledger = []  # instance variable
        self.operations = []  # auxiliar list which keep the balance of a current category

    """
    *check_funds*
    returns "False" if the amount is greater than the balance of the budget category
    otherwise it returns "True"
    """
    def check_funds(self, amount):
        if float(amount) <= sum(self.operations):
            return True
        else:
            return False

    """
    *deposit* (einzahlen)
    append an object to the ledger list
    in the form of "{"amount": amount, "description": description}".
    """
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.operations.append(float(amount))

    """
    *withdraw* (abheben)
    similar to the "deposit" method, but the amount passed in should be stored in the ledger
    as a negative number. If there are not enough funds, nothing should be added to the ledger.
    This method should return "True" if the withdrawal took place, and "False" otherwise.
    """
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            self.operations.append(-float(amount))
            return True
        else:
            return False

    """
    *get_balance*
    returns the current balance of the budget category based on the
    deposits and withdrawals that have occurred
    """
    def get_balance(self):
        current_balance = sum(self.operations)
        return current_balance

    """
    *transfer*
    accepts an amount and another budget category as arguments.
    Add a withdrawal with the amount and the description
    """
    def transfer(self, amount, d):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {d.category}")
            d.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    """
    *__str__*
    represents the class objects as a string and should be defined in a way that is easy
    to read and outputs all the members of the class
    """
    def __str__(self):
        y = "{:*^30s}".format(f"{self.category}") + "\n"
        for item in self.ledger:
            y = y + f"{item['description'][:23].ljust(23)}" + "{:.2f}".format(item['amount']).rjust(7) + "\n"
        total = self.get_balance()
        y = y + "Total: " + "{:.2f}".format(total)
        return y

def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total = total - item['amount']
        spent.append(round(total, 2))
        category_names.append(category.category)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"

    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    ----" + ("---" * (len(category_names) - 1))
    graph += "\n     "

    longest_name_length = 0

    for name in category_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)

    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length - 1:
            graph += "\n     "

    return (graph)
