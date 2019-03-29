with open('/data1/nsrg/kwang40/fullData/2019-03-03/banners.json') as f:
    with open('badGateway.txt', 'w') as f2:
        for line in f:
            if line.find('title\u003e502 Bad Gateway\u003c/title') != -1:
                domainStart = line.find('domain') + 9
                domain = line[domainStart:line.find('\"', domainStart + 1)]
                f2.write(domain + '\n')
