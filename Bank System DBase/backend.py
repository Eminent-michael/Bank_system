"""
This is a Bank system program
        __Functions__
# -User can save money.
-User can transfer money
# -User can Check current balance
-User can recharge card from their account.
# -User can see all details about them with (all)
-User can invest their money.
"""


# //TODO: Create CSV file to collect single User:

import sqlite3


class Account:
    def __init__(self):
        self.connect = sqlite3.connect("Account.db")
        self.cur = self.connect.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS account (name TEXT, email TEXT, account_no INTEGER PRIMARY KEY, pin INTEGER, balance REAL)")

    def create_account(self, name, email="", account_no=0, pin=0, balance=0):
        self.cur.execute("INSERT INTO account VALUES(?,?,?,?,?)", (name, email, account_no, pin, balance))

    def deposit(self, account_no, pin, balance):
        self.cur.execute("UPDATE account SET balance=balance + ? WHERE account_no=? and pin=?", (balance, account_no, pin))

    def withdraw(self, account_no, pin, balance):
        self.cur.execute("UPDATE account SET balance=balance - ? WHERE account_no=? and pin=?", (balance, account_no, pin))

    def all_info(self):
        self.cur.execute("SELECT * FROM account")
        rows = self.cur.fetchall()
        return rows

    def commit(self):
        self.connect.commit()
        self.connect.close()

    def check_balance(self, account_no, pin):
        self.cur.execute("SELECT balance FROM account WHERE account_no = ? and pin = ?", (account_no, pin))
        rows = self.cur.fetchone()
        return rows

    def transfer(self, amount, account_no, pin, recipient):
        self.cur.execute("SELECT balance FROM account WHERE account_no = ? and pin = ?", (account_no, pin))
        rows = self.cur.fetchone()[0]
        if rows < amount:
            print("Insufficient balance as your balance is %s" % rows)
        elif amount < 100:
            print("You can not transfer amount less than 100")
        else:
            self.cur.execute("UPDATE account SET balance=balance - ? WHERE account_no=? and pin=?", (amount, account_no, pin))
            self.cur.execute("UPDATE account SET balance=balance + ? WHERE account_no=?", (amount, recipient))

    def check_account_name(self, recipient):
        self.cur.execute("SELECT name FROM account WHERE account_no = ?", (recipient,))
        rows = self.cur.fetchone()[0]
        return rows
