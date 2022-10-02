
textIT={ #this text will appear on the app in various places to guide the user
  "Select an example:"   : "Scegli un esempio:",
  "Select an output:"    : "Cambia un output:",
  "Select an input:"     : "Cambia un input:",
  "Select another output:"    : "Cambia un altro output:",
  "Select another input:"     : "Cambia un altro input:",##############
  "Select another example"      : "Scegli un altro esempio",
  "Edit this example"   : "Modifica questo esempio",#or Change input or ouput in this example #RG they are two different interactions
  "You have selected: "   : "Hai scelto: ",
  "Download this program"  : "Scarica il programma",#or Open this code in the editor
  }

exampleListIT= [ #these are the names of the example programs which users will select through a dropdown menu
    "1a1_toAddITdescription" ,#match the code i.e. "1a1" to the labelled taxonomy diagram
    "1a2_toAddITdescription" ,
    
    "1b1_toAddITdescription" ,
    "1b2_toAddITdescription" ,

    "1c1_toAddITdescription" ,
    "1c2_toAddITdescription" ,
    
    "2a1_toAddITdescription" ,
    "2a2_toAddITdescription" ,

    "2b1_toAddITdescription" ,
    "2b2_toAddITdescription" ,

    "2c1_toAddITdescription" ,
    "2c2_toAddITdescription" ,

    "3a1_toAddITdescription" ,
    "3a2_toAddITdescription" ,

    "3b1_toAddITdescription" ,
    "3b2_toAddITdescription"  
]


ITdescription2var= {#keys should contain the IT description needed to be shown in the app for each example.
    "1a1_toAddITdescription"  : "lvl1a1-1in_1out",
    "1a2_toAddITdescription"  : "lvl1a2-1in_1out_else",
    
    "1b1_toAddITdescription"  : "lvl1b1-1in_2out",
    "1b2_toAddITdescription"  : "lvl1b2-1in_2out_else",

    "1c1_toAddITdescription"  : "lvl1c1-2in_1out",
    "1c2_toAddITdescription"  : "lvl1c2-2in_1out_else",
    
    "2a1_toAddITdescription"  : "lvl2a1-1in_1out-1in_1out",
    "2a2_toAddITdescription"  : "lvl2a2-1in_1out_else-1in_1out_else",

    "2b1_toAddITdescription"  : "lvl2b1-1in_1out_elif_1in_1out",
    "2b2_toAddITdescription"  : "lvl2b2-1in_1out_elif_1in_1out_else",

    "2c1_toAddITdescription"  : "lvl2c1-1in_1out-nest-1in_1out",
    "2c2_toAddITdescription"  : "lvl2c2-1in_1out-nest-1in_1out_else_else",

    "3a1_toAddITdescription"  : "lvl3a1-1in_1out_var",
    "3a2_toAddITdescription"  : "lvl3a2-1in_1out_var_else",

    "3b1_toAddITdescription"  : "lvl3b1-1var_1out",
    "3b2_toAddITdescription"  : "lvl3b2-1var_1out_else"
}


it2en_inout={ #this is the text description of input, ouput cards.
  # NEW Cards to be added, 
  # if any new card is to be added, just add the text as a key, 
  # and put anything in the value, i will take care of the rest.
  # text can be revised of existing cards
  # Should match the description that on the printed cards
"il rumore è alto":"noiseHigh" ,
'il rumore è basso':"noiseLow" ,
'il logo è toccato':"touchYes" ,#v2 
'il logo non è toccato':"touchNo" , #v2 
"l\'accelerazione è alta":"accelHigh" ,
"l\'accelerazione è bassa":"accelLow" , #RG: fixed typo
"il pulsante è premuto":"buttonPress",
"il pulsante non è premuto":"buttonNotPress",
"la bussola punta ad Est":"compassE" ,
"la bussola punta a Nord":"compassN" ,
"la bussola punta a Sud":"compassS" ,
"la bussola punta ad Ovest":"compassW" ,
"il gesto è scuotere":"gestureShake" ,
"il gesto è inclinare":"gestureTilt" ,
"l\'intensità di luce è alta":"lightlevelHigh",
'l\'intensità di luce è bassa':"lightlevelLow",
'la temperatura è alta':"tempHigh" ,
'la temperatura è bassa':"tempLow" ,
'recezione dati' :"recieveData",
"c\'è tanta umidità (Envirobit)": "EB_humidityHigh",
"c\'è poca umidità (Envirobit)" : "EB_humidityLow",
"la pressione atmosferica è alta (Envirobit)" : "EB_pressureHigh",
"la pressione atmosferica è bassa (Envirobit)" : "EB_pressureLow",
'il rumore è alto (Envirobit)':"EB_noiseHigh" ,
'Il rumore è basso (Envirobit)':"EB_noiseLow" ,
"la temperatura è alta (Envirobit)":"EB_tempHigh" ,
"la temperatura è bassa (Envirobit)":"EB_tempLow" ,
"l\'intensità di luce è alta (Envirobit)":"EB_lightlevelHigh",
"l\'intensità di luce è bassa (Envirobit)":"EB_lightlevelLow",
"il colore  è rosso (Envirobit)": "EB_colorIsRed",
"il colore  è verde (Envirobit)": "EB_colorIsGreen",
"il colore  è blu (Envirobit)": "EB_colorIsBlue",
"il colore  è nero (Envirobit)": "EB_colorIsBlack",
"c\'è un applauso (Envirobit)": "EB_clapYes",
"non c’è un applauso (Envirobit)": "EB_clapNo",
'c\'è movimento nei dintorni (BosonKit)':"movementPresent" ,
'non c\'è movimento nei dintorni (BosonKit)':"movementNotPresent" ,
'il cursore è al massimo (BosonKit)':"sliderHigh" ,
'il cursore è al minimo (BosonKit)':"sliderLow" ,
"il cursore è a metà (BosonKit)":"sliderMid" , #RG: fixed another typo
'no Input':"noInput",
'suona una melodia allegra':"musicHappy" ,
'suona una melodia triste':"musicSad" ,
"suona un allarme":"musicAlarm" ,
'smette di suonare':"musicNone" ,
'mostra un numero':"displayInput" ,
'mostra del testo':"displayText" ,
'smette di mostrare testi o numeri':"displayNone" ,
'mostra un\'icona felice':"iconHappy",
'mostra un\'icona triste':"iconSad",
#RG: new cards: START
'mostra un\'icona grande':"iconBig",
'mostra un\'icona piccola':"iconSmall",
#RG: new cards: END
'smette di mostrare un\'icona':"iconNone",  
'invio dati' :"sendData",
"accende i LED bianchi (Envirobit)": "EB_whiteLEDon",
"spegne i LED bianchi (Envirobit)": "EB_whiteLEDoff",
'accende un ventilatore (BosonKit)':"fanOn" ,
'spegne un ventilatore (BosonKit)':"fanOff" ,
'accende una luce (BosonKit)':"lightOn",
'spegne una luce (BosonKit)':"lightOff",
'ruota il motore (BosonKit)':"rotateMax" , #RG: fixed another typo
'smette di ruotare il motore (BosonKit)':"rotateMin" ,
'attiva un\'animazione luminosa (BosonKit)':"showStripRainbow" ,
#'spegne un\'animazione luminosa verde (BosonKit)':"showStripGreen", #RG: they are removed from cards, because confusing
#'spegne un\'animazione luminosa rossa (BosonKit)':"showStripRed",   #RG: they are removed from cards, because confusing
'spegne un\'animazione luminosa (BosonKit)':"showStripBlack",
'no Output':"noOutput", 
"l\'umidità del suolo è alta":"soilMoistureHigh",#new
"l\'umidità del suolo è bassa":"soilMoistureLow",#new
}
