#portfolio tracker 
stock_prices={
    "AAPL":180,
    "TSLA":140,
    "GOOG":250,
    "MSFT":300
}
total_investment=0

while True:
    stock=input("Enter stock name (or type 'DONE' to finish): ").upper()
    if stock=='DONE':
        break
    if stock in stock_prices:
        quantity=int(input("Enter quantity : "))
        investment=stock_prices[stock]*quantity
        total_investment+=investment
        print(f"Investment in {stock}: {investment}")
    else:
        print("Stock not fount in our list.")
print("Total Portfolio Value: $",total_investment)