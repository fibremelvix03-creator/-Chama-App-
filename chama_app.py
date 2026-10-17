import json

class ChamaMember:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.savings = 0
        self.loan = 0

    def contribute(self, amount):
        self.savings += amount
        return f"{self.name} contributed {amount}. Total savings: {self.savings}"

    def request_loan(self, amount):
        max_loan = self.savings * 3
        if amount > max_loan:
            return f"Denied. You can only borrow up to 
            members.append(m)
        return members
    except:
        return []

members = load_members()

while True:
    print("\n--- CHAMA APP ---")
    print("1. Add Member")
    print("2. Contribute")
    print("3. Request Loan")
    print("4. Show Balance")
    print("5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        members.append(ChamaMember(name, phone))
        save_members(members)
        print(f"Member {name} added!")
    elif choice == "2":
        idx = int(input("Member number (start 0): "))
        amt = int(input("Amount: "))
        print(members[idx].contribute(amt))
        save_members(members)
    elif choice == "3":
        idx = int(input("Member number: "))
        amt = int(input("Loan amount: "))
        print(members[idx].request_loan(amt))
        save_members(members)
    elif choice == "4":
        for i, m in enumerate(members):
            print(f"{i}. {m.name} - Savings: {m.savings}, Loan: {m.loan}")
    elif choice == "5":
        save_members(members)
        print("Saved. Bye!")
        break
