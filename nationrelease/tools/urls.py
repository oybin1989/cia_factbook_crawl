# parse urls in json file

import json

file=open('urls.jl')
jsons=file.readlines()
for j in jsons:
    t=eval(j)
    print(t)
pass
