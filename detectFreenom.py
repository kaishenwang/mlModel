import json
with open('/data1/nsrg/kwang40/fullData/2019-03-03/banners.json') as f:
    with open('freenom.txt', 'w') as f2:
        for line in f:
            if line[:4] == 'null':
                continue
            try:
                data = json.loads(line.strip())
                if data['data']['http']['response']['status_line'] == '429 Too Many Requests':
                    f2.write(data['domain'] + '\n')
            except:
                continue
