rdName = '/data1/nsrg/kwang40/fullData/'
dNames = [name for name in os.listdir(rdName) if os.path.isdir(name)]
dNames.sort()

with open ('otherData.csv', 'w') as f:
    for i in range (20):
        with open(rdName + dNames[i] + '/log.txt') as logFile:
            if i == 0:
                f.write('uniqueDomainCount,totalIpCount,uniqueIpCount,'
                + 'uniqueOpenIpCount,domainOpenCount,urlOpenCount')
            lines = logFile.readlines()
            for lineIdx in range(2, 8):
                parts = lines[lineIdx].rstrip().split(':')
                f.write(parts[1] + '\n')
