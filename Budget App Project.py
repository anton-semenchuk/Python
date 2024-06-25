class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.budget = 0
    
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.budget += amount

    def withdraw(self,amount, description=''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False

    def get_balance(self):
        return self.budget
    
    def transfer(self, amount, another_category):
        if self.check_funds(amount):
            self.budget -= amount
            self.ledger.append(
                {"amount": -amount, "description": f"Transfer to {another_category.category}"})
            another_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        string_output = '' 
        title = self.category.center(30, '*')
        string_output += title
        string_output += '\n'

        for item in self.ledger:
            description = item['description']
            amount = item['amount']
            string_output += f'{description[0:23]:23}{amount:7.2f}'
            string_output += '\n'
        string_output += 'Total: '
        string_output += format(self.budget, '.2f')

        return string_output

food = Category("Food")
clothing = Category("Clothing")
auto = Category('Auto')

food.deposit(1000, "deposit")
food.withdraw(600, "groceries")
food.withdraw(165.60, "books")
food.withdraw(175.10, "books")

clothing.deposit(1000, "deposit")
clothing.withdraw(200, "groceries")

auto.deposit(1000, "deposit")
auto.withdraw(100, "groceries")

print(food)
print(clothing)
print(auto)

def create_spend_chart(categories):
    max_len = 0
    total = 0
    item_list = {}
    percent_list = {}
    print_string = ''
    for cat in categories:
        max_len = max(max_len, len(cat.category))
        line_total = 0
        for line_item in cat.ledger:
            if line_item['amount'] < 0:
                line_total += abs(line_item['amount'])
                total += abs(line_item['amount'])
        item_list[cat.category] = line_total
    
    for cat in categories:
        percent = int(item_list[cat.category]/total*100)
        percent_list[cat.category] = percent
    
    print_string += 'Percentage spent by category\n'
    for i in range(10,-1,-1):
        print_string += str(i * 10).rjust(3) + '|'
        for cat in categories:
            if percent_list[cat.category] >= i * 10:
                print_string += ' o '
            else: print_string += '   '
        print_string += ' \n'

    print_string += '    ' + (('---' * len(percent_list)) + '-')
    for num in range(max_len):
        str_cat = ''
        for i in range(len(categories)):
            str_cat += f'{categories[i].category[num]}  ' if num < len(categories[i].category) else '   '
        print_string += f'\n     {str_cat}'


    return print_string


create_spend_chart([food, clothing, auto])