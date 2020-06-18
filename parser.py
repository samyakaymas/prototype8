import os
import re
dir_path =os.path.join(os.path.join(os.getcwd(),"files"))
dictionary={}
for filename in os.listdir(dir_path):
    ques=[]
    ans=[]
    file = open(os.path.join(dir_path,filename))
    s=file.read()
    intervalsQues=[m for m in re.finditer('qUeS',s)]
    for i in range(0,len(intervalsQues)-1,2):
        ques.append(s[intervalsQues[i].end():(intervalsQues[i+1].start()-1)])
    intervalsAns=[m for m in re.finditer('aNs',s)]
    for i in range(0,len(intervalsAns)-1,2):
        ans.append(s[intervalsAns[i].end():(intervalsAns[i+1].start()-1)])
    pair={}
    pair["ques"]=ques
    pair["ans"]=ans
    dictionary[filename]=pair
for name in dictionary:
    for i in range(len(dictionary[name]["ques"])):
        print('ques1=QuesTag(chapter=Chapter.objects.get(name=\"{name}\"),ques=\"\"\"{ques}\n\"\"\",ans=\"\"\"{ans}\n\"\"\")\nques1.save()\n'.format(name=name,ques=dictionary[name]["ques"][i],ans=dictionary[name]["ans"][i]))

