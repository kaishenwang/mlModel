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
                f.write('totalUrlCount,uniqueDomainCount,totalIpCount,uniqueIpCount,'
                        + 'uniqueOpenIpCount,domainOpenCount,urlOpenCount,success_count\n')
            lines = logFile.readlines()
            f.write(str(i) + ',')
            for lineIdx in range(8):
                if lineIdx == 1:
                    continue
                parts = lines[lineIdx].rstrip().split(':')
                f.write(parts[1] + ',')
        with open(rdName + dNames[i] + '/result.txt') as resultFile:
            lines = resultFile.readlines()
            data = json.loads(lines[0][1:-1])
            f.write(str(data['success_count']) + '\n')
