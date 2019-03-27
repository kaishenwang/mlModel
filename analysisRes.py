# get detected parked domains
detected = {}
with open('/home/kwang40/parkedDomainHeuristic/fullParkedDomains.txt') as f:
    for line in f:
        detected[line.rstrip()] = True

# get domains
domainList = []
with open('fullDataPreparedWithURL.csv') as f:
    firstLine = True
    for line in f:
        if firstLine:
            firstLine = False
            continue
        parts = line.split(',')
        domainList.append(parts[1])

count = 0
with open('predictionResult.txt') as f:
    with open('newDomains.txt', 'w') as f2:
        idx = 0
        for line in f:
            if line[0] == '1':
                count += 1
                if domainList[idx] not in detected:
                    f2.write(domainList[idx] + '\n')
            idx += 1
print ('Total Count is ' + str(count))
