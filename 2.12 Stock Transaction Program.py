# 2.12 Stock Transaction Program
# Last month, Joe purchased some stock in Acme Software, Inc. Here are the details 
# of the purchase:
#  * The number of shares that Joe purchased was 2,000.
#  * When Joe purchased the stock, he paid $40.00 per share.
#  * Joe paid his stockbroker a commission that amounted to 3 percent of the amount 
#    he paid for the stock.
# Two weeks later, Joe sold the stock. Here are the details of the sale:
#  * The number of shares that Joe sold was 2,000.
#  * He sold the stock for $42.75 per share.
#  * He paid his stockbroker another commission that amounted to 3 percent of the amount 
#    he received for the stock.
# Write a program that displays the following information:
#  * The amount of money Joe paid for the stock.
#  * The amount of commission joe paid his broker when he bought the stock.
#  * The amount for which Joe sold the stock.
#  * The amount of commission Joe paid his broker when he sold the stock.
#  * Display the amount of money that Joe had left when he sold the stock and paid his 
#    broker(both times). If this amount is positive, then Joe made a profit. If the amount
#    is negative, then Joe lost money.
# Create variables.
SHARES = 2000
PRICE_PURCHASED = 40.00
PRICE_SOLD = 42.75
COMMISSION_RATE_BROKER = 0.03

# Calculate purchase cost.
net_purchased = SHARES * PRICE_PURCHASED
commission_purchased = net_purchased * COMMISSION_RATE_BROKER
total_purchased = net_purchased + commission_purchased

# Calculate profit or loss
total_sold = SHARES * PRICE_SOLD
commission_sold = total_sold * COMMISSION_RATE_BROKER
net_sold = total_sold - commission_sold
result_transaction = net_sold - total_purchased

# Display the Stock Transaction Result.
print('\n**** Stock Transaction Result ****')
print('+'*60)
print(f"{'Total Purchase Cost':<35} {total_purchased:>15,.2f}")
print(f"{'Total sell Amount':<35} {total_sold:>15,.2f}")
print(f"{'Broker Commission for selling':<35} {commission_sold:>15,.2f}")
print('='*60)

if result_transaction < 0:
    print(f"{'Transaction result':<35} ${abs(result_transaction):>15,.2f} loss")
else:
    print(f"{'Transaction result':<35} ${result_transaction:>15,.2f} profit")
    


