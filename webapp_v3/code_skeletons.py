

description2var= {#keys should contain the IT description needed to be shown in the app for each example.
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

example_list= [
    "lvl1a1-1in_1out",
    "lvl1a2-1in_1out_else",

    "lvl1b1-1in_2out",
    "lvl1b2-1in_2out_else",

    "lvl1c1-2in_1out",
    "lvl1c2-2in_1out_else",
    
    "lvl2a1-1in_1out-1in_1out",
    "lvl2a2-1in_1out_else-1in_1out_else",

    "lvl2b1-1in_1out_elif_1in_1out",
    "lvl2b2-1in_1out_elif_1in_1out_else",

    "lvl2c1-1in_1out-nest-1in_1out",
    "lvl2c2-1in_1out-nest-1in_1out_else_else",

    "lvl3a1-1in_1out_var",
    "lvl3a2-1in_1out_var_else",

    "lvl3b1-1var_1out",
    "lvl3b2-1var_1out_else"
]


default_IO = {
    "lvl1a1-1in_1out"                   :{"in1":"","out1":""},
    "lvl1a2-1in_1out_else"              :{"in1":"","out1":""},
    "lvl1b1-1in_2out"                   :{"in1":"","out1":"","out2":""},
    "lvl1b2-1in_2out_else"              :{"in1":"","out1":"","out2":""},
    "lvl1c1-2in_1out"                   :{"in1":"","in2":"","out1":""},
    "lvl1c2-2in_1out_else"              :{"in1":"","in2":"","out1":""},
    "lvl2a1-1in_1out-1in_1out"          :{"in1":"","out1":"","in2":"","out2":""},
    "lvl2a2-1in_1out_else-1in_1out_else":{"in1":"","out1":"","in2":"","out2":""},
    "lvl2b1-1in_1out_elif_1in_1out"     :{"in1":"","out1":"","in2":"","out2":""},
    "lvl2b2-1in_1out_elif_1in_1out_else":{"in1":"","out1":"","in2":"","out2":""},
    "lvl2c1-1in_1out-nest-1in_1out"     :{"in1":"","out1":"","in2":"","out2":""},
    "lvl2c2-1in_1out-nest-1in_1out_else_else":{"in1":"","out1":"","in2":"","out2":""},
    "lvl3a1-1in_1out_var"               :{"in1":"","out1":""},  
    "lvl3a2-1in_1out_var_else"          :{"in1":"","out1":""},
    "lvl3b1-1var_1out"                  :{"in1":"","out1":""},
    "lvl3b2-1var_1out_else"             :{"in1":"","out1":""}
}



code_skeletons = {
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
    "lvl1c1-2in_1out : 
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
        let conto = 0
        let valore_caratteristico = 0
        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            basic.showNumber(valore_caratteristico)
            if (valore_caratteristico % 2 == 0) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
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
                _out1_
            }
        })
        """, 
    "lvl1b1-1in_2out_else" : 
        """
        /**
        * CESTINO SORRIDENTE, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (_in1_) {
                _out1_
                _out2_
            } else {
                _out1_
                _out2_
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
                _out1_
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
                _out1_
            }
            if (_in2_) {
                _out2_
            } else {
                _out2_
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
                _out1_
                _out2_
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
                    _out2_
                }
            } else {
                _out1_
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
                _out1_
            }
        })
        """, 
    "lvl3b2-1var_1out_else" : 
        """   
        /**
        * IL DADO MUSICALE, ALTRIMENTI SPENTO
        */
        basic.clearScreen()
        let conto = 0
        let valore_caratteristico = 0

        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            basic.showNumber(valore_caratteristico)
            if (valore_caratteristico % 2 == 0) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            } else {
                music.stopAllSounds()
            }
        })
        """
}


code_examples = {
    "lvl1a1-1in_1out" : 
        """
        /**
        * CESTINO SORRIDENTE
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            }
        })
        """, 
    "lvl1b1-1in_2out" : 
        """
        /**
        * ALBERO ANIMATO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Heart)
                basic.showIcon(IconNames.SmallHeart)
            }
        })
        """, 
    "lvl1c1-2in_1out : 
        """
        /**
        * OROLOGIO SEGNAFREDDO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A) && input.temperature() < 10) {
                basic.showIcon(IconNames.Sad)
            }
        })
        """, 
    "lvl2a1-1in_1out-1in_1out" : 
        """
                /**
        * TAVOLO GIOCO X 2, FACCINA E MUSICA
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            }
            if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            }
        })
        """, 
    "lvl2b1-1in_1out_elif_1in_1out" : 
        """
                /**
        * CAVALLO SFIDA X 2, O  FACCINA O MUSICA
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            }
        })
        """, 
    "lvl2c1-1in_1out-nest-1in_1out" : 
        """
        /**
        * PANCHINA x DUE., CON FACCINA E POI MUSICALE
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
                if (input.buttonIsPressed(Button.B)) {
                    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
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
            if (input.buttonIsPressed(Button.A)) {
                conto += 1
                basic.showString("" + (conto))
            }
        })
        """, 
    "lvl3b1-1var_1out" : 
        """
        /**
        * IL DADO MUSICALE
        */
        basic.clearScreen()
        let conto = 0
        let valore_caratteristico = 0
        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            basic.showNumber(valore_caratteristico)
            if (valore_caratteristico % 2 == 0) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            }
        })
        """, 
    "lvl1a2-1in_1out_else" : 
        """
        /**
        * ALBERO ANIMATO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Heart)
                basic.showIcon(IconNames.SmallHeart)
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "lvl1b1-1in_2out_else" : 
        """
        /**
        * CESTINO SORRIDENTE, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else {
                basic.clearScreen()
            }
        }) 
        """, 
    "lvl1c2-2in_1out_else" : 
        """
                /**
        * OROLOGIO SEGNAFREDDO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A) && input.temperature() < 10) {
                basic.showIcon(IconNames.Sad)
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "lvl2a2-1in_1out_else-1in_1out_else" : 
        """
        /**
        * TAVOLO GIOCO X 2, FACCINA E MUSICA, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else {
                basic.clearScreen()
            }
            if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            } else {
                music.stopAllSounds()
            }
        })
        """, 
    "lvl2b2-1in_1out_elif_1in_1out_else" : 
        """
        /**
        * CAVALLO SFIDA X 2, O  FACCINA O MUSICA, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            } else {
                basic.clearScreen()
                music.stopAllSounds()
            }
        })
        """, 
    "lvl2c2-1in_1out-nest-1in_1out_else_else" : 
        """
        /**
        * PANCHINA x DUE., CON FACCINA E POI MUSICALE, ALTRIMENTI SPENTA
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
                if (input.buttonIsPressed(Button.B)) {
                    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
                } else {
                    music.stopAllSounds()
                }
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "lvl3a2-1in_1out_var_else" : 
        """
        /**
        * IL CANESTRO MOSTRA-PUNTEGGIO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                conto += 1
                basic.showString("" + (conto))
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "lvl3b2-1var_1out_else" : 
        """   
        /**
        * IL DADO MUSICALE, ALTRIMENTI SPENTO
        */
        basic.clearScreen()
        let conto = 0
        let valore_caratteristico = 0

        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            basic.showNumber(valore_caratteristico)
            if (valore_caratteristico % 2 == 0) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            } else {
                music.stopAllSounds()
            }
        })
        """
}











