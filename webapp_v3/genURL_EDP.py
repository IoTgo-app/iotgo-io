from code_components import input_code, output_else_code, output_code 
from code_components import package_suffix, input_sensorValue
from code_components import on_end, on_start  
import urllib.parse


def genURL_EDP(codeBody,io_list,codetitle,codesubtitle): # (groupnum,p2ptype,gamelevel,*args):#input_name, output_name):#here i am collecting chunks of code, encoding them, and concatenating them into a URL:
    # TO DO list
    # - remove clearscreen duplicates in output_else_code
    # 
    #----------prepare code chunks---------
    on_start_code=[]
    on_end_code=[]
    package_code=[]
    jscode=""
    for eachKey, eachValue in io_list.items():
        if eachValue in on_start:
            on_start_code.append(on_start[eachItem]+ '\n')
        if eachValue in on_end:
            on_end_code.append(on_end[eachItem]+ '\n')
        if eachValue in package_suffix:
            package_code.append(on_end[eachItem]+ '\n')
    #----------add on-start-code---------
    on_start_code_noDup= list( dict.fromkeys(on_start_code) )
    for eachline in on_start_code_noDup:
        jscode= jscode + eachline
    #-----------add body code---------
    jscode = jscode + codeBody
    # 
    # in future, codeBody can be generated here too
    # 
    #-----------add on_end_code---------
    on_end_code_noDup= list( dict.fromkeys(on_end_code) )
    for eachline in on_end_code_noDup:
        jscode= jscode + eachline 
    
    #------enclose jscode in URL:---    
    url='https://makecode.microbit.org/--docs?md='+codetitle+codesubtitle+'%0A%0A%60%60%60%20blocks%0A'
    for eachline in jscode:
        url=url+urllib.parse.quote(eachline) 
    url=url+'%0A%60%60%60%0A%0A'
    #-----------add-extensions-code---------
    package_code_noDup= list( dict.fromkeys(package_code) )
    #print(on_end_code_noDup)
    for eachline in package_code_noDup:
        url=url+eachline
    return url

