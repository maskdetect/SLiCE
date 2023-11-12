import ast
if __name__ == '__main__':
    fn = 'train.txt'
    # dict_fn = 'ent2id.txt'

    # with open(dict_fn,'r') as f:
    #     dict_id = ast.literal_eval(f.read())
    #     print(dict_id)
    with open(fn,'r') as f:
        edges = ""
        for line in f.readlines():
            _,src,dst = line.split(" ")
            # edges+= dict_id[int(src)]+" "+dict_id[int(dst)]+"\n"

    output_fn = 'edgelists.txt'
    with open(output_fn,'w') as g:
        g.write(edges)
