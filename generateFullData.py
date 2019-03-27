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

with open ('/home/kwang40/mlModel/fullDataInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open ('fullDataPrepared.csv', 'w') as f:
        f.write('parked,rawPageLen,textTotalRatio,jsCodeTotalRatio,aTagLen,')
        f.write('index,follow,archive\n')
        for row in reader:
            f.write('1,')
            pageLen = 0.0
            textTotalRatio = 0.0
            jsCodeTotalRatio = 0.0
            if float(row['rawPageLen']) != 0:
                pageLen = float(row['rawPageLen'])
                textTotalRatio = (float(row['headTextLen']) + float(row['bodyTextLen'])) / pageLen
                jsCodeTotalRatio = float(row['codeLen']) / pageLen
            f.write(str(float(row['rawPageLen'])/maxPageLen) + ',' + str(textTotalRatio) + ',' + str(jsCodeTotalRatio) + ',')
            aTagLen = 0
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
                aTagLen = aTagLen / maxATagLen
            f.write(str(aTagLen) + ',')
            f.write(row['index'] + ',')
            f.write(row['follow'] + ',')
            f.write(row['archive'] + '\n')

with open ('/home/kwang40/mlModel/fullDataInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open ('fullDataPreparedWithURL.csv', 'w') as f:
        f.write('parked,URL,rawPageLen,textTotalRatio,jsCodeTotalRatio,aTagLen,i')
        f.write('index,follow,archive\n')
        for row in reader:
            f.write('1,' + row['domain'] + ',')
            pageLen = 0.0
            textTotalRatio = 0.0
            jsCodeTotalRatio = 0.0
            if float(row['rawPageLen']) != 0:
                pageLen = float(row['rawPageLen'])
                textTotalRatio = (float(row['headTextLen']) + float(row['bodyTextLen'])) / pageLen
                jsCodeTotalRatio = float(row['codeLen']) / pageLen
            f.write(str(float(row['rawPageLen'])/maxPageLen) + ',' + str(textTotalRatio) + ',' + str(jsCodeTotalRatio) + ',')
            aTagLen = 0
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
                aTagLen = aTagLen / maxATagLen
            f.write(str(aTagLen) + ',')
            f.write(row['index'] + ',')
            f.write(row['follow'] + ',')
            f.write(row['archive'] + '\n')
