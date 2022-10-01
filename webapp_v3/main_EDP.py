
import streamlit as st
import streamlit.components.v1 as components
import time
import textwrap


import inputs_IT, outputs_IT
from translations_IT import it2en_inout
from imageURL import imageURL
from genURL import genURL
import mods #for custom modifications to default streamlit app style

#################################################################################à
#apply custom modifications to default streamlit app style
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
st.markdown(mods.hide_menu_style, unsafe_allow_html=True)
st.markdown(mods.hide_img_fs, unsafe_allow_html=True)
st.markdown(mods.fix_sidebar,unsafe_allow_html=True)
st.markdown(mods.fix_tabs, unsafe_allow_html=True)
st.markdown(mods.hide_top_padding, unsafe_allow_html=True)

############################# app settings ##########################################à
langPrefix=['EN','IT','DE','UR']
lang=1
baseURL=   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/images/cards_v2/"
baseURL_codeSkeletons=   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/"
codetitle=""
codesubtitle=""
groupnum="0"
p2p=True
appTabs=True
version="EDB.0.0.1"


########################### app sidebar ########################################à
#add iotgo logo-----------------------------------------------------------
st.sidebar.image("https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/images/logotrans.png",width=200)
st.sidebar.markdown("""---""")

#populate input and output lists------------------------------------------
input_options=  ('no Input',) + inputs_IT.microbitv1 + inputs_IT.microbitv2 +inputs_IT.exOthers  
output_options=  ('no Output',) + outputs_IT.microbitv1 + outputs_IT.microbitv2+ outputs_IT.exBosonKit

#initialize variables-----------------------------------------------------
input1="no Input"
output1="no Output"
input2="no Input"
output2="no Output"
gamelevel=0


def resetCards():
    gamelevel=0	 



# with sidebar_placeholder.container():
#     skeleton = sidebar_selectExample()

# container = st.container()

# sidebar_placeholder=st.sidebar.empty()
# sidebar_container=sidebar_placeholder.container()





# if p2p==True:
# 	p2ptype = st.sidebar.radio("Sono...",('invio dati', 'ricevo dati'),on_change=resetCards)
# 	if p2ptype=='invio dati':
# 		input1 = st.sidebar.selectbox('Seleziona la tua carta di input',input_options)
# 		output1= 'invio dati' 
# 	elif  p2ptype=='ricevo dati': #'ricevo dati'
# 		output1 = st.sidebar.selectbox('Seleziona la tua carta di output', output_options)
# 		input1='recezione dati'
# 	else:
# 		input1="no Input"
# 		output1="no Output"
# 		gamelevel=0

# st.sidebar.markdown("""---""")	
# secondLevel = st.sidebar.checkbox('Aggiungere un ulteriore livello di comunicazione')

# if secondLevel==True:
# 	gamelevel=1
# 	if p2ptype=='invio dati':
# 		st.sidebar.write('Stavi inviando dati, ora riceviamo anche i dati:')
# 		output2 = st.sidebar.selectbox('Seleziona la tua carta di output ', output_options)
# 		input2='recezione dati'
# 	elif  p2ptype=='ricevo dati':  
# 		st.sidebar.write('Stavi ricevendo dati, ora inviamo anche i dati:')		
# 		input2 = st.sidebar.selectbox('Seleziona la tua carta di input ',input_options)
# 		output2= 'invio dati' 
# 	else:
# 		input2="no Input"
# 		output2="no Output"
 
skeleton_list= ["",
                "lvl1-1con-1in-1out", 
                "lvl1-1con-1in-2out", 
                "lvl1-1con-2in-1out"]
io_changed=False

def updateCode():
    st.write("codeupdated")
    io_changed=False

# def sidebar_selectExample():
#     skeleton=st.sidebar.selectbox('Select an example',skeleton_list)
#     return skeleton

# def sidebar_editExample():
#     input0is=st.sidebar.selectbox('Select an input',['x','y'])
#     output0is=st.sidebar.selectbox('Select an output',['a','b'])
#     return input0is,output0is




prevSkeleton=""
skeleton=""
prevInput="x" # get default value for this skeleton
prevOutput="a" # get default value for this skeleton

if 'input0is' not in st.session_state:
    st.session_state['input0is'] = "x"
if 'prevInput' not in st.session_state:
    st.session_state['prevInput'] = "x"


if 'output0is' not in st.session_state:
    st.session_state['output0is'] = "a"
if 'skeleton' not in st.session_state:
    st.session_state['skeleton'] = ""
if 'sidebar_mode' not in st.session_state:
    st.session_state['sidebar_mode'] = "app_start"



########################### app body ########################################à

#initialize list of inputs and outputs------------------------------------------
input_name= ["no Input"  ,"no Input"]#  ,"no Input"]
output_name=["no Output" ,"no Output"]# ,"no Output"]

#initialize image sizes-----------------------------------------------------------
cardWidth=150
pluscardwidht=150
missionCardWidth=160
vertiPaddingWidth=35
vertiPaddingWidthhalf=17


# sidebar_mode        = "app_start" #"edit_example" #"app_start"
select_placeholder  = st.sidebar.container()#empty()
input_placeholder   = st.sidebar.container()#empty()
output_placeholder  = st.sidebar.container()#empty()
change_placeholder  = st.sidebar.container()#empty()

code_col, padding1  = st.columns([3,1])
with code_col:
    code_placeholder = st.empty()
edit_placeholder     = st.empty()

with select_placeholder:
    if st.session_state['sidebar_mode']=="editing_example":
        st.session_state['input0is'] =st.selectbox( 'Select an input',['x','y'])#,key='selInput')
        if not st.session_state['prevInput']==st.session_state['input0is']:
            st.session_state['sidebar_mode']="editing_example"
            st.session_state['prevInput']=st.session_state['input0is']
            st.balloons()
    if st.session_state['sidebar_mode']=="app_start" or "example_selected":
        st.session_state['skeleton']=st.selectbox('Select an example',skeleton_list)#, key='selector')        
        if not st.session_state['skeleton']==prevSkeleton:
            prevSkeleton=st.session_state['skeleton']
            st.session_state['sidebar_mode']="example_selected"
    
with edit_placeholder:
    if st.session_state['sidebar_mode']=="example_selected":
        isClick=st.button('Edit example')
        if isClick:
            st.session_state['sidebar_mode']="editing_example"
            edit_placeholder.empty()
            select_placeholder.empty()
            st.balloons()
    if st.session_state['sidebar_mode']=="app_start":
        st.empty()
    if st.session_state['sidebar_mode']=="editing_example":
        st.empty()


# with input_placeholder:
#     if st.session_state['sidebar_mode']=="app_start":
#         st.empty()
#     elif st.session_state['sidebar_mode']=="example_selected":
#         st.empty()
#     elif st.session_state['sidebar_mode']=="editing_example":
#         st.session_state['input0is'] =st.selectbox( 'Select an input',['x','y'])#,key='selInput')
#         if not st.session_state['prevInput']==st.session_state['input0is']:
#             st.session_state['sidebar_mode']="editing_example"
#             st.session_state['prevInput']=st.session_state['input0is']
#             st.balloons()

with change_placeholder:
    if st.session_state['sidebar_mode']=="app_start":
        st.empty()
    if st.session_state['sidebar_mode']=="example_selected":
        st.empty()
    if st.session_state['sidebar_mode']=="editing_example":
        isclick2 = change_placeholder.button('Select another example')
        if isclick2:
            st.session_state['sidebar_mode']="example_selected"
            change_placeholder.empty()

with code_placeholder:
    if st.session_state['sidebar_mode']=="app_start":
        st.empty()
    if st.session_state['sidebar_mode']=="example_selected":
        st.image(baseURL_codeSkeletons+str(st.session_state['skeleton'])+'.png')
    if st.session_state['sidebar_mode']=="editing_example":
        # st.image(baseURL_codeSkeletons+str(st.session_state['skeleton'])+'.png')
        st.write("editing this....")




st.sidebar.markdown("---")
st.sidebar.write("version 4.7 ")
st.session_state 


# if sidebar_mode=="app_start":
#     with select_placeholder:
#         st.session_state['skeleton']=st.selectbox('Select an example',skeleton_list)#, key='selector')        
#         if not st.session_state['skeleton']==prevSkeleton:
#             prevSkeleton=st.session_state['skeleton']
#             sidebar_mode="example_selected"
#     with input_placeholder:
#         st.empty()
#     


# if sidebar_mode=="example_selected":
#     code_placeholder.image(baseURL_codeSkeletons+str(st.session_state['skeleton'])+'.png')
#     isclick = edit_placeholder.button('Edit example')
#     if isclick:
#         sidebar_mode="editing_example"
#         # st.sidebar.write("Editing example: " + st.session_state['skeleton'])
#         edit_placeholder.empty()
#         with select_placeholder:
#             # st.empty()
#             st.write("Editing example: \n" + st.session_state['skeleton'])

# if sidebar_mode=="editing_example":
#     code_placeholder.image(baseURL_codeSkeletons+str(st.session_state['skeleton'])+'.png')
#     with input_placeholder:
#         # input0is=st.selectbox( 'Select an input',['x','y'],key='selInput')
#         st.session_state['input0is'] =st.selectbox( 'Select an input',['x','y'])#,key='selInput')
#         if not st.session_state['prevInput']==st.session_state['input0is']:
#             # io_changed=True
#             sidebar_mode="editing_example"
#             st.session_state['output0is']="caught"
#             st.session_state['prevInput']=st.session_state['input0is']
#             st.balloons()
#             st.write("code changed")
#     # with output_placeholder:
#         #     # output0is=st.selectbox('Select an output',['a','b'],key='selOutput')
#         #     st.session_state['output0is'] =st.selectbox('Select an output',['a','b'])#,key='selOutput')
#         #     if not prevOutput==st.session_state['Output0is']:
#         #         io_changed=True
#         #         prevOutput=st.session_state['output0is']
#         # if io_changed:
#             # st.write("code updated with "+st.session_state['input0is']+" and "+st.session_state['output0is'])
#         # st.balloons()
#                 # io_changed=False
#     # else:
#     #     st.sidebar.write("waiting for change")
#     isclick2 = change_placeholder.button('Select another example')
#     if isclick2:
#         sidebar_mode="example_selected"
#         change_placeholder.empty()
#         # input_placeholder.empty()
#         st.session_state['skeleton']=prevSkeleton


# st.sidebar.markdown("---")
# st.sidebar.write("Stats for mehdi: programState = "+st.session_state['sidebar_mode']+" \n- version 3.7 ")
# st.session_state



# if sidebar_mode=="app_start":
#     code_placeholder.write("")
# elif sidebar_mode=="example_selected":
#     code_placeholder.image(baseURL_codeSkeletons+str(st.session_state['skeleton'])+'.png')
#     # st.write(baseURL_codeSkeletons+str(skeleton)+'.png')
# elif sidebar_mode=="editing_example":
#     code_placeholder.image(baseURL_codeSkeletons+str(st.session_state['skeleton'])+'.png')
#     #st.write(baseURL_codeSkeletons+str(st.session_state['skeleton'])+'.png')
    # st.write("now we select inputs and outputs.")


# with st.form("my_form"):
#    st.write("Inside the form")
#    slider_val = st.slider("Form slider")
#    checkbox_val = st.checkbox("Form checkbox")
#    # Every form must have a submit button.
#    submitted = st.form_submit_button("Submit")
#    if submitted:
#        st.write("slider", slider_val, "checkbox", checkbox_val)

# st.write("Outside the form")





# back_btn_col, fore_btn_col = st.columns(2)
# with back_btn_col:
#     if sidebar_mode=="edit_example":
#         if st.button('⬅ Cambia esempio'):
#             sidebar_mode="select_example"
#             with sidebar_placeholder2:
#                 st.sidebar.empty()#NOT WORKING
            
#     else:
#         st.empty()



# # fore_btn_placeholder=st.empty()
# # with fore_btn_col:
# #     forebtnClicked=fore_btn_placeholder.button('➡ Cambia input oppure output')
# #     if sidebar_mode=="select_example":
# #         if forebtnClicked:
# #             sidebar_mode="edit_example"
# #             with sidebar_placeholder2:
# #                 input0is=st.sidebar.selectbox( 'Select an input',['x','y'])
# #                 output0is=st.sidebar.selectbox('Select an output',['a','b'])
# #                 if prevInput != input0is or prevOutput != ouput0is:
# #                     io_changed=True
# #                     updateCode()
# #                     prevInput=input0is
# #                     prevOutput=output0is
# #     else:
# #         fore_btn_placeholder.empty() #NOT WORKING#NOT WORKING, use PLACEHOLDERS?
# #         st.write("should be no edit button")

# with fore_btn_col:
#     if sidebar_mode=="select_example":
#         if st.button('➡ Cambia input oppure output'):
#             sidebar_mode="edit_example"
#             with sidebar_placeholder2:
#                 input0is=st.sidebar.selectbox( 'Select an input',['x','y'])
#                 output0is=st.sidebar.selectbox('Select an output',['a','b'])
#                 if prevInput != input0is or prevOutput != ouput0is:
#                     io_changed=True
#                     updateCode()
#                     prevInput=input0is
#                     prevOutput=output0is
#     else:
#         st.empty() #NOT WORKING#NOT WORKING, use PLACEHOLDERS?
#         sidebar_mode="app_start"





# #translate ITalian input output names to base ENglish variable names------------
# input_name[0]= it2en_inout[input1]
# output_name[0]=it2en_inout[output1]
# input_name[1]= it2en_inout[input2]
# output_name[1]=it2en_inout[output2]


# #build image URLs for cards-----------------------------------------------------
# inputcard0path=  baseURL+langPrefix[lang]+imageURL[ input_name[0]]
# outputcard0path= baseURL+langPrefix[lang]+imageURL[output_name[0]]
# inputcard1path=  baseURL+langPrefix[lang]+imageURL[ input_name[1]]
# outputcard1path= baseURL+langPrefix[lang]+imageURL[output_name[1]]
    

# # generate code and code URL----------------------------------------------------
# urlis=""
# prevUrlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Abasic.pause%281000%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28true%29%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A"
# jscode=""
# if gamelevel==0:
# 	urlis,jscode=genURL(groupnum,p2ptype,gamelevel,codetitle,codesubtitle,[input_name[0],output_name[0]])
# elif gamelevel==1:
# 	urlis,jscode=genURL(groupnum,p2ptype,gamelevel,codetitle,codesubtitle,[input_name[0],output_name[0]],[input_name[1],output_name[1]])
	


# def showCards():
#     # show cards------------------------------------------
#     input_col, plus_col, output_col, pad, code_col,pad2,= st.columns([1,1,1,1,1,2])
#     #input_col, plus_col, output_col, pad, code_col= st.columns([1,1,1,1,6])
#     with input_col:    
#         st.write(" se...")
#         # ("Input1:")
#         st.image(inputcard0path, width=cardWidth) 
#         # ("Input2:")
#         if gamelevel==1: st.image(inputcard1path, width=cardWidth) 
#     with plus_col:    
#         st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidthhalf)
#         st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
#         if gamelevel==1: st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 

#     with output_col:    
#         st.write(" allora...")
#         # ("Output1:")
#         st.image(outputcard0path, width=cardWidth) 
#         # ("Output1:")
#         if gamelevel==1: st.image(outputcard1path, width=cardWidth) 




# def showBlockCode(prevUrlis,urlis):
#     # show block code------------------------------------------
#     if prevUrlis != urlis:
#         with st.spinner('Plz wait. Generating code for you....'):
#                 time.sleep(0.1)
#     prevUrlis=urlis
#     e,edit  = st.columns([1,1])
#     with edit:
#             #st.markdown("[Modifica...]("+urlis+")", unsafe_allow_html=True)
#         st.write("[Modifica codice...]("+urlis+")")
#     components.iframe(urlis, height=1000, scrolling=True)



# #def showPythonCode():
#     # show Python code------------------------------------------
#     #components.html(htmliframe, height=1000, scrolling=False)


# def showSuggestions():
#     # show code warnings and suggestions------------------------- 
#     warnings=0
#     externalWarning=False
#     radioGroupWarning=False
#     receiveDataWarning=False
#     #warnings:
#     if input_name[0]=="soilMoistureHigh" or input_name[0]=="soilMoistureLow" or  input_name[1]=="soilMoistureHigh" or input_name[1]=="soilMoistureLow":
#         externalWarning=True
#         warnings+=1
#     if secondLevel==True:
#         radioGroupWarning=True
#         warnings+=1
#     if p2ptype=="ricevo dati":
#         receiveDataWarning=True
#         warnings+=1

#     if warnings>0:
#         with st.expander("\U000026A0 Attenzione ("+str(warnings)+")", expanded=True):
#             if externalWarning==True:
#                 st.warning(':electric_plug: ricorda che il sensore di umidità del suolo è esterno. Deve essere fissato fisicamente al micro:bit.')
#             if radioGroupWarning==True:
#                 st.warning(':mega: ricorda che il numero del gruppo deve corrispondere a quello dei tuoi amici con cui stai comunicando.')
#             if receiveDataWarning==True:
#                 st.warning(':exclamation: ricorda che devi cambiare la parola "replace" nel tuo codice con quello che ti aspetti di ricevere dai tuoi amici')
#     else:
#         st.write('Nessun suggerimento disponibile al momento.')


# if appTabs==True:
#     tab1, tab2, tab3 = st.tabs(["🡳 Le tue carte.    ",
#                              "   🡳 Il tuo codice.   ",
#                              "   🡳 Suggerimenti.    "])
#     with tab1:
#         showCards()
#     with tab2:
#         showBlockCode(prevUrlis,urlis)
#     with tab3:
#         showSuggestions()
# else:
#     showCards()
#     showBlockCode(prevUrlis,urlis)
#     showSuggestions()




########################### app footer ########################################à

# st.sidebar.markdown("""---""")
# #st.write("Un progetto di / A project of:")
# #st.image("https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/images/unilogo.png",width=600)


# # st.write("IoTgo version "+version)
# # # st.markdown("<h6 style='text-align: right; color: grey;'>By Mehdi Rizvi | "+version+"</h6>", unsafe_allow_html=True)

# badges="""
# ![Version](https://img.shields.io/badge/IoTgo%20Version-"""+version+"""-orange) 
# [![Mehdi Rizvi](https://img.shields.io/badge/Author-@rizMehdi-grey.svg?colorA=gray&colorB=dodgerblue&logo=github)](https://github.com/rizMehdi/)
# """
# st.sidebar.markdown(badges,  unsafe_allow_html=False)
# st.sidebar.markdown("""---""")
 
