#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re 
import sys
import os,glob
import uuid
import zipfile  
import shutil  


path="./"
os.chdir(path)
shutil.rmtree('dist')  

os.mkdir('dist')
for filename in os.listdir("./30-seconds-of-code/snippets"):  
    file = open("./30-seconds-of-code/snippets/"+filename,'r',-1,"UTF-8") 
    i=1
    title=''
    keyword=''
    codeline=0
    titleline=3
    content=''
    end=0
    uuidstr=str(uuid.uuid1())
    for line in file.readlines():
        if i==1:
            keyword=line.replace("### ",'')
        if keyword=="anagrams\n":
            titleline=5
        if i==titleline:
            title=line
        if line=='```js\n' and codeline==0 and end==0:
            codeline=i
        if line=='```\n' and end==0 :
            end=1
        if end==0 and i>codeline and codeline>0:
            content+=line.replace('\n','\\n')
        i+=1

    output = open('./dist/'+keyword.replace("\n","")+'['+uuidstr+'].json', 'w+')
    output.write('{\n')
    output.write('    "alfredsnippet" : {\n' )
    output.write('        "keyword" : "' + keyword.replace("\n","") + '",\n')
    output.write('        "dontautoexpand" : true,\n' )
    output.write('        "name" : "' + title.replace("\n","") + '",\n')
    output.write('        "snippet": "' + content.replace("\n","").replace('"','\\"')+ '",\n') 
    output.write('        "uid": "' + uuidstr+ '"\n') 
    output.write('    }\n');
    output.write('}\n');
    output.close( )


z = zipfile.ZipFile("3sc.alfredsnippets", 'w') 
z.write("./icon.png")
path2="./dist"
os.chdir(path2)
testdir='.'
for d in os.listdir():  
    z.write(testdir+os.sep+d)  
z.close()