from collections import defaultdict
import tldextract
nsDict = {}
uniqueDomain = {}
tldDict = {}
def parseRR(line):
    data = json.loads(line)
    try:
        hostName = data['name']
        if hostName in uniqueDomain or data['status'] == 'NO_ANSWER':
            return
        uniqueDomain[hostName] = True
        tld = tldextract.extract(hostName).suffix
        if tld not in tldDict:
            tldDict[tld] = 0
        tldDict[tld] += 1
        for auth in data['trace'][-1]['results']['authorities']:
            ns = auth['answer']
            if ns not in nsDict:
                nsDict[ns] = 0
            nsDict[ns] += 1
    except:
        return


def writeResult(fName, d1, d2):
    with open(fName, 'w') as f:
        for k,v in d1:
            f.write(k + ':')
            for idx in range(len(v)-1):
                f.write(v[idx] + ',')
            f.write(v[-1] + '\n')

        for k,v in d2:
            f.write(k + ':')
            for idx in range(len(v)-1):
                f.write(v[idx] + ',')
            f.write(v[-1] + '\n')


with open ('/data1/nsrg/kwang40/fullData/2019-03-03/RR.json') with f:
    for line in f:
        if line[:4] == 'null':
            continue
        else:
            parseRR(line)

sorted_tld = sorted(tldDict.items(), key=lambda x: x[1], reverse=True)
sorted_NS = sorted(nsDict.items(), key=lambda x: x[1], reverse=True)

writeResult('DNSInfo.txt', sorted_tld, sorted_NS)
