def record(data,name='record'):
    with open('./{}.txt'.format(name),'w+') as f:
        f.write(data)