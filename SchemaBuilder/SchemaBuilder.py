import json

file=open("raw-data.jl","rb")
lines=file.readlines();
i=lines[1]
t=eval(i)
Attribute_second_level=[]
print('create class Country subsume {"Countries"}[')
for h in t.keys():
    print('contain "'+h+'" (inverse belongto):"'+h+'",')
    s=eval(str(t[h]))
    if isinstance(s,dict):
        #print(s.keys())
        for c in s.keys():
            if isinstance(s[c],dict):
                pass#print (c)
print('];\n')
for h in t.keys():

    s=eval(str(t[h]))
    if isinstance(s,list):
        #print('create class "'+h+'"[')
        #print('@data*:string,')
        #print('];')
        pass
    if isinstance(s,dict):
        #print('create class "'+ h+'" [')
        pass
        for si in s.keys():
            pass
            #print('contain "'+si+'" (inverse belongto)*:"'+si+'",')
        #print("];")
    if isinstance(s,dict):
        for si in s.keys():
            sidic=eval(str(s[si]))
            if isinstance(sidic,dict):
                for sidicdic in sidic.keys():
                    #print(sidicdic)
                    if isinstance(sidicdic,dict):
                        print("!complex")
                    print('create class "'+sidicdic+'" [')
                    print ('@data*:string')
                    print('];')
        #if isinstance(sidic,dict):
            #print('create class "'+sidic+'" [')

          #  if isinstance(sidic,list):
          #      print('create class "'+si+'" [')
          #      print('@data*:string')
          #      print('];')
          #  if isinstance(sidic,dict):
          #      print('create class "'+si+'" [')
          #      for sidicdic in sidic.keys():
          #          print ('contain  "'+sidicdic+'" (inverse belongto) *:"'+sidicdic+'",')
          #      print('];')

    pass



pass