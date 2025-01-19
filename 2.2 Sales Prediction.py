# 2.2 Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales.
# Write a program that asks the user to enter the projected amount of total sales, then
# displays the profit that will be made from that amount.

total_sales = float(input("Enter the projected amount of total sales: "))
profit = total_sales * 0.23

print(f"The projected profit amount of ${total_sales:,.2f} will be ${profit:,.2f}.")
