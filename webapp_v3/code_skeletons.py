
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
    "lvl3b2-1var_1out_else",

]


default_IO = {
    "lvl1-1con-1in-1out" : "toadd"
}


code_skeletons = {
    "lvl1-1con-1in-1out" : 
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
    "lvl1-1con-1in-2out" : 
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
    "lvl1-1con-2in-1out" : 
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
    "lvl1-2con-2in-2out" : 
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
    "lvl1-1con-2in-2out" : 
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
    "lvl1-2con-2in-2out" : 
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
    "lvl1-1con-1in-2out" : 
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
    "lvl1-1con-1in-2out" : 
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
    "1" : 
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
    "1" : 
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
    "1" : 
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
    "1" : 
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
    "1" : 
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
    "1" : 
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
    "1" : 
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
    "1" : 
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
        """, 
     
}











