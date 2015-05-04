# -*- coding: utf-8 -*-
import json
import re
file=open("raw-data-utf8.jl","rb")
fileprovince=open("provinceFinal.jl","rb")
file1=open('insert.txt',"w")
lines=file.readlines()

# sub-class of type "list"
'''for line in lines:
    linedic=eval(line)
    print ('insert "Countries" "'+linedic['country'][0]+' "[')
    for e_linedic in linedic.keys():
        if isinstance(linedic[e_linedic],list) and e_linedic!='province' and len(linedic[e_linedic][0])>0:
            print ('contain '+str(e_linedic)+':{"'+str(e_linedic)+' of '+ linedic['country'][0]+'"''[@data:"'+str(linedic[e_linedic][0]).replace('"',"'").replace("\n","").replace("\r","")+'"]}("'+linedic['country'][0]+'"),')
    print('];')'''
# sub-class of type "dict" but third-level sub-class is type of "list"
'''for line in lines:
    linedic=eval(line)
    country=linedic['country'][0]
    #print ('insert "Countries" "'+country+' "[')
    #file1.write('insert "Countries" "'+country+' "[\n')
    for e_linedic in linedic.keys():
        if isinstance(linedic[e_linedic],dict):
            #print('contain '+e_linedic+':{"'+str(e_linedic)+' of '+country+'"[')
            #file1.write('contain '+e_linedic+':{"'+str(e_linedic)+' of '+country+'"[\n')
            for thirdlevel in linedic[e_linedic].keys():
                if isinstance(linedic[e_linedic][thirdlevel],list):
                    print ('insert "Countries" "'+country+' "[')
                    file1.write('insert "Countries" "'+country+' "[\n')
                    print('contain '+e_linedic+':{"'+str(e_linedic)+' of '+country+'"[')
                    file1.write('contain '+e_linedic+':{"'+str(e_linedic)+' of '+country+'"[\n')
                    print ('contain "'+thirdlevel+'":{"'+str(thirdlevel)+' of '+country+'"[@data:"'+str(linedic[e_linedic][thirdlevel]).replace('"',"'").replace("\n","").replace("\r","")+'"]}("'+str(e_linedic)+' of '+country+'")]}("'+country+'")');
                    file1.write('contain "'+thirdlevel+'":{"'+str(thirdlevel)+' of '+country+'"[@data:"'+str(linedic[e_linedic][thirdlevel]).replace('"',"'").replace("\n","").replace("\r","")+'"]}("'+str(e_linedic)+' of '+country+'")]}("'+country+'"),\n')
                    print('];')
                    file1.write('];\n')'''

# sub-class of type "dict" and 3rd-level "dict" , 4th-level "list"
for line in lines:
    linedic=eval(line)
    country=linedic['country'][0]
    for levelone in linedic.keys():
        if isinstance(linedic[levelone],dict):
            for leveltwo in linedic[levelone].keys():
                if isinstance(linedic[levelone][leveltwo],dict):
                    for levelthree in linedic[levelone][leveltwo].keys():
                        nameone=levelone;
                        nametwo=leveltwo;
                        namethree=levelthree;
                        #print(namethree); correct.
                        print('insert "Countries" "'+country+' "[')
                        file1.write('insert "Countries" "'+country+' "[\n')
                        print('     contain "'+nameone+'":{"'+str(nameone)+' of '+country+'"[')
                        file1.write('     contain "'+nameone+'":{"'+str(nameone)+' of '+country+'"[\n')
                        print('         contain "'+nametwo+'":{"'+str(nametwo)+' of '+country+'"[')
                        file1.write('         contain "'+nametwo+'":{"'+str(nametwo)+' of '+country+'"[\n')
                        print('             contain "'+namethree+'":{"'+str(namethree)+' of '+nametwo+" of "+country+'"[@data:"'+str(linedic[levelone][leveltwo][levelthree]).replace('"',"'").replace("\n","").replace("\r","")+'"]}("'+str(nametwo)+' of '+country+'")]')
                        file1.write('             contain "'+namethree+'":{"'+str(namethree)+' of '+nametwo+" of "+country+'"[@data:"'+str(linedic[levelone][leveltwo][levelthree]).replace('"',"'").replace("\n","").replace("\r","")+'"]}("'+str(nametwo)+' of '+country+'")]\n')
                        print('         }("'+str(nameone)+' of '+country+'")')
                        file1.write('         }("'+str(nameone)+' of '+country+'")\n')
                        print(']}("'+country+'")')
                        file1.write(']}("'+country+'")\n')
                        print('];')
                        file1.write('];\n')






#insert provinces
'''for line in lines:
    linedic=eval(line)
    country=linedic['country'][0]
    if 'province' in linedic:
        if len(linedic['province'][0])>0:
            provinces=linedic['province'][0]
            provincelist=provinces['province']
            for p in provincelist:
                print('insert "Countries" "'+country+'"[')
                file1.write('insert "Countries" "'+country+'"[\n')
                print ('contain "province":{"province of '+country+'"[@data:"'+str(p).rstrip()+'"]}("'+country+'")')
                file1.write('contain "province":{"province of '+country+'"[@data:"'+str(p).rstrip()+'"]}("'+country+'")\n')
                print ('];')
                file1.write('];\n')'''
'''for line in lines:
    linedic=eval(line)
    country=linedic['country'][0]
    if 'province' in linedic:
        if len(linedic['province'][0])>0:
            provinces=linedic['province'][0]
            provincelist=provinces['province']
            for p in provincelist:
                print('insert "Countries" "'+country+' "[')
                file1.write('insert "Countries" "'+country+' "[\n')
                print ('contain "province":{"Province '+ str(p).rstrip()+' of '+country+' "[@data:"'+str(p).rstrip()+'"]}("'+country+' ")')
                file1.write('contain "province":{"Province '+ str(p).rstrip()+' of '+country+' "[@data:"'+str(p).rstrip()+'"]}("'+country+' ")\n')
                print ('];')
                file1.write('];\n')'''

#for United States
'''linesprovince=fileprovince.readlines()
for line in linesprovince:
    provincedict=eval(line)
    if provincedict['country']=="United States of America":
        for p in provincedict['province']:
                print('insert "Countries" "UNITED STATES  "[')
                file1.write('insert "Countries" "UNITED STATES  "[\n')
                print ('contain "province":{"State '+ str(p).rstrip()+' of "UNITED STATES  "[@data:"'+str(p).rstrip()+'"]}("UNITED STATES  ")')
                file1.write('contain "province":{"State '+ str(p).rstrip()+' of UNITED STATES  "[@data:"'+str(p).rstrip()+'"]}("UNITED STATES  ")\n')
                print ('];')
                file1.write('];\n')'''


file1.close()

