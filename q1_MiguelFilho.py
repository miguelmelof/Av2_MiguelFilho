# Arquivo: q1_MiguelFilho.py

# Funções lambda para operações bancárias
print_receipt = lambda amount: f"Payment Receipt:\nAmount: {amount}"
confirm_transaction = lambda: "Transaction completed successfully."
cancel_transaction = lambda: "Transaction has been canceled."
receive_cash = lambda amount: print_receipt(amount)
transfer_funds = lambda details: f"Bank Deposit Details: {details}"
request_credit_details = lambda details: f"Credit Account Details: {details}"

# Função para criar transações, utilizando expressões lambda para controle de fluxo
create_transaction = lambda transaction_type: (
    (lambda amount: (
        print(print_receipt(amount)),
        print(confirm_transaction())
    ))(float(input("Enter the amount to receive: ")))
    if transaction_type == 'Cash' else

    (lambda details: (
        print(transfer_funds(details)),
        (print(confirm_transaction()) if input("Press 1 to Confirm or 2 to Cancel: ") == '1' else print(cancel_transaction()))
    ))(input("Provide Bank Deposit Details: "))
    if transaction_type == 'Fund Transfer' else

    (lambda details: (
        print(request_credit_details(details)),
        (print(confirm_transaction()) if input("Press 1 to Request Payment from Bank or 2 to Cancel: ") == '1' else print(cancel_transaction()))
    ))(input("Request Credit Account Details: "))
    if transaction_type == 'Credit' else
    "Invalid transaction type"
)

# Menu principal usando expressões lambda
main = lambda: (
    (lambda choice: (
        create_transaction('Cash') if choice == '1' else
        create_transaction('Fund Transfer') if choice == '2' else
        create_transaction('Credit') if choice == '3' else
        print("Exiting...") if choice == '4' else
        print("Invalid choice, try again.")
    ))(input("Main Menu:\n1. Cash\n2. Fund Transfer\n3. Credit\n4. Exit\nEnter your choice (1-4): "))
)

# Executa o programa
if __name__ == "__main__":
    while True:
        main()
