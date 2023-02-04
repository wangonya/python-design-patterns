from pos_facade import *


class Sale:
    def __init__(self):
        pass

    @staticmethod
    def make_invoice(customer_id):
        return Invoice(Customer.fetch(customer_id))

    @staticmethod
    def make_customer():
        return Customer()

    @staticmethod
    def make_item(item_barcode):
        return Item(item_barcode)

    @staticmethod
    def make_invoice_line(item):
        return InvoiceLine(item)

    @staticmethod
    def make_receipt(invoice, payment_type):
        return Receipt(invoice, payment_type)

    @staticmethod
    def make_loyalty_account(customer):
        return LoyaltyAccount(customer)

    @staticmethod
    def fetch_invoice(invoice_id):
        return Invoice(customer)

    @staticmethod
    def fetch_customer(customer_id):
        return Customer(customer_id)

    @staticmethod
    def fetch_item(item_barcode):
        return Item(item_barcode)

    @staticmethod
    def fetch_invoice_line(line_item_id):
        return InvoiceLine(item)

    @staticmethod
    def fetch_receipts(invoice_id):
        return Receipt(invoice, payment_type)

    @staticmethod
    def fetch_loyalty_account(customer_id):
        return LoyaltyAccount(customer)

    @staticmethod
    def add_item(invoice, item_barcode, amount_purchased):
        item = Item.fetch(item_barcode)
        item.amount_in_stock - amount_purchased
        item.save()
        invoice_line = InvoiceLine.make(item)
        invoice.add_line(invoice_line)

    @staticmethod
    def finalize(invoice):
        invoice.calculate()
        invoice.save()
        loyalt_account = LoyaltyAccount.fetch(invoice.customer)
        loyalty_account.calculate(invoice)
        loyalty_account.save()

    @staticmethod
    def generate_receipt(invoice, payment_type):
        receipt = Receipt(invoice, payment_type)
        receipt.save()
