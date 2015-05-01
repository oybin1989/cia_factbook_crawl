import json

file=open('urls.jl',"rb")
line=file.readlines()
filewrite=open('output.jl','wb')
for i in line:
    print i
    t=eval(i)
    a={'url':" ",'country':" "}
    i=0
    for url in t['url']:
        print url
        a['url']='http://www.statoids.com/'+url
        a['country']=t['country'][i]
        i=i+1
        print a
        line=json.dumps(dict(a))+"\n"
        filewrite.write(line)


pass
