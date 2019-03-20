with open ('/data1/nsrg/kwang40/mlData/preparedParkedInfo.csv') as r:
    count = 0
    countLine = 0
    with open('sampledParkedInfo.csv', 'w') as w:
        for line in r:
            countLine += 1
            if countLine % 12 != 5:
                continue
            w.write(line)
            count += 1
            if count >= 10000:
                break
        
