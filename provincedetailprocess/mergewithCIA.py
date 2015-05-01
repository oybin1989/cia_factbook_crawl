import json

file_CIA= open('details.jl')
file_Province=open('provinceFinal.jl')
file_Merge=open('MergeInfo.jl','wb')

lines_CIA=file_CIA.readlines()
lines_Province=file_Province.readlines()
i=0;
for c in lines_CIA:
    cj=eval(c)
    exist=0
    #print cj['country']
    for l in lines_Province:
        lj=eval(l)

        #print lj['country'].upper()
        if cj['country'][0]==lj['country'].upper()+" ":
            #print cj['country']
            i=i+1
            exist=1
            cj['province']=[]
            provinceItem={'province':[],'url':" ",'country':" "}
            provinceItem['province']=lj['province']
            provinceItem['url']=lj['url']
            provinceItem['country']=cj['country'][0]
            cj['province'].append(provinceItem)
            print cj['province']
            line=json.dumps(dict(cj))+"\n"
            file_Merge.write(line)
            pass
        pass
    if exist==0:
        line=json.dumps(dict(cj))+"\n"
        file_Merge.write(line)
    pass
print i
pass
