import json
if __name__ == '__main__':
    fn = 'amazon_s.emd'
    ent2id = dict()
    cnt = 0
    with open(fn,'r') as f:
        for line in f.readlines()[1:]:
            ent2id[line.split(" ")[0]] = cnt
            cnt += 1
    with open('ent2id.txt','w') as g:
        g.write(json.dumps(ent2id))

