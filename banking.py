# Write your code here
import sqlite3
import random

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


def count_rows(card_number):
    cur.execute(f'SELECT COUNT(*) FROM card WHERE number = "{card_number}"')
    rows = int(cur.fetchone()[0])
    return rows


def create_new_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS card
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  number TEXT,
                  pin TEXT,
                  balance INTEGER DEFAULT 0)''')
    conn.commit()


def check_balance(card_number):
    cur.execute(f'SELECT balance FROM card WHERE number = "{card_number}"')
    balance = float(cur.fetchone()[0])
    return balance


def insert_into_db(card_number, card_pin, balance=None):
    cur.execute(f'INSERT INTO card (number, pin) VALUES ("{card_number}", "{card_pin}")')
    conn.commit()


def update_balance(card_number, balance, action="add"):
    cur.execute(f'SELECT balance FROM card WHERE number = "{card_number}"')
    current_balance = float(cur.fetchone()[0])
    if action == "add":
        new_balance = current_balance + balance
        cur.execute(f'UPDATE card SET balance = "{new_balance}" WHERE number = "{card_number}"')
        conn.commit()
    elif action == "subtract":
        new_balance = current_balance - balance
        cur.execute(f'UPDATE card SET balance = "{new_balance}" WHERE number = "{card_number}"')
        conn.commit()


def delete_account(card_number):
    cur.execute(f'DELETE FROM card WHERE number = "{card_number}"')
    conn.commit()


def bank_menu():
    print("1. Create an account")
    print("2. Log into an account")
    print("0. Exit")
    return input()


def logged_menu():
    print("1. Balance")
    print("2. Add Income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")
    return input()


def generate_checksum(card_number):
    total_lunh = []
    counter = 1
    for i in card_number:
        if counter % 2 != 0:
            a = int(i) * 2
            if a > 9:
                total_lunh.append(a - 9)
            else:
                total_lunh.append(a)
        else:
            total_lunh.append(int(i))
        counter += 1
    checksum = 0
    total_sum_15 = sum(total_lunh)
    while True:
        if (total_sum_15 + checksum) % 10 == 0:
            break
        checksum += 1
    return str(checksum)


def create_account():
    card_number_row = "400000" + "".join([str(random.randrange(0, 9)) for x in range(9)])
    checksum = generate_checksum(card_number_row)
    card_pin = "".join([str(random.randrange(0, 9)) for x in range(4)])
    new_card = [card_number_row + checksum, card_pin]
    return new_card


def login_to_acc(card_number, pin):
    cur.execute(f'SELECT COUNT(*) FROM card WHERE number = "{card_number}" AND pin = "{pin}"')
    rows = cur.fetchone()[0]
    if rows == 1:
        return True
    else:
        return False


def start():
    create_new_table()

    while True:
        inp = bank_menu()
        if inp == "0":
            print("Bye!")
            exit()
        elif inp == "1":
            new_account = create_account()
            new_card_number = new_account[0]
            new_card_pin = new_account[1]
            insert_into_db(new_card_number, new_card_pin)
            print("Your card has been created")
            print("Your card number:")
            print(new_card_number)
            print("Your card PIN:")
            print(new_card_pin)
        elif inp == "2":
            print("Enter your card number:")
            card_number = input()
            print("Enter your PIN:")
            pin = input()
            logged_in = login_to_acc(card_number, pin)
            if not logged_in:
                print("Wrong card number or PIN!")
                continue
            else:
                print("You have successfully logged in!")
                while True:
                    lm = logged_menu()
                    if lm == "1":
                        balance = check_balance(card_number)
                        print(f"Balance: {balance}")
                        print()
                    elif lm == "2":
                        print("Enter income:")
                        income = float(input())
                        update_balance(card_number, income)
                        print("Income was added!")
                        print()
                    elif lm == "3":
                        print("Enter card number:")
                        destination_card_number = input()
                        first_15 = destination_card_number[:-1]
                        last_1 = destination_card_number[-1]
                        generated_luhn_checksum = generate_checksum(first_15)

                        if last_1 != generated_luhn_checksum:
                            print("Probably you made mistake in the card number. Please try again!")
                            print()
                            continue
                        elif destination_card_number == first_15 + generated_luhn_checksum:
                            if count_rows(destination_card_number) == 0:
                                print("Such a card does not exist.")
                                print()
                                continue
                            elif count_rows(destination_card_number) == 1:
                                print("Enter how much money you want to transfer:")
                                transfer_amount = float(input())
                                balance = check_balance(card_number)
                                if transfer_amount > balance:
                                    print("Not enough money!")
                                    print()
                                    continue
                                else:
                                    update_balance(card_number, transfer_amount, "subtract")
                                    update_balance(destination_card_number, transfer_amount)
                                    print("Success!")
                                    print()
                                    continue
                    elif lm == "4":
                        delete_account(card_number)
                        print("The account has been closed!")
                        print()
                        break
                    elif lm == "5":
                        print("You have successfully logged out!")
                        print()
                        break
                    elif lm == "0":
                        print("Bye!")
                        exit()

    conn.close()


start()
