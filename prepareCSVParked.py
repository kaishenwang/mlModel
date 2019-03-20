import csv
output = ""
with open ('/home/kwang40/testExtractor/parkedInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    domains = {}
    with open ('/home/kwang40/testExtractor/preparedParkedInfo.csv', 'w') as f:
        f.write('parked,textTotalRatio,jsCodeTotalRatio,frameCount,aTagLen')
        f.write('index,follow,archive,snippet,translate,imageindex,unavailable_after\n')

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
            f.write(str(textTotalRatio) + ',' + str(jsCodeTotalRatio) + ',' + row['frameCount'] + ',')
            aTagLen = 0
            if float(row['aTagCount']) != 0:
                aTagLen = float(row['aTagLen']) / float(row['aTagCount'])
            f.write(str(aTagLen) + ',')
            f.write(row['index'] + ',')
            f.write(row['follow'] + ',')
            f.write(row['archive'] + ',')
            f.write(row['snippet'] + ',')
            f.write(row['translate'] + ',')
            f.write(row['imageindex'] + ',')
            f.write(row['unavailable_after'] + '\n')
