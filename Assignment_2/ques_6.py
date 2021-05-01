from typing import List, Dict

class User:
    def __init__(self, name: str, mobile: str, pin: str, username: str, password: str):
        self.name: str = name
        self.mobile: str = mobile
        self.__pin: str = pin
        self.username: str = username
        self.__password: str = password

    def verify_user(self, uname, passd):
        """
        Check if username and password match
        """
        return self.username == uname and self.__password == passd

    def verify_pin(self, pin):
        return self.__pin == pin

    def get_user(self):
        return {"name": self.name, "mobile": self.mobile, "username": self.username}

    def __modify_name(self, new_name):
        self.name = new_name

    def __modify_mobile(self, new_mobile):
        self.mobile = new_mobile

    def __modify_pin(self, new_pin):
        self.__pin = new_pin

    def __modify_pass(self, new_pass):
        self.__password = new_pass

    def __modify_private(self, ctype: str, value: dict):
        if value.get("cpass") != self.__password:
            return {"error": "incorrect password"}
        if ctype == "password":
            self.__modify_pass(value.get(ctype))
        elif ctype == "pin":
            self.__modify_pin(value.get(ctype))

    def modify_user(self, ctype: str, value):
        """
        Modifies user data. \n
        __requires__ = '[ctype: Change Type, value: str | dict]' \n
        The parameter value is assumed to be a dict if ctype is password or pin
        """
        if ctype == "name":
            self.__modify_name(value)
        elif ctype == "mobile":
            self.__modify_mobile(value)
        elif ctype == "password" or ctype == "pin":
            self.__modify_private(ctype, value)

class Bank:
    __users_list: List[Dict] = []

    def __init__(self):
        self.__users_list: List[Dict] = []

    def create_account(self, user: User):
        """
        Creates bank account for the user by adding \n
        bank specific details to the user object.
        """
        prev_users = self.__users_list

        # Increment acc. no. by 1 if any user present otherwise 1
        if len(prev_users) == 0:
            account_number = 1
        else:
            account_number = prev_users[-1].get("account_number") + 1

        __transaction_history: List[Dict] = []

        new_user = {
            **user.get_user(),
            "idx": len(prev_users),
            "account_number": account_number,
            "account_balance": 0,
            "transaction_history": __transaction_history,
        }
        prev_users.append(new_user)
        self.__users_list = prev_users

    def __get_current_user(self, user: User):
        """
        __requires__ = 'User object' \n
        Returns user if found in the list. Search by username
        """
        for usr in self.__users_list:
            if usr.get("username") == user.username:
                return usr
        return None

    def get_account_balance(self, user: User, pin: str):
        if not user.verify_pin(pin):
            return {"error": "Incorrect pin"}

        if not self.__get_current_user(user):
            return {"error": "User not found"}

        return self.__get_current_user(user).get("account_balance")

    def credit_money(self, user: User, amount: float):

        if(amount <=0 ):
            return {"error": "Amount must be greater than 0"}

        # Get the current user and increment amount
        curr_user = self.__get_current_user(user)
        curr_user["account_balance"] = curr_user.get("account_balance") + amount

        # Update transaction history as per the action
        history = curr_user.get("transaction_history")
        history.append({"type": "credit", "amount": amount})
        new_users_list = self.__users_list

        # Finally, get the index of current user and update users list
        new_users_list[curr_user.get("idx")] = curr_user
        self.__users_list = new_users_list

    def withdraw_money(self, user: User, amount: float):
        # Get the current user
        curr_user = self.__get_current_user(user)

        if(amount == -1):
            return

        if(amount <= 0):
            return {"error": "Amount must be greater than 0"}

        if curr_user.get("account_balance") < amount:
            return {"errror": "Not enough balance"}

        curr_user["account_balance"] = curr_user.get("account_balance") - amount

        # Update transaction history as per the action
        history = curr_user.get("transaction_history")
        history.append({"type": "debit", "amount": amount})
        new_users_list = self.__users_list

        # Finally, get the index of current user and update users list
        new_users_list[curr_user.get("idx")] = curr_user
        self.__users_list = new_users_list

    def get_transaction_history(self, user: User):
        return self.__get_current_user(user).get("transaction_history")
bank = Bank()

print(
    "Hey, Welcome to the bank!",
    "Please fill some details to create your bank account: ",
    sep="\n",
)
