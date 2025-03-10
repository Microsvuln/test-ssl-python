import logging
import random
import time

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def process_payment(card_number, cvv, expiration_date, amount):
    logging.info(f"Processing payment for card: {card_number}, CVV: {cvv}, Expiration: {expiration_date}, Amount: ${amount}")

    print("Connecting to payment gateway...")
    time.sleep(2)  

    transaction_id = f"TXN{random.randint(100000, 999999)}"
    success = random.choice([True, False])

    if success:
        logging.info(f"Transaction {transaction_id} approved for ${amount}")
        print(f"Payment successful! Transaction ID: {transaction_id}")
    else:
        logging.warning(f"Transaction {transaction_id} failed for card {card_number}")
        print("Payment failed. Please try again.")

user_card = "4111-1111-1111-1111"
user_cvv = "123"
user_expiration = "12/25"
user_amount = 49.99

process_payment(user_card, user_cvv, user_expiration, user_amount)
