# Arquivo: q2_MiguelFilho.py
import unittest
import sys

# Ajuste o caminho se os arquivos estiverem em diretórios diferentes
sys.path.append('/path/to/your/modules')
from q1_MiguelFilho import main

from unittest.mock import patch, call

# Helper functions using lambda
simulate_input = lambda inputs: (lambda f, inputs=inputs: [f(input) for input in inputs])(lambda x: x)

# Teste unitário
class TestBankingSystem(unittest.TestCase):

    # Testar a transação de 'Cash'
    @patch('builtins.input', side_effect=["1", "50", "1", "4"])
    @patch('builtins.print')
    def test_cash_transaction(self, mocked_print, mocked_input):
        main()
        mocked_print.assert_has_calls([
            call("Payment Receipt:\nAmount: 50.0"),
            call("Transaction completed successfully.")
        ])

    # Testar a transação de 'Fund Transfer'
    @patch('builtins.input', side_effect=["2", "Bank Details", "1", "4"])
    @patch('builtins.print')
    def test_fund_transfer_transaction(self, mocked_print, mocked_input):
        main()
        mocked_print.assert_has_calls([
            call("Bank Deposit Details: Bank Details"),
            call("Transaction completed successfully.")
        ])

    # Testar a transação de 'Credit'
    @patch('builtins.input', side_effect=["3", "Credit Details", "1", "4"])
    @patch('builtins.print')
    def test_credit_transaction(self, mocked_print, mocked_input):
        main()
        mocked_print.assert_has_calls([
            call("Credit Account Details: Credit Details"),
            call("Transaction completed successfully.")
        ])

# Executa os testes
if __name__ == "__main__":
    unittest.main()
