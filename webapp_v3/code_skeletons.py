
from code_components import input_code,output_code,output_else_code
from code_components import package_suffix,on_end,on_start,input_sensorValue


default_IO = {
    "":{},
    "lvl1a1-1in_1out"                   :{"in1":"buttonPress","out1":"iconHappy"},
    "lvl1a2-1in_1out_else"              :{"in1":"buttonPress","out1":"iconHappy","out1else":"iconHappy"},
    "lvl1b1-1in_2out"                   :{"in1":"buttonPress","out1":"iconHappy","out2":"iconSad"},
    "lvl1b2-1in_2out_else"              :{"in1":"buttonPress","out1":"iconHappy","out2":"iconSad","out1else":"iconHappy","out2else":"iconSad"},
    "lvl1c1-2in_1out"                   :{"in1":"buttonPress","in2":"tempLow","out1":"iconSad"},
    "lvl1c2-2in_1out_else"              :{"in1":"buttonPress","in2":"tempLow","out1":"iconSad","out1else":"iconSad"},
    "lvl2a1-1in_1out-1in_1out"          :{"in1":"buttonPress","out1":"iconHappy","in2":"buttonPressB","out2":"musicHappy"},
    "lvl2a2-1in_1out_else-1in_1out_else":{"in1":"buttonPress","out1":"iconHappy","in2":"buttonPressB","out2":"musicHappy","out1else":"iconHappy","out2else":"musicHappy"},
    "lvl2b1-1in_1out_elif_1in_1out"     :{"in1":"buttonPress","out1":"iconHappy","in2":"buttonPressB","out2":"musicHappy"},
    "lvl2b2-1in_1out_elif_1in_1out_else":{"in1":"buttonPress","out1":"iconHappy","in2":"buttonPressB","out2":"musicHappy","out1else":"iconHappy","out2else":"musicHappy"},
    "lvl2c1-1in_1out-nest-1in_1out"     :{"in1":"buttonPress","out1":"iconHappy","in2":"buttonPressB","out2":"musicHappy"},
    "lvl2c2-1in_1out-nest-1in_1out_else_else":{"in1":"buttonPress","out1":"iconHappy","in2":"buttonPressB","out2":"musicHappy","out1else":"iconHappy","out2else":"musicHappy"},
    "lvl3a1-1in_1out_var"               :{"in1":"buttonPress","out1":"displayInput"},####TOASK 
    "lvl3a2-1in_1out_var_else"          :{"in1":"buttonPress","out1":"displayInput","out1else":"displayInput"},####TOASK
    "lvl3b1-1var_1out"                  :{"out1":"musicHappy"},####TOASK
    "lvl3b2-1var_1out_else"             :{"out1":"musicHappy","out1else":"musicHappy"}####TOASK
}



code_skeletons = {
    "":"",
    "lvl1a1-1in_1out" : 
        """
        /**
        * CESTINO SORRIDENTE
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
            }
        })
        """, 
    "lvl1b1-1in_2out" : 
        """
        /**
        * ALBERO ANIMATO
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
                _out2_
            }
        })
        """, 
    "lvl1c1-2in_1out" : 
        """
        /**
        * OROLOGIO SEGNAFREDDO
        */
        basic.forever(function () {
            if (_in1_ && _in2_) {
                _out1_
            }
        })
        """, 
    "lvl2a1-1in_1out-1in_1out" : 
        """
                /**
        * TAVOLO GIOCO X 2, FACCINA E MUSICA
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_            }
            if (_in2_) {
                _out2_            }
        })
        """, 
    "lvl2b1-1in_1out_elif_1in_1out" : 
        """
                /**
        * CAVALLO SFIDA X 2, O  FACCINA O MUSICA
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
            } else if (_in2_) {
                _out2_
            }
        })
        """, 
    "lvl2c1-1in_1out-nest-1in_1out" : 
        """
        /**
        * PANCHINA x DUE., CON FACCINA E POI MUSICALE
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
                if (_in2_) {
                _out2_
                }
            }
        })
        """, 
    "lvl3a1-1in_1out_var" : 
        """
                /**
        * IL CANESTRO MOSTRA-PUNTEGGIO
        */
        basic.forever(function () {
            if (_in1_) {
                conto += 1
                _out1_
            }
        })
        """, 
    "lvl3b1-1var_1out" : 
        """
        /**
        * IL DADO MUSICALE
        */
        basic.clearScreen()
        let valore_caratteristico = 0
        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            if (valore_caratteristico % 2 == 0) {
                _out1_
            }
        })
        """, 





    "lvl1a2-1in_1out_else" : 
        """
        /**
        * ALBERO ANIMATO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
            } else {
                _out1else_
            }
        })
        """, 
    "lvl1b2-1in_2out_else" : 
        """
        /**
        * CESTINO SORRIDENTE, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
                _out2_
            } else {
                _out1else_
                _out2else_
            }
        }) 
        """, 
    "lvl1c2-2in_1out_else" : 
        """
                /**
        * OROLOGIO SEGNAFREDDO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (_in1_ && _in2_) {
                _out1_
            } else {
                _out1else_
            }
        })
        """, 
    "lvl2a2-1in_1out_else-1in_1out_else" : 
        """
        /**
        * TAVOLO GIOCO X 2, FACCINA E MUSICA, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
            } else {
                _out1else_
            }
            if (_in2_) {
                _out2_
            } else {
                _out2else_
            }
        })
        """, 
    "lvl2b2-1in_1out_elif_1in_1out_else" : 
        """
        /**
        * CAVALLO SFIDA X 2, O  FACCINA O MUSICA, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
            } else if (_in2_) {
                _out2_
            } else {
                _out1else_
                _out2else_
            }
        })
        """, 
    "lvl2c2-1in_1out-nest-1in_1out_else_else" : 
        """
        /**
        * PANCHINA x DUE., CON FACCINA E POI MUSICALE, ALTRIMENTI SPENTA
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
                if (_in2_) {
                    _out2_
                } else {
                    _out2else_
                }
            } else {
                _out1else_
            }
        })
        """, 
    "lvl3a2-1in_1out_var_else" : 
        """
        /**
        * IL CANESTRO MOSTRA-PUNTEGGIO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (_in1_) {
                conto += 1
                _out1_
            } else {
                _out1else_
            }
        })
        """, 
    "lvl3b2-1var_1out_else" : 
        """   
        /**
        * IL DADO MUSICALE, ALTRIMENTI SPENTO
        */
        basic.clearScreen()
        let valore_caratteristico = 0

        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            if (valore_caratteristico % 2 == 0) {
                _out1_
            } else {
                _out1else_
            }
        })
        """
}




def changeIO(skeleton_name,IO2change):
    currentSkeleton=code_skeletons[skeleton_name]
    for eachKey, eachVal in IO2change.items():
        if eachKey=="in1":
            currentSkeleton=currentSkeleton.replace("_"+eachKey+"_", input_code[eachVal])
        if eachKey=="in2":
            currentSkeleton=currentSkeleton.replace("_"+eachKey+"_", input_code[eachVal])
        if eachKey=="out1":
            currentSkeleton=currentSkeleton.replace("_"+eachKey+"_", output_code[eachVal])
        if eachKey=="out2":
            currentSkeleton=currentSkeleton.replace("_"+eachKey+"_", output_code[eachVal])
        if eachKey=="out1else":
            currentSkeleton=currentSkeleton.replace("_"+eachKey+"_", output_else_code[eachVal]) 
        if eachKey=="out2else":
            currentSkeleton=currentSkeleton.replace("_"+eachKey+"_", output_else_code[eachVal])
    return currentSkeleton




# code_examples = {
#     "lvl1a1-1in_1out" : 
#         """
#         /**
#         * CESTINO SORRIDENTE
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#             }
#         })
#         """, 
#     "lvl1b1-1in_2out" : 
#         """
#         /**
#         * ALBERO ANIMATO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Heart)
#                 basic.showIcon(IconNames.SmallHeart)
#             }
#         })
#         """, 
#     "lvl1c1-2in_1out" : 
#         """
#         /**
#         * OROLOGIO SEGNAFREDDO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A) && input.temperature() < 10) {
#                 basic.showIcon(IconNames.Sad)
#             }
#         })
#         """, 
#     "lvl2a1-1in_1out-1in_1out" : 
#         """
#                 /**
#         * TAVOLO GIOCO X 2, FACCINA E MUSICA
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#             }
#             if (input.buttonIsPressed(Button.B)) {
#                 music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#             }
#         })
#         """, 
#     "lvl2b1-1in_1out_elif_1in_1out" : 
#         """
#                 /**
#         * CAVALLO SFIDA X 2, O  FACCINA O MUSICA
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#             } else if (input.buttonIsPressed(Button.B)) {
#                 music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#             }
#         })
#         """, 
#     "lvl2c1-1in_1out-nest-1in_1out" : 
#         """
#         /**
#         * PANCHINA x DUE., CON FACCINA E POI MUSICALE
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#                 if (input.buttonIsPressed(Button.B)) {
#                     music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#                 }
#             }
#         })
#         """, 
#     "lvl3a1-1in_1out_var" : 
#         """
#                 /**
#         * IL CANESTRO MOSTRA-PUNTEGGIO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 conto += 1
#                 basic.showString("" + (conto))
#             }
#         })
#         """, 
#     "lvl3b1-1var_1out" : 
#         """
#         /**
#         * IL DADO MUSICALE
#         */
#         basic.clearScreen()
#         let conto = 0
#         let valore_caratteristico = 0
#         basic.forever(function () {
#             basic.pause(2000)
#             valore_caratteristico += randint(1, 6)
#             basic.showNumber(valore_caratteristico)
#             if (valore_caratteristico % 2 == 0) {
#                 music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#             }
#         })
#         """, 
#     "lvl1a2-1in_1out_else" : 
#         """
#         /**
#         * ALBERO ANIMATO, ALTRIMENTI SPENTO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Heart)
#                 basic.showIcon(IconNames.SmallHeart)
#             } else {
#                 basic.clearScreen()
#             }
#         })
#         """, 
#     "lvl1b1-1in_2out_else" : 
#         """
#         /**
#         * CESTINO SORRIDENTE, ALTRIMENTI SPENTO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#             } else {
#                 basic.clearScreen()
#             }
#         }) 
#         """, 
#     "lvl1c2-2in_1out_else" : 
#         """
#                 /**
#         * OROLOGIO SEGNAFREDDO, ALTRIMENTI SPENTO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A) && input.temperature() < 10) {
#                 basic.showIcon(IconNames.Sad)
#             } else {
#                 basic.clearScreen()
#             }
#         })
#         """, 
#     "lvl2a2-1in_1out_else-1in_1out_else" : 
#         """
#         /**
#         * TAVOLO GIOCO X 2, FACCINA E MUSICA, ALTRIMENTI SPENTO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#             } else {
#                 basic.clearScreen()
#             }
#             if (input.buttonIsPressed(Button.B)) {
#                 music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#             } else {
#                 music.stopAllSounds()
#             }
#         })
#         """, 
#     "lvl2b2-1in_1out_elif_1in_1out_else" : 
#         """
#         /**
#         * CAVALLO SFIDA X 2, O  FACCINA O MUSICA, ALTRIMENTI SPENTO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#             } else if (input.buttonIsPressed(Button.B)) {
#                 music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#             } else {
#                 basic.clearScreen()
#                 music.stopAllSounds()
#             }
#         })
#         """, 
#     "lvl2c2-1in_1out-nest-1in_1out_else_else" : 
#         """
#         /**
#         * PANCHINA x DUE., CON FACCINA E POI MUSICALE, ALTRIMENTI SPENTA
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 basic.showIcon(IconNames.Happy)
#                 if (input.buttonIsPressed(Button.B)) {
#                     music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#                 } else {
#                     music.stopAllSounds()
#                 }
#             } else {
#                 basic.clearScreen()
#             }
#         })
#         """, 
#     "lvl3a2-1in_1out_var_else" : 
#         """
#         /**
#         * IL CANESTRO MOSTRA-PUNTEGGIO, ALTRIMENTI SPENTO
#         */
#         basic.forever(function () {
#             if (input.buttonIsPressed(Button.A)) {
#                 conto += 1
#                 basic.showString("" + (conto))
#             } else {
#                 basic.clearScreen()
#             }
#         })
#         """, 
#     "lvl3b2-1var_1out_else" : 
#         """   
#         /**
#         * IL DADO MUSICALE, ALTRIMENTI SPENTO
#         */
#         basic.clearScreen()
#         let conto = 0
#         let valore_caratteristico = 0

#         basic.forever(function () {
#             basic.pause(2000)
#             valore_caratteristico += randint(1, 6)
#             basic.showNumber(valore_caratteristico)
#             if (valore_caratteristico % 2 == 0) {
#                 music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
#             } else {
#                 music.stopAllSounds()
#             }
#         })
#         """
# }






