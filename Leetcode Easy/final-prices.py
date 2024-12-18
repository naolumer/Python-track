def finalPrice(prices):

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]>=prices[j]:
                prices[i]=prices[i]-prices[j]
                break
            else:
                continue
    return prices
print(finalPrice([10,1,1,6]))
