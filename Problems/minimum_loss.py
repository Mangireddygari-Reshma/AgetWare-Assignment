def minimum_loss(prices):
    price_to_year = {price: year + 1 for year, price in enumerate(prices)}
    sorted_prices = sorted(prices, reverse=True)

    min_loss = float('inf')
    buy_year = sell_year = -1

    for i in range(len(sorted_prices) - 1):
        high = sorted_prices[i]
        low = sorted_prices[i + 1]
        if price_to_year[high] < price_to_year[low]:  
            loss = high - low
            if 0 < loss < min_loss:
                min_loss = loss
                buy_year = price_to_year[high]
                sell_year = price_to_year[low]

    return buy_year, sell_year, min_loss
prices = list(map(int, input("Enter the prices for each year (space-separated): ").split()))
if len(prices) < 2:
    print("At least two years of prices are required.")
else:
    buy_year, sell_year, min_loss = minimum_loss(prices)
    if min_loss == float('inf'):
        print("No valid buy-sell pair found.")
    else:
        print(f"Buy in year {buy_year}, sell in year {sell_year}, minimum loss: {min_loss}")