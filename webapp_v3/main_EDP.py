
import streamlit as st
import streamlit.components.v1 as components
import time
import textwrap
from bokeh.models.widgets import Div # for button-new-page
from code_skeletons import changeIO, code_skeletons,default_IO
import inputs_IT, outputs_IT
from translations_IT import it2en_inout, en2it_inout, descip2varIT, textIT, var2descipIT
from imageURL import imageURL
from genURL_EDP import genURL_EDP
import mods #for custom modifications to default streamlit app style

#################################################################################à
#apply custom modifications to default streamlit app style
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
st.markdown(mods.hide_menu_style, unsafe_allow_html=True)
st.markdown(mods.hide_img_fs, unsafe_allow_html=True)
st.markdown(mods.fix_sidebar, unsafe_allow_html=True)
st.markdown(mods.fix_tabs, unsafe_allow_html=True)
st.markdown(mods.hide_top_padding, unsafe_allow_html=True)

############################# app settings ##########################################à
langPrefix=['EN','IT','DE','UR']
lang=1
#baseURL                 =   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/images/cards_v2/"
baseURL_cards           =   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/cards/"
baseURL_codeSkeletons   =   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/"
baseURL_boards           =   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/cards/"
baseURL_codeChunks      =  "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/code/"
#https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/code/code_buttonNotPress.png
#https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/cards/rotateMax.png 
codetitle=""
codesubtitle=""
groupnum="0"
# p2p=True        #not implemented yet.
# appTabs=True    #not implemented yet.
codeLang="blocks" #or "js"

#populate input and output lists------------------------------------------
input_options=    inputs_IT.microbitv1_noCompass_noAccel  
                + inputs_IT.microbitv2  
                + inputs_IT.exOthers   
                + inputs_IT.exBosonKit 
                # + inputs_IT.exEnviroBit 
                # + inputs_IT.exCloudBitPi
                # + inputs_IT.p2p
                # + inputs_IT.microbitv1 


output_options=   outputs_IT.microbitv1 
                + outputs_IT.microbitv2 
                + outputs_IT.exBosonKit 
                + outputs_IT.microbitv1_negativeOutputs 
                + outputs_IT.microbitv2_negativeOutputs 
                + outputs_IT.exBosonKit_negativeOutputs  
                # + outputs_IT.exEnviroBit
                # + outputs_IT.exCloudBitPi
                # + outputs_IT.exOthers
                # + outputs_IT.p2p

#initialize session state variables----------------------------------------------------------
if 'sidebar_mode' not in st.session_state:
    st.session_state['sidebar_mode'] = "app_start"
    # st.session_state['sidebar_mode'] = "example_selected"
    # st.session_state['sidebar_mode'] = "editing_example"
if 'io_index' not in st.session_state:
    st.session_state['io_index'] = 0
if 'forward2' not in st.session_state:
    st.session_state['forward2'] = ""
if 'back2' not in st.session_state:
    st.session_state['back2']    = ""
if 'cardDeckOptions' not in st.session_state:
    st.session_state['cardDeckOptions'] = {}
if 'changingCardsNow' not in st.session_state:
    st.session_state['changingCardsNow'] = ""
if 'input0is' not in st.session_state:
    st.session_state['input0is'] = "no Input"
if 'prevInput' not in st.session_state:
    st.session_state['prevInput'] = "no Input"
if 'input1index' not in st.session_state:
    st.session_state['input1index'] = "0"
if 'output0is' not in st.session_state:
    st.session_state['output0is'] = "no Output"
if 'prevOutput' not in st.session_state:
    st.session_state['prevOutput'] = "no Output"
if 'input2is' not in st.session_state:
    st.session_state['input2is'] = "no Input"
if 'prevInput2' not in st.session_state:
    st.session_state['prevInput2'] = "no Input"
if 'output2is' not in st.session_state:
    st.session_state['output2is'] = "no Output"
if 'prevOutput2' not in st.session_state:
    st.session_state['prevOutput2'] = "no Output"
if 'skeleton' not in st.session_state:
    st.session_state['skeleton'] = ""
if 'skeletonIndex' not in st.session_state:
    st.session_state['skeletonIndex'] = 0
if 'io_list' not in st.session_state:
    if not st.session_state['skeleton']=="":
        st.session_state['io_list'] = default_IO[st.session_state['skeleton']]
    else:
        st.session_state['io_list'] = {"":""}
if 'urlis' not in st.session_state:
    st.session_state['urlis'] = ""
prevSkeleton="" ####MOVE TO SESSION STATE


#initialize image and iframe sizes-----------------------------------------------------------
cardWidth=150
#codeChunckWidth=250
pluscardwidht=150
missionCardWidth=160
vertiPaddingWidth=35
vertiPaddingWidthhalf=17
codeHeight=1500
codeWidth=800



########################### app init ########################################à
#add iotgo logo
st.sidebar.image("https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v3/images/logo_hor.png",width=250)
#st.sidebar.markdown("---")

#init placeholders for app content
select_placeholder      = st.sidebar.empty()
cardDeck_placeholder    = st.sidebar.container() #has selectBox with cards, image of the card, and code for that card
edit_placeholder        = st.sidebar.empty()
download_placeholder    = st.sidebar.empty()
st.sidebar.markdown("---")
nav_back, nav_fore = st.sidebar.columns(2)
with nav_back:
    st.container() 
with nav_fore:
    st.container() 
code_placeholder        = st.container()

########################### app sidebar ########################################à
with select_placeholder:
    if st.session_state['sidebar_mode']=="editing_example":
        st.write(textIT['youSelected'] + " \n *" +var2descipIT[st.session_state['skeleton']] + "*")
    elif st.session_state['sidebar_mode']=="app_start" or "example_selected":
        if not st.session_state['skeleton']=="":
            currIndex=list(var2descipIT.keys()).index((st.session_state['skeleton']))
        else:
            currIndex=0
        st.session_state['skeleton']=descip2varIT[st.selectbox(textIT['selectExample'],descip2varIT.keys(), index=currIndex)]#code_skeletons)
        # st.session_state['skeletonIndex']  = list(descip2varIT.keys()).index(en2it_inout[st.session_state['io_list']['in1']])
        if not st.session_state['skeleton']==prevSkeleton:
            prevSkeleton=st.session_state['skeleton']
            st.session_state['sidebar_mode']="example_selected"
            st.session_state['io_list']=default_IO[st.session_state['skeleton']]#new
            st.session_state['nav_list']=["app_start"] + list(st.session_state['io_list'].keys()) + ["download"] #new


def playTheCards(deckType, selectedCard,prevSelectedCard):     #"in1", st.session_state['input0is']  st.session_state['prevInput'] 
    if deckType == "in1": 
        options=input_options
        selectBoxText =textIT['selectInput1']
    elif deckType == "in2": 
        options=input_options
        selectBoxText =textIT['selectInput2']
    elif deckType == "out1": 
        options=output_options
        selectBoxText =textIT['selectOutput1']
    elif deckType == "out2": 
        options=output_options
        selectBoxText =textIT['selectOutput2']
    elif deckType == "out1else": 
        options=output_options
        selectBoxText =textIT['selectOutput1else']
    elif deckType == "out2else": 
        options=output_options
        selectBoxText =textIT['selectOutput2else']
    selectedCard = st.selectbox( selectBoxText,options, index= int(options.index(en2it_inout[st.session_state['io_list'][deckType]]))) 
    st.image(baseURL_cards      + it2en_inout[selectedCard]         +".png", width=cardWidth)  
    st.image(baseURL_codeChunks + "code_"+it2en_inout[selectedCard] +".png")
    if not prevSelectedCard == selectedCard:  
        prevSelectedCard = selectedCard
        temp=default_IO[st.session_state['skeleton']]
        temp[deckType]=it2en_inout[selectedCard]
        st.session_state['io_list']  = temp
        changeIO(st.session_state['skeleton'],st.session_state['io_list'])
        # st.experimental_rerun()      

with cardDeck_placeholder:
    if st.session_state['sidebar_mode']=="editing_example": 
        if st.session_state['nav_list'][st.session_state['io_index']+1] == "in1":
            playTheCards("in1", st.session_state['input0is'], st.session_state['prevInput']  )
        elif st.session_state['nav_list'][st.session_state['io_index']+1] == "in2":
            playTheCards("in2", st.session_state['input2is'], st.session_state['prevInput2']  )
        elif st.session_state['nav_list'][st.session_state['io_index']+1] == "out1":
            playTheCards("out1", st.session_state['output0is'], st.session_state['prevOutput']  )
        elif st.session_state['nav_list'][st.session_state['io_index']+1] == "out2":
            playTheCards("out2", st.session_state['output2is'], st.session_state['prevOutput2']  )
        elif st.session_state['nav_list'][st.session_state['io_index']+1] == "out1else":
            playTheCards("out1else", st.session_state['output0is'], st.session_state['prevOutput']  )
        elif st.session_state['nav_list'][st.session_state['io_index']+1] == "out2else":
            playTheCards("out2else", st.session_state['output2is'], st.session_state['prevOutput2']  ) 
        # to revert to automatic ouputElseCode:
        # in code_skeletons, revert default_IO
        # in code_components, revert output_else_code
        else:
            st.empty()
    else:
        st.empty()

        

with nav_back:
    if st.session_state['sidebar_mode']=="example_selected" or st.session_state['sidebar_mode']=="app_start":
        st.empty()
    elif st.session_state['sidebar_mode']=="editing_example":
        # st.markdown("---")
        isclick_nav_back = st.button(textIT['goBack'])
        if isclick_nav_back:
            st.session_state['io_index']=st.session_state['io_index']-1 
            if st.session_state['io_index']<=0:   
                st.session_state['sidebar_mode']="example_selected"  
                st.session_state['io_index']=0
                # change_placeholder.empty()
                nav_back.empty()
                nav_fore.empty()
            st.experimental_rerun()
    else:
        st.empty() 

with nav_fore:
    if st.session_state['sidebar_mode']=="example_selected" or st.session_state['sidebar_mode']=="app_start":
        st.empty()
    elif st.session_state['sidebar_mode']=="editing_example":
        if not st.session_state['nav_list'][st.session_state['io_index']+1]=='download':
            # st.markdown("---")
            isclick_nav_fore = st.button(textIT['goFront'])
            if isclick_nav_fore:
                st.session_state['io_index']=st.session_state['io_index']+1
                st.experimental_rerun()
    else:
        st.empty() 

with edit_placeholder:
    if st.session_state['sidebar_mode']=="example_selected":
        isClick=st.button(textIT['editExample'])
        if isClick:
            st.session_state['sidebar_mode'] = "editing_example"
            st.session_state['cardsList']    = st.session_state['io_list'].keys()
            st.session_state['deckNumber'] = 0
            edit_placeholder.empty()
            select_placeholder.empty()
            # st.balloons()
            st.experimental_rerun()
    else:
        st.empty()


########################### app body ########################################à
with code_placeholder:
    if st.session_state['sidebar_mode']=="app_start":
        st.empty()
    elif st.session_state['sidebar_mode']=="example_selected":
        if not  st.session_state['sidebar_mode']== "":
            st.image(baseURL_boards+st.session_state['skeleton'][3:6]+'cards.png')
        else:
            st.empty()
    elif st.session_state['sidebar_mode']=="editing_example":
        # st.image(baseURL_boards+st.session_state['skeleton'][3:6]+'cards.png')
        codeBodyis=changeIO(st.session_state['skeleton'],st.session_state['io_list'])
        st.session_state['urlis']=genURL_EDP(codeBodyis,st.session_state['io_list'],codetitle,codesubtitle)        
        if codeLang=="js":
            st.code(changeIO(st.session_state['skeleton'],st.session_state['io_list']), language="javascript")
        else:
            components.iframe(st.session_state['urlis'], height=codeHeight, width=codeWidth, scrolling=True)
        # st.markdown('[' + textIT['downloadProgram'] + '](' +st.session_state['urlis'] +')'  , unsafe_allow_html=True)


with download_placeholder:
    if st.session_state['sidebar_mode']=="app_start":
        st.empty()
    elif st.session_state['sidebar_mode']=="example_selected":
        st.empty()
    elif st.session_state['sidebar_mode']=="editing_example":
        if st.session_state['nav_list'][st.session_state['io_index']+1]=='download':
            st.markdown('[' + textIT['downloadProgram'] + '](' +st.session_state['urlis'] +')'  , unsafe_allow_html=True)
        #else:
         #   st.session_state['nav_list']
        # if st.button(textIT['downloadProgram']):            
        #     st.bokeh_chart( Div(text='<img src onerror="{}">'.format("window.open("+urlis+").focus()")))

########################### app end ########################################à
#st.sidebar.markdown("---")
st.write("version 8.0.3")
# st.session_state['io_index']
# st.session_state['sidebar_mode']


################################ old working
# with cardDeck_placeholder:
#     #TO DO: move repeating code to Func
#     if st.session_state['sidebar_mode']=="editing_example":
#         # if st.session_state['io_index'] == "in1":
#         if st.session_state['nav_list'][st.session_state['io_index']+1] == "in1":
#         # if "in1" in st.session_state['io_list'].keys():
#             st.session_state['input1index'] = input_options.index(en2it_inout[st.session_state['io_list']['in1']])
#             # st.session_state['input1index'] = input_options.index(en2it_inout[st.session_state['io_list']['in1']])
#             st.session_state['input0is'] =st.selectbox( textIT['selectInput1'],input_options,index= int(st.session_state['input1index']))#,index=2) #,key='selInput')
#             #st.image(baseURL_cards+langPrefix[lang]+imageURL[it2en_inout[st.session_state['input0is']]], width=cardWidth) 
#             st.image(baseURL_cards+it2en_inout[st.session_state['input0is']]+".png",                width=cardWidth)  
#             st.image(baseURL_codeChunks+"code_"+it2en_inout[st.session_state['input0is']]+".png")#,   width=codeChunckWidth) 
#             if not st.session_state['prevInput']==st.session_state['input0is']:  
#                 st.session_state['prevInput']=st.session_state['input0is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["in1"]=it2en_inout[st.session_state['input0is']]
#                 st.session_state['io_list']  = temp
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])            
#                 # st.session_state['changingCardsNow'] = "in1"
#                 st.experimental_rerun()
#         elif st.session_state['nav_list'][st.session_state['io_index']+1] == "in2":
#         # st.session_state['io_index'] == "in2":
#             # if "in2" in st.session_state['io_list'].keys():
#             st.session_state['input2index'] = input_options.index(en2it_inout[st.session_state['io_list']['in2']])
#             st.session_state['input2is'] =st.selectbox( textIT['selectInput2'],input_options,index= int(st.session_state['input2index']))#,index=2) #,key='selInput')
#             st.image(baseURL_cards+it2en_inout[st.session_state['input2is']]+".png",                width=cardWidth)  
#             st.image(baseURL_codeChunks+"code_"+it2en_inout[st.session_state['input2is']]+".png")#,   width=codeChunckWidth)             
#             if not st.session_state['prevInput2']==st.session_state['input2is']:  
#                 st.session_state['prevInput2']=st.session_state['input2is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["in2"]=it2en_inout[st.session_state['input2is']]
#                 st.session_state['io_list']  = temp
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])
#                 st.experimental_rerun()
#         elif st.session_state['nav_list'][st.session_state['io_index']+1] == "out1":
#             # if "out1" in st.session_state['io_list'].keys():
#             st.session_state['output1index'] = output_options.index(en2it_inout[st.session_state['io_list']['out1']])
#             st.session_state['output0is'] =st.selectbox( textIT['selectOutput1'],output_options,index= int(st.session_state['output1index']))#,key='selInput')
#             st.image(baseURL_cards+it2en_inout[st.session_state['output0is']]+".png",                width=cardWidth)  
#             st.image(baseURL_codeChunks+"code_"+it2en_inout[st.session_state['output0is']]+".png")#,   width=codeChunckWidth)             
#             if not st.session_state['prevOutput']==st.session_state['output0is']:
#                 st.session_state['prevOutput']=st.session_state['output0is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["out1"]=it2en_inout[st.session_state['output0is']]
#                 st.session_state['io_list']  = temp          
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])  
#                 st.experimental_rerun()
#         elif st.session_state['nav_list'][st.session_state['io_index']+1] == "out2":
#             # if "out2" in st.session_state['io_list'].keys():
#             st.session_state['output2index'] = output_options.index(en2it_inout[st.session_state['io_list']['out2']])
#             st.session_state['output2is'] =st.selectbox( textIT['selectOutput2'],output_options,index= int(st.session_state['output2index']))#,key='selInput')
#             st.image(baseURL_cards+it2en_inout[st.session_state['output2is']]+".png",                width=cardWidth)  
#             st.image(baseURL_codeChunks+"code_"+it2en_inout[st.session_state['output2is']]+".png")#,   width=codeChunckWidth)             
#             if not st.session_state['prevOutput2']==st.session_state['output2is']:
#                 st.session_state['prevOutput2']=st.session_state['output2is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["out2"]=it2en_inout[st.session_state['output2is']]
#                 st.session_state['io_list']  = temp          
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])  
#                 st.experimental_rerun()
#         else:
#             st.empty()
#     else:
#         st.empty()



######################################################
# app_start
# example_selected
# editing_example
# -back=app_start  fore=nextIO
# -back=prevIO     fore=nextIO
# -back=prevIO     fore=download
# download 


# st.session_state['nav_list'][int(st.session_state['io_index'])+1] == "in1":
# io_list.keys =  in1 in2 out1
# nav_list     = app_start in1 in2 out1 download
# nav_back     nav_list[io_index - 1]      
# nav_fore     nav_list[io_index + 2]
# io_index -> 0  1  2 
# nav_back -> 0  1  2 
# nav_fore -> 2  3  4 

###########################
# if st.session_state['deckNumber'] < len(st.session_state['io_list']):
#     # st.session_state['changingCardsNow'] = st.session_state['cardsList'][st.session_state['deckNumber'] ]
#     st.session_state['deckNumber']      = st.session_state['deckNumber'] + 1

# with change_placeholder:
#     if st.session_state['sidebar_mode']=="editing_example":
#         st.markdown("---")
#         isclick2 = change_placeholder.button(textIT['changeExample'])
#         if isclick2:
#             st.session_state['sidebar_mode']="app_start"
#             st.session_state['io_index']=0
#             change_placeholder.empty()
#             st.experimental_rerun()
#     else:
#         st.empty() 

######################################################

# with input_placeholder:
#     if st.session_state['sidebar_mode']=="editing_example":
#         if "in1" in st.session_state['io_list'].keys():
#             st.session_state['input1index'] = input_options.index(en2it_inout[st.session_state['io_list']['in1']])
#             st.session_state['input0is'] =st.selectbox( textIT['selectInput1'],input_options,index= int(st.session_state['input1index']))#,index=2) #,key='selInput')
#             if not st.session_state['prevInput']==st.session_state['input0is']:  
#                 st.session_state['prevInput']=st.session_state['input0is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["in1"]=it2en_inout[st.session_state['input0is']]
#                 st.session_state['io_list']  = temp
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])
#                 st.experimental_rerun()
#         else:
#             st.empty()
#     else:
#         st.empty()

# with input2_placeholder:
#     if st.session_state['sidebar_mode']=="editing_example":
#         if "in2" in st.session_state['io_list'].keys():
#             st.session_state['input2index'] = input_options.index(en2it_inout[st.session_state['io_list']['in2']])
#             st.session_state['input2is'] =st.selectbox( textIT['selectInput2'],input_options,index= int(st.session_state['input2index']))#,index=2) #,key='selInput')
#             if not st.session_state['prevInput2']==st.session_state['input2is']:  
#                 st.session_state['prevInput2']=st.session_state['input2is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["in2"]=it2en_inout[st.session_state['input2is']]
#                 st.session_state['io_list']  = temp
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])
#                 st.experimental_rerun()
#         else:
#             st.empty()
#     else:
#         st.empty()


# with output_placeholder:
#     if st.session_state['sidebar_mode']=="editing_example":
#         if "out1" in st.session_state['io_list'].keys():
#             st.session_state['output1index'] = output_options.index(en2it_inout[st.session_state['io_list']['out1']])
#             st.session_state['output0is'] =st.selectbox( textIT['selectOutput1'],output_options,index= int(st.session_state['output1index']))#,key='selInput')
#             if not st.session_state['prevOutput']==st.session_state['output0is']:
#                 st.session_state['prevOutput']=st.session_state['output0is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["out1"]=it2en_inout[st.session_state['output0is']]
#                 st.session_state['io_list']  = temp          
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])  
#                 st.experimental_rerun()
#         else:
#             st.empty()
#     else:
#         st.empty()


# with output2_placeholder:
#     if st.session_state['sidebar_mode']=="editing_example":
#         if "out2" in st.session_state['io_list'].keys():
#             st.session_state['output2index'] = output_options.index(en2it_inout[st.session_state['io_list']['out2']])
#             st.session_state['output2is'] =st.selectbox( textIT['selectOutput2'],output_options,index= int(st.session_state['output2index']))#,key='selInput')
#             if not st.session_state['prevOutput2']==st.session_state['output2is']:
#                 st.session_state['prevOutput2']=st.session_state['output2is']
#                 temp=default_IO[st.session_state['skeleton']]
#                 temp["out2"]=it2en_inout[st.session_state['output2is']]
#                 st.session_state['io_list']  = temp          
#                 changeIO(st.session_state['skeleton'],st.session_state['io_list'])  
#                 st.experimental_rerun()
#         else:
#             st.empty()
#     else:
#         st.empty()



# st.session_state 


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
