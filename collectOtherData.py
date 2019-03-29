import os
import json

rdName = '/data1/nsrg/kwang40/fullData/'
dNames = [name for name in os.listdir(rdName) if os.path.isdir(rdName + name)]
dNames.sort()

with open ('otherData.csv', 'w') as f:
    for i in range (len(dNames)):
        if not os.path.isfile(rdName + dNames[i] + '/log.txt'):
            continue
        if not os.path.isfile(rdName + dNames[i] + '/result.txt'):
            continue
        with open(rdName + dNames[i] + '/log.txt') as logFile:
            if i == 0:
                f.write('uniqueDomainCount,totalIpCount,uniqueIpCount,'
                        + 'uniqueOpenIpCount,domainOpenCount,urlOpenCount,success_count\n')
            lines = logFile.readlines()
            f.write(str(i) + ',')
            parts = lines[0].rstrip().split(':')
            totalCount = float(parts[1])
            for lineIdx in range(2,8):
                if lineIdx == 1:
                    continue
                parts = lines[lineIdx].rstrip().split(':')
                rate = float(parts[1]) / totalCount
                f.write(str(rate) + ',')
        with open(rdName + dNames[i] + '/result.txt') as resultFile:
            lines = resultFile.readlines()
            data = json.loads(lines[0][1:-1])
            sucess_rate = float(data['success_count']) / totalCount
            f.write(str(sucess_rate) + '\n')
