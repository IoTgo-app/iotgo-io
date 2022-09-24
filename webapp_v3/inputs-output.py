inputs_microbitv1= ("l\'accelerazione è alta" ,
		    "l\'accelerazione è basso" ,
		    "il pulsante non è premuto",
		    "il pulsante è premuto",
		    "la bussola punta ad Est",
		    "la bussola punta a Nord" ,
		    "la bussola punta a Sud" ,
		    "la bussola punta ad Ovest" ,
		    "il gesto è scuotere" ,
		    "il gesto è inclinare" ,
		    "l\'intensità di luce è alta",
		    'l\'intensità di luce è bassa',
		    'la temperatura è alta' ,
		    'la temperatura è bassa' ,
	
		   )
inputs_microbitv2= ( "il rumore è alto" ,
		    'il rumore è basso' ,
		    'il logo non è toccato', #v2 
		    'il logo è toccato' ,#v2 
		   )
inputs_exBosonKit= ('non c\'è movimento nei dintorni (BosonKit)' ,
'c\'è movimento nei dintorni (BosonKit)' ,
'il cursore è al massimo (BosonKit)' ,
'il cursore è al minimo (BosonKit)' ,
#"il cursore è al medio (BosonKit)" ,
		   )
inputs_exEnviroBit= ("c\'è tanta umidità (Envirobit)",
"c\'è poca umidità (Envirobit)",
"la pressione atmosferica è alta (Envirobit)",
"la pressione atmosferica è bassa (Envirobit)",
'il rumore è alto (Envirobit)' ,
'Il rumore è basso (Envirobit)' ,
"la temperatura è alta (Envirobit)" ,
"la temperatura è bassa (Envirobit)" ,
"l\'intensità di luce è alta (Envirobit)",
"l\'intensità di luce è bassa (Envirobit)",
"il colore  è rosso (Envirobit)",
"il colore  è verde (Envirobit)",
"il colore  è blu (Envirobit)",
"il colore  è nero (Envirobit)",
"c\'è un applauso (Envirobit)",
"non c’è un applauso (Envirobit)",
)

inputs_exCloudBitPi= ()

inputs_exOthers= ("l\'umidità del suolo è bassa",
"l\'umidità del suolo è alta",
)


inputs_p2p= ('recezione dati',)


outputs_microbitv1= ('suona una melodia allegra' ,
'smette di suonare' ,
'suona una melodia triste' ,
"suona un allarme" ,
'mostra un numero' ,
'smette di mostrare testi o numeri' ,
'mostra del testo' ,
'mostra un\'icona felice',
'smette di mostrare un\'icona',
'mostra un\'icona triste', 
		    )

outputs_microbitv2= ()


# outputs_exBosonKit= ('spegne un ventilatore (BosonKit)' ,
# 'accende un ventilatore (BosonKit)' ,
# 'spegne una luce (BosonKit)',
# 'accende una luce (BosonKit)',
# 'fa ruotare il motore (BosonKit)' ,
# 'smette di ruotare il motore (BosonKit)' ,
# 'spegne un\'animazione luminosa (BosonKit)',
# 'attiva un\'animazione luminosa (BosonKit)' ,
# 'spegne un\'animazione luminosa verde (BosonKit)',
# 'spegne un\'animazione luminosa rossa (BosonKit)',
# 		     )

outputs_exBosonKit= ('spegne un ventilatore (BosonKit)' ,
'accende un ventilatore (BosonKit)' ,
'spegne un\'animazione luminosa (BosonKit)',
'attiva un\'animazione luminosa (BosonKit)' ,
)


outputs_exEnviroBit=()
#"accende i LED bianchi (Envirobit)"
#"spegne i LED bianchi (Envirobit)"

outputs_exCloudBitPi= ()
outputs_exOthers= ()

outputs_p2p= ('invio dati',)	
