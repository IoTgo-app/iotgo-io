                #this file was updated on Sun Nov 14 20:22:54 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Amusic.setVolume%28255%29%0Aradio.setGroup%281%29%0Alet%20recieved%20%3D%200%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28pins.digitalReadPin%28DigitalPin.P0%29%20%3D%3D%200%29%7B%0A%20%20%20%20%20%20%20%20music.stopMelody%28MelodyStopOptions.All%29%0A%20basic.pause%281000%29%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20music.startMelody%28music.builtInMelody%28Melodies.Birthday%29%2C%20MelodyOptions.Forever%29%0Abasic.pause%281000%29%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28recieved%20%3D%3D%201%29%7B%0A%20%20%20%20%20%20%20%20music.stopMelody%28MelodyStopOptions.All%29%0A%20basic.pause%281000%29%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20music.startMelody%28music.builtInMelody%28Melodies.Birthday%29%2C%20MelodyOptions.Forever%29%0Abasic.pause%281000%29%0A%20%20%20%20%7D%0A%7D%29radio.onReceivedValue%28function%20%28name%2C%20value%29%20%7B%20%20%20%20%20%20%20%20if%20%28name%20%3D%3D%20%22pulsante%22%20%26%26%20value%20%3D%3D%201%29%20%7B%20%20%20%20%20%20%20%20%20%20%20%20recieved%20%3D%201%20%20%20%20%20%20%20%20%7D%20%20%20%20%7D%29%0A%0A%60%60%60%0A%0A"
cardWidth=130
pluscardwidht=130
missionCardWidth=160
vertiPaddingWidth=35


st.markdown(
        """
        <style type="text/css">
        iframe{
        top: 0;
        left: 0;
        width: 100%;
        max-width: 1200px;
        min-width: 900px;
        }
        </style>
        """,
          unsafe_allow_html=True,
)

st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 400px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 400px;
                margin-left: -400px;
        }
        </style>
        """,
        unsafe_allow_html=True,
)


st.sidebar.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo-hor.png",width=380)
input_col, plus_col, output_col, empty= st.sidebar.columns([1,1,1,1])
with input_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" se...")
	# ("Input1:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-MovementNotPresent.png", width=cardWidth)
	# ("Input2:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/ITrecieveData.png", width=cardWidth)
with plus_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
with output_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" allora...")
	# ("Output1:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-outputPhy-TurnOffMusic.png", width=cardWidth)
	# ("Output2:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-outputPhy-PlaySadMusic.png", width=cardWidth) 


st.subheader("")
st.markdown(
        """
        <style> .font{
        font-size:50px;}
        </style>
        """,
        unsafe_allow_html=True,
        )
st.code('''music.setVolume(255)
radio.setGroup(1)
let recieved = 0
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 0){
        music.stopMelody(MelodyStopOptions.All)
 basic.pause(1000)
    } else {
        music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)
basic.pause(1000)
    }
    if (recieved == 1){
        music.stopMelody(MelodyStopOptions.All)
 basic.pause(1000)
    } else {
        music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)
basic.pause(1000)
    }
})radio.onReceivedValue(function (name, value) {        if (name == "pulsante" && value == 1) {            recieved = 1        }    })
''',language="javascript")

st.subheader("")
components.iframe(urlis, height=1000, scrolling=True)    

e,edit  = st.columns([3,1])
with edit:
        #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
        st.markdown("[Modifica questa codice]("+urlis+")", unsafe_allow_html=True)

#st.button("Refresh")
