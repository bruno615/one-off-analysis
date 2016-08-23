#1 - stock price.py

#stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

#get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

import pdb

def get_max_profit(stock_prices_yesterday):

  # If trading halts after only a single quote, max profit is 0
  if len(stock_prices_yesterday) = 1:
    return(0)

  # I disagree with the author, in that a day trader can always choose not to enter the market, which will result in a profit of 0
  best_profit = 0

  # This is O(xlogx) time, can do better
  for i in xrange(len(stock_prices_yesterday) - 1):
    best_price = max(stock_prices_yesterday[i + 1:])

    best_profit = max(best_profit, best_price - stock_prices_yesterday[i])

  return(best_profit)












# returns 6 (buying for $5 and selling for $11)
print(get_max_profit([10, 7, 5, 8, 11, 9]))
