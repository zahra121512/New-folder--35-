def calculate_due_amount(bill_amount, payment_amount):
  """Calculates the due amount after a partial payment.

  Args:
    bill_amount: The total amount of the bill.
    payment_amount: The amount paid by the customer.

  Returns:
    The remaining due amount.
  """

  due_amount = bill_amount - payment_amount
  return due_amount

if __name__ == "__main__":
  bill_amount = float(input("Enter the total bill amount: "))
  payment_amount = float(input("Enter the amount paid: "))

  due_amount = calculate_due_amount(bill_amount, payment_amount)

  print("The due amount is:", due_amount)