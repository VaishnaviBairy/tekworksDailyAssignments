
import streamlit as st

class Bank:
    totalamount = 100000

    def __init__(self):
        self.totalamount = Bank.totalamount

    def Deposit(self, damount):
        if (damount % 100) == 0 and 100 < damount < 50000:
            self.totalamount += damount
            return f"Deposit accepted. New balance: {self.totalamount}"
        else:
            return "Deposit rejected. Amount must be in multiples of 100 and between 100 and 50,000."

    def Withdraw(self, withdrawamount):
        limitamount = 20000
        if withdrawamount >= 100 and withdrawamount % 100 == 0 and withdrawamount <= self.totalamount and withdrawamount <= limitamount:
            self.totalamount -= withdrawamount
            return f"Withdraw accepted. Remaining balance: {self.totalamount}"
        else:
            return "Withdraw rejected. Invalid amount or limit exceeded."

    def balEnquiry(self):
        return f"Current balance: {self.totalamount}"

    def validate(self, pinnum):
        return pinnum == 1234

# Initialize the bank object
bank_obj = Bank()

def main():
    st.title("Banking Application")

    # Initialize session state for pin attempts
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 3
        st.session_state.authenticated = False

    # Check if the user is already authenticated
    if not st.session_state.authenticated:
        # Validate Pin
        pinnum = st.text_input("Enter Pin Number", type="password")

        if pinnum:
            if bank_obj.validate(int(pinnum)):
                st.session_state.authenticated = True
                st.success("Pin validated successfully!")
                view_options()
            else:
                st.session_state.attempts -= 1
                if st.session_state.attempts > 0:
                    st.error(f"Invalid Pin Number. You have {st.session_state.attempts} attempts remaining.")
                else:
                    st.error("Too many incorrect attempts. Access locked.")
    else:
        view_options()

def view_options():
    option = st.selectbox('Choose an option:', ('Deposit', 'Withdraw', 'Balance Enquiry', 'Exit'))

    if option == 'Deposit':
        damount = st.number_input("Enter the amount to deposit", min_value=0)
        if st.button('Deposit'):
            if damount > 0:
                result = bank_obj.Deposit(damount)
                st.write(result)
            else:
                st.write("Please enter a valid deposit amount.")

    elif option == 'Withdraw':
        withdrawamount = st.number_input("Enter the amount to withdraw", min_value=0)
        if st.button('Withdraw'):
            if withdrawamount > 0:
                result = bank_obj.Withdraw(withdrawamount)
                st.write(result)
            else:
                st.write("Please enter a valid withdraw amount.")

    elif option == 'Balance Enquiry':
        result = bank_obj.balEnquiry()
        st.write(result)

    elif option == 'Exit':
        st.write("Thank you for using the banking application!")

if __name__ == "__main__":
    main()

