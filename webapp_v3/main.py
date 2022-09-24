
import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import time
import textwrap


import inputs_IT, outputs_IT
from translations_IT import it2en_inout
from imageURL import imageURL
#from code_components import input_code, output_else_code, output_code 
#from code_components import package_suffix, input_sensorValue
#from code_components import on_end, on_start  
from genURL import genURL
import mods #for custom modifications to default streamlit app style


#apply custom modifications to default streamlit app style
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
st.markdown(mods.hide_menu_style, unsafe_allow_html=True)
st.markdown(mods.hide_img_fs, unsafe_allow_html=True)
st.markdown(mods.fix_sidebar,unsafe_allow_html=True)



langPrefix=['EN','IT','DE','UR']
lang=1
baseURL=   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/images/cards_v2/"
codetitle=""
codesubtitle=""
groupnum="0"
p2p=True


#input_options=  ('no Input',) 
#output_options=  ('no Output',)
input_options=  ('no Input',) + inputs_IT.microbitv1 + inputs_IT.microbitv2 +inputs_IT.exOthers  
output_options=  ('no Output',) + outputs_IT.microbitv1 + outputs_IT.microbitv2+ outputs_IT.exBosonKit


input1="no Input"
output1="no Output"
input2="no Input"
output2="no Output"
gamelevel=0
def resetCards():
    gamelevel=0	 

########################### app sidebar ########################################à
#add iotgo logo
st.sidebar.image("https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/images/logotrans.png",width=300)
st.sidebar.markdown("""---""")

if p2p==True:
	p2ptype = st.sidebar.radio("Sono...",('invio dati', 'ricevo dati'),on_change=resetCards)
	if p2ptype=='invio dati':
		input1 = st.sidebar.selectbox('Seleziona la tua carta di input',input_options)
		output1= 'invio dati' 
	elif  p2ptype=='ricevo dati': #'ricevo dati'
		output1 = st.sidebar.selectbox('Seleziona la tua carta di output', output_options)
		input1='recezione dati'
	else:
		input1="no Input"
		output1="no Output"
		gamelevel=0

st.sidebar.markdown("""---""")		
secondLevel = st.sidebar.checkbox('Aggiungere un ulteriore livello di comunicazione')
if secondLevel==True:
	gamelevel=1
	if p2ptype=='invio dati':
		st.sidebar.write('Stavi inviando dati, ora riceviamo anche i dati:')
		output2 = st.sidebar.selectbox('Seleziona la tua carta di output ', output_options)
		input2='recezione dati'
	elif  p2ptype=='ricevo dati':  
		st.sidebar.write('Stavi ricevendo dati, ora inviamo anche i dati:')		
		input2 = st.sidebar.selectbox('Seleziona la tua carta di input ',input_options)
		output2= 'invio dati' 
	else:
		input2="no Input"
		output2="no Output"
 





input_name= ["no Input"  ,"no Input"  ,"no Input"]
output_name=["no Output" ,"no Output" ,"no Output"]


input_name[0]= it2en_inout[input1]
output_name[0]=it2en_inout[output1]
input_name[1]= it2en_inout[input2]
output_name[1]=it2en_inout[output2]



input0path=  baseURL+langPrefix[lang]+imageURL[ input_name[0]]
output0path= baseURL+langPrefix[lang]+imageURL[output_name[0]]
input1path=  baseURL+langPrefix[lang]+imageURL[ input_name[1]]
output1path= baseURL+langPrefix[lang]+imageURL[output_name[1]]
    
 



urlis=""
prevUrlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Abasic.pause%281000%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28true%29%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A"
jscode=""
if gamelevel==0:
	urlis,jscode=genURL(groupnum,p2ptype,[input_name[0],output_name[0]])
elif gamelevel==1:
	urlis,jscode=genURL(groupnum,p2ptype,[input_name[0],output_name[0]],[input_name[1],output_name[1]])
	



########################### app body ########################################à
cardWidth=150
pluscardwidht=150
missionCardWidth=160
vertiPaddingWidth=35
vertiPaddingWidthhalf=17



#input_col, plus_col, output_col, pad, code_col= st.columns([1,1,1,1,6])
input_col, plus_col, output_col, pad, code_col,pad2,= st.columns([1,1,1,1,1,2])
with input_col:    
	#st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" se...")
	# ("Input1:")
	st.image(input0path, width=cardWidth) 
	# ("Input2:")
	if gamelevel==1: st.image(input1path, width=cardWidth) 
with plus_col:    
	#st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidthhalf)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
	if gamelevel==1: st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 

with output_col:    
	#st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" allora...")
	# ("Output1:")
	st.image(output0path, width=cardWidth) 
	# ("Output1:")
	if gamelevel==1: st.image(output1path, width=cardWidth) 

if prevUrlis != urlis:
	with st.spinner('Plz wait. Generating code for you....'):
    		time.sleep(0.1)
	#st.success('Done!')
prevUrlis=urlis


e,edit  = st.columns([1,1])
with edit:
        #st.markdown("[Modifica...]("+urlis+")", unsafe_allow_html=True)
	st.write("[Modifica codice...]("+urlis+")")


components.iframe(urlis, height=1000, scrolling=True)   
#components.html(htmliframe, height=1000, scrolling=False)


########################### code warnings and suggestions ########################################à
warnings=0
externalWarning=False
radioGroupWarning=False
receiveDataWarning=False
#warnings:
if input_name[0]=="soilMoistureHigh" or input_name[0]=="soilMoistureLow" or  input_name[1]=="soilMoistureHigh" or input_name[1]=="soilMoistureLow":
    externalWarning=True
    warnings+=1
if secondLevel==True:
    radioGroupWarning=True
    warnings+=1
if p2ptype=="ricevo dati":
    receiveDataWarning=True
    warnings+=1

if warnings>0:
    with st.expander("\U000026A0 Attenzione ("+str(warnings)+")", expanded=True):
        if externalWarning==True:
            st.warning(':electric_plug: ricorda che il sensore di umidità del suolo è esterno. Deve essere fissato fisicamente al micro:bit.')
        if radioGroupWarning==True:
            st.warning(':mega: ricorda che il numero del gruppo deve corrispondere a quello dei tuoi amici con cui stai comunicando.')
        if receiveDataWarning==True:
            st.warning(':exclamation: ricorda che devi cambiare la parola "replace" nel tuo codice con quello che ti aspetti di ricevere dai tuoi amici')




 
########################### app footer ########################################à
st.markdown("""---""")
#st.write("Un progetto di / A project of:")
#st.image("https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/images/unilogo.png",width=600)
version="V3.0.0.1"

# st.write("IoTgo version "+version)
# # st.markdown("<h6 style='text-align: right; color: grey;'>By Mehdi Rizvi | "+version+"</h6>", unsafe_allow_html=True)

badges="""
![Version](https://img.shields.io/badge/IoTgo%20Version-"""+version+"""-orange) 
[![Mehdi Rizvi](https://img.shields.io/badge/Author-@rizMehdi-grey.svg?colorA=gray&colorB=dodgerblue&logo=github)](https://github.com/rizMehdi/)
"""
st.markdown(badges,  unsafe_allow_html=False)

 
