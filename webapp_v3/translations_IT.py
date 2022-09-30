
textIT={ #this text will appear on the app in various places to guide the user
  "Select an example:"   : "Select an example: (in italian)",
  "Select an output:"    : "Select an output: (in italian)",
  "Select an input:"     : "Select an input: (in italian)",
  "Change example"      : "Change example: (in italian)",#or select another example
  "Edit this example"   : "Edit this example: (in italian)",
  "You have selected:"   : "You have selected: (in italian)",
  "Download this code"  : "Download this code: (in italian)",
  }

exampleListIT= [ #these are the names of the examples code which user will select through a dropdown menu
    "1a1_toAddITdescription" ,#for the code i.e. "1a1" refer to the labelled taxonomy diagram
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


it2en_inout={ #this is the text description of input, ouput cards.
  # NEW Cards to be added, 
  # if any new card is to be added, just add the text as a key, 
  # and put anything in the value, i will take care of the rest.
  # text can be revised of existing cards
  # Should match the description that on the printed cards
"il rumore è alto":"noiseHigh" ,
'il rumore è basso':"noiseLow" ,
'il logo non è toccato':"touchNo" , #v2 
'il logo è toccato':"touchYes" ,#v2 
"l\'accelerazione è alta":"accelHigh" ,
"l\'accelerazione è basso":"accelLow" ,
"il pulsante non è premuto":"buttonNotPress",
"il pulsante è premuto":"buttonPress",
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
'non c\'è movimento nei dintorni (BosonKit)':"movementNotPresent" ,
'c\'è movimento nei dintorni (BosonKit)':"movementPresent" ,
'il cursore è al massimo (BosonKit)':"sliderHigh" ,
'il cursore è al minimo (BosonKit)':"sliderLow" ,
"il cursore è al medio (BosonKit)":"sliderMid" ,
'no Input':"noInput",
'suona una melodia allegra':"musicHappy" ,
'smette di suonare':"musicNone" ,
'suona una melodia triste':"musicSad" ,
"suona un allarme":"musicAlarm" ,
'mostra un numero':"displayInput" ,
'smette di mostrare testi o numeri':"displayNone" ,
'mostra del testo':"displayText" ,
'mostra un\'icona felice':"iconHappy",
'smette di mostrare un\'icona':"iconNone",
'mostra un\'icona triste':"iconSad",
'invio dati' :"sendData",
"accende i LED bianchi (Envirobit)": "EB_whiteLEDon",
"spegne i LED bianchi (Envirobit)": "EB_whiteLEDoff",
'spegne un ventilatore (BosonKit)':"fanOff" ,
'accende un ventilatore (BosonKit)':"fanOn" ,
'spegne una luce (BosonKit)':"lightOff",
'accende una luce (BosonKit)':"lightOn",
'fa ruotare il motore (BosonKit)':"rotateMax" ,
'smette di ruotare il motore (BosonKit)':"rotateMin" ,
'spegne un\'animazione luminosa (BosonKit)':"showStripBlack",
'attiva un\'animazione luminosa (BosonKit)':"showStripRainbow" ,
'spegne un\'animazione luminosa verde (BosonKit)':"showStripGreen",
'spegne un\'animazione luminosa rossa (BosonKit)':"showStripRed",
'no Output':"noOutput", 
"l\'umidità del suolo è bassa":"soilMoistureLow",#new
"l\'umidità del suolo è alta":"soilMoistureHigh",#new
}
