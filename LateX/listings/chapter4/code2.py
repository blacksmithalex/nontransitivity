def strategy23(data, day, a, b):
    df = data[data['<DATE>'] == day]
    prices = list(df['<OPEN>'])
    start_price = prices[0]
    income = 0 
    for p in prices[1:]:
        percent = round((p/start_price - 1) * 100, 3)
        if percent > a or percent < -b:
            income = p - start_price
            break
    if income == 0:
        return round(start_price - prices[-1], 4)
    else:
        return round(income, 4)
    
def betterthan(a1, a2):
    count = 0
    for i in range(len(a1)):
        if a1[i] > a2[i]:
            count += 1
    return count 