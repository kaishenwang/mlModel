import csv

maxATagLen = 0.0
maxPageLen = 0.0
for file in ['/data1/nsrg/kwang40/topDomainData/topDomainInfo.csv', '/home/kwang40/testExtractor/parkedInfo.csv']:
    with open (file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
                maxATagLen = max(aTagLen, maxATagLen)
            if float(row['rawPageLen']) != 0:
                maxPageLen = max(maxPageLen, float(row['rawPageLen']))


topParkedDomains = {}
with open('/home/kwang40/parkedDomainHeuristic/topDomainsByID.txt') as f:
    for line in f:
        if line.rstrip() != 'sedo.com' and line.rstrip() != 'afternic.com':
            topParkedDomains[line.rstrip()] = True

with open ('/data1/nsrg/kwang40/topDomainData/topDomainInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    domains = {}
    with open ('tmpNonParked.csv', 'w') as f:
        f.write('parked,rawPageLen,textTotalRatio,jsCodeTotalRatio,aTagLen,')
        f.write('index,follow,archive\n')
        count = 0
        for row in reader:
            if row['domain'] in domains or row['domain'] in topParkedDomains:
                continue
            count += 1
            if count > 10000:
                break
            domains[row['domain']] = True
            f.write('0,')
            pageLen = 0.0
            textTotalRatio = 0.0
            jsCodeTotalRatio = 0.0
            if float(row['rawPageLen']) != 0:
                pageLen = float(row['rawPageLen'])
                textTotalRatio = (float(row['headTextLen']) + float(row['bodyTextLen'])) / pageLen
                jsCodeTotalRatio = float(row['codeLen']) / pageLen
            f.write(str(row['rawPageLen']/maxPageLen) + ',' + str(textTotalRatio) + ',' + str(jsCodeTotalRatio) + ',')
            aTagLen = 0
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
                aTagLen = aTagLen / maxATagLen
            f.write(str(aTagLen) + ',')
            f.write(row['index'] + ',')
            f.write(row['follow'] + ',')
            f.write(row['archive'] + '\n')

with open ('/home/kwang40/testExtractor/parkedInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    domains = {}
    with open ('tmpParked.csv', 'w') as f:
        f.write('parked,rawPageLen,textTotalRatio,jsCodeTotalRatio,aTagLen')
        f.write('index,follow,archive\n')

        for row in reader:
            if row['domain'] in domains:
                continue
            domains[row['domain']] = True
            f.write('1,')
            pageLen = 0.0
            textTotalRatio = 0.0
            jsCodeTotalRatio = 0.0
            if float(row['rawPageLen']) != 0:
                pageLen = float(row['rawPageLen'])
                textTotalRatio = (float(row['headTextLen']) + float(row['bodyTextLen'])) / pageLen
                jsCodeTotalRatio = float(row['codeLen']) / pageLen
            f.write(str(row['rawPageLen']/maxPageLen) + ',' + str(textTotalRatio) + ',' + str(jsCodeTotalRatio) + ',')
            aTagLen = 0
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
                aTagLen = aTagLen / maxATagLen
            f.write(str(aTagLen) + ',')
            f.write(row['index'] + ',')
            f.write(row['follow'] + ',')
            f.write(row['archive'] + '\n')

nonParkDomainResult = []
with open ('tmpNonParked.csv') as f:
    nonParkDomainResult = f.readlines()
parkDomainResult = []
with open ('tmpParked.csv') as f:
    parkDomainResult = f.readlines()

with open ('data.csv', 'w') as f:
    f.write(nonParkDomainResult[0])
    nonParkIdx = 1
    parkIdx = 1
    parkStep = len(parkDomainResult) / 10000 - 2
    for i in range(20000):
        if i % 2 == 1:
            f.write(parkDomainResult[parkIdx])
            parkIdx += parkStep
        else:
            f.write(nonParkDomainResult[nonParkIdx])
            nonParkIdx += 1

with open ('/data1/nsrg/kwang40/topDomainData/topDomainInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    domains = {}
    with open ('tmpNonParked2.csv', 'w') as f:
        f.write('parked,rawPageLen,textTotalRatio,jsCodeTotalRatio,frameCount,aTagLen,')
        f.write('index,follow,archive,snippet,translate,imageindex,unavailable_after,url\n')
        count = 0
        for row in reader:
            if row['domain'] in domains or row['domain'] in topParkedDomains:
                continue
            count += 1
            if count > 10000:
                break
            domains[row['domain']] = True
            f.write('0,')
            pageLen = 0.0
            textTotalRatio = 0.0
            jsCodeTotalRatio = 0.0
            if float(row['rawPageLen']) != 0:
                pageLen = float(row['rawPageLen'])
                textTotalRatio = (float(row['headTextLen']) + float(row['bodyTextLen'])) / pageLen
                jsCodeTotalRatio = float(row['codeLen']) / pageLen
            f.write(str(row['rawPageLen']/maxPageLen) + ',' + str(textTotalRatio) + ',' + str(jsCodeTotalRatio) + ',' + row['frameCount'] + ',')
            aTagLen = 0
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
                aTagLen = aTagLen / maxATagLen
            f.write(str(aTagLen) + ',')
            f.write(row['index'] + ',')
            f.write(row['follow'] + ',')
            f.write(row['archive'] + ',')
            f.write(row['snippet'] + ',')
            f.write(row['translate'] + ',')
            f.write(row['imageindex'] + ',')
            f.write(row['unavailable_after'] + ',' + row['URL'] + '\n')

with open ('/home/kwang40/testExtractor/parkedInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    domains = {}
    with open ('tmpParked2.csv', 'w') as f:
        f.write('parked,rawPageLen,textTotalRatio,jsCodeTotalRatio,frameCount,aTagLen')
        f.write('index,follow,archive,snippet,translate,imageindex,unavailable_afteri,url\n')

        for row in reader:
            if row['domain'] in domains:
                continue
            domains[row['domain']] = True
            f.write('1,')
            pageLen = 0.0
            textTotalRatio = 0.0
            jsCodeTotalRatio = 0.0
            if float(row['rawPageLen']) != 0:
                pageLen = float(row['rawPageLen'])
                textTotalRatio = (float(row['headTextLen']) + float(row['bodyTextLen'])) / pageLen
                jsCodeTotalRatio = float(row['codeLen']) / pageLen
            f.write(str(row['rawPageLen']/maxPageLen) + ',' + str(textTotalRatio) + ',' + str(jsCodeTotalRatio) + ',' + row['frameCount'] + ',')
            aTagLen = 0
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
                aTagLen = aTagLen / maxATagLen
            f.write(str(aTagLen) + ',')
            f.write(row['index'] + ',')
            f.write(row['follow'] + ',')
            f.write(row['archive'] + ',')
            f.write(row['snippet'] + ',')
            f.write(row['translate'] + ',')
            f.write(row['imageindex'] + ',')
            f.write(row['unavailable_after'] +','+ row['domain'] + '\n')

nonParkDomainResult = []
with open ('tmpNonParked2.csv') as f:
    nonParkDomainResult = f.readlines()
parkDomainResult = []
with open ('tmpParked2.csv') as f:
    parkDomainResult = f.readlines()

with open ('dataWithUrl.csv', 'w') as f:
    f.write(nonParkDomainResult[0])
    nonParkIdx = 1
    parkIdx = 1
    parkStep = len(parkDomainResult) / 10000 - 2
    for i in range(20000):
        if i % 2 == 1:
            f.write(parkDomainResult[parkIdx])
            parkIdx += parkStep
        else:
            f.write(nonParkDomainResult[nonParkIdx])
            nonParkIdx += 1
