import json

file1 = open('output.jl')
lines1 = file1.readlines()
file2 = open('provincedetail.jl')
lines2 = file2.readlines()
file=open('provinceFinal.jl',"wb")
s={}
for i in lines1:
    t = eval(i)
    for j in lines2:
        m = eval(j)
        if t['url'] == m['url']:
            s['url']=t['url']
            s['country']=t['country']
            s['province']=m['province']
            line=json.dumps(dict(s))+"\n"
            file.write(line)
            pass
    pass
pass