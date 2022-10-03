
#defining a dictionary for any additional extension/package needed for each output: %60%60%60package%0Aservo%0A%60%60%60  wrong="%60%60%%0Aservo%0A%60%60%60"
package_suffix = {
	"rotateMin"         : "%60%60%60package%0Aservo%0A%60%60%60", 
	"rotateMid"         : "%60%60%60package%0Aservo%0A%60%60%60",
	"rotateMax"         : "%60%60%60package%0Aservo%0A%60%60%60",
	"showStripRainbow"  : "%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60", 
	"showStripBlack"    : "%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60",
	"showStripGreen"    : "%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60",
	"showStripRed"    : "%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60",
	"EB_humidityHigh"   : "%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60"	,
	"EB_humidityLow":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_pressureHigh":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60"	,
	"EB_pressureLow":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_noiseHigh" : "%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",  
	"EB_noiseLow" : "%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60", 
	"EB_tempHigh" :"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_tempLow" :"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_lightlevelHigh":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_lightlevelLow":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_colorIsRed":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_colorIsGreen":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_colorIsBlue":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_colorIsBlack":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_clapYes":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_clapNo":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_whiteLEDon":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	"EB_whiteLEDoff":"%60%60%60package%0Aenvirobit%3Dgithub%3Apimoroni%2Fpxt-envirobit%0A%0A%60%60%60",
	
} #only where needed

 

on_end = {
  	"recieveData":'radio.onReceivedValue(function (name, value) {\n\t if (name == "replace" && value == 1) {\n\t\t   received = 1\n\t} else  {\n\t\t   received = 0}})'
    	#"recieveData":'radio.onReceivedValue(function (name, value) {\n\t if (name == "replace" && value == 1) {\n\t\t   received = 1\n\t} else if (name == "replace" && value == 0) {\n\t\t   received = 0}})'

    #was: '\nradio.onReceivedValue(function (name, value) {\n\tif (name == "replace" && value == 1) {\n\t\t received = 1\n\t}\n})',
        } 


#defining a dictionary for startup-code for each output:
on_start = {
"EB_colorIsRed":"envirobit.setLEDs(envirobit.OnOff.On)\nenvirobit.setColourIntegrationTime(100)",
"EB_colorIsGreen":"envirobit.setLEDs(envirobit.OnOff.On)\nenvirobit.setColourIntegrationTime(100)",
"EB_colorIsBlue":"envirobit.setLEDs(envirobit.OnOff.On)\nenvirobit.setColourIntegrationTime(100)",
"EB_colorIsRed":"envirobit.setLEDs(envirobit.OnOff.On)\nenvirobit.setColourIntegrationTime(100)",
"EB_colorIsBlack":"envirobit.setLEDs(envirobit.OnOff.On)\nenvirobit.setColourIntegrationTime(100)",
"noInput": "basic.pause(1000)",
"musicHappy": "music.setVolume(255)",
"musicNone": "music.setVolume(255)",
"musicSad": "music.setVolume(255)",
"musicAlarm": "music.setVolume(255)",
"sendData":  "radio.setGroup(99)",# todo: set group automatically
"recieveData":"radio.setGroup(99)",# todo: set group automatically
"rotateMax":"servos.P1.setRange(0,180)",
"rotateMid":"servos.P1.setRange(0,180)",
"rotateMin":"servos.P1.setRange(0,180)",
"showStripBlack": "let strip = neopixel.create(DigitalPin.P1,7,NeoPixelMode.RGB)",
"showStripRainbow": "let strip = neopixel.create(DigitalPin.P1,7,NeoPixelMode.RGB)",
"showStripGreen": "let strip = neopixel.create(DigitalPin.P1,7,NeoPixelMode.RGB)",
"showStripRed": "let strip = neopixel.create(DigitalPin.P1,7,NeoPixelMode.RGB)",
"forecastHumidityHigh": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"forecastHumidityLow": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"forecastprecipHigh": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"forecastprecipLow": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"forecastTempHigh": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"forecastTempLow": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"forecastWindHigh": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"forecastWindLow": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"logInput" : "radio.setGroup(313)\nradio.setTransmitSerialNumber(true)\nradio.sendValue(\"log4\", 8791)",
"timeForSchool": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"todayNewYear": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"todayStartOfMonth": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"todaySummerMonth": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"todayWeekday": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"todayWeekend": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
"tweetInput": "radio.setGroup(313)\nradio.setTransmitSerialNumber(true)\nradio.sendValue(\"b#\", 8903)",
"tweetText" : "radio.setGroup(313)\nradio.setTransmitSerialNumber(true)\nradio.sendValue(\"b#\", 8903)",
"noOutput": "basic.pause(1000)",
}
 

input_code = {
"noiseHigh" :"input.soundLevel() >= 128" , #v2
"noiseLow" :"input.soundLevel() < 128" , #v2
"touchNo" :"!input.logoIsPressed()" , #v2
"touchYes" :"input.logoIsPressed()" , #v2
"accelHigh":"input.acceleration(Dimension.X) >= 511" ,
"accelLow":"input.acceleration(Dimension.X) < 511" ,
"buttonNotPress":"!input.buttonIsPressed(Button.A)",
"buttonPress":"input.buttonIsPressed(Button.A)",
"buttonPressB":"input.buttonIsPressed(Button.B)",#NEWsep22
"compassE" :"input.compassHeading() >= 45 && input.compassHeading() < 135" ,
"compassN" :"input.compassHeading() < 45" ,
"compassS" :"input.compassHeading() >= 135 && input.compassHeading() < 225" ,
"compassW" :"input.compassHeading() >= 225 && input.compassHeading() < 315" ,
"gestureShake":"input.isGesture(Gesture.Shake)" ,
"gestureTilt" :"input.isGesture(Gesture.TiltLeft) || input.isGesture(Gesture.TiltRight)",
"lightlevelHigh":"input.lightLevel() >= 127",
"lightlevelLow" :"input.lightLevel() < 127",
"tempHigh" :"input.temperature() >= 28" ,
"tempLow" :"input.temperature() < 28",
"recieveData":"received == 1",
"EB_humidityHigh":"envirobit.getHumidity() >= 40",
"EB_humidityLow":"envirobit.getHumidity() < 40",
"EB_pressureHigh":"envirobit.getPressure() >= 1013",
"EB_pressureLow":"envirobit.getPressure() < 1013",
"EB_noiseHigh" :"envirobit.getNoiseLevel() >= 30" ,  
"EB_noiseLow" :"envirobit.getNoiseLevel() < 30" , 
"EB_tempHigh" :"input.envirobit.getTemperature() >= 28" ,
"EB_tempLow" :"envirobit.getTemperature() < 28",
"EB_lightlevelHigh":"envirobit.getLight() >= 500",
"EB_lightlevelLow":"envirobit.getLight() >= 500",
"EB_colorIsRed":"envirobit.getRed() >= 110 && (envirobit.getGreen() < 100 && envirobit.getBlue() < 100",
"EB_colorIsGreen":"envirobit.getRed() < 100 && (envirobit.getGreen() >= 100 && envirobit.getBlue() < 100",
"EB_colorIsBlue":"envirobit.getRed() < 100 && (envirobit.getGreen() < 100 && envirobit.getBlue() >= 110",
"EB_colorIsBlack":"envirobit.getRed() < 80 && (envirobit.getGreen() < 80 && envirobit.getBlue() < 100)",
"EB_clapYes":"envirobit.waitForClap(1000)",
"EB_clapNo":"!(envirobit.waitForClap(1000))",
"movementNotPresent":"pins.digitalReadPin(DigitalPin.P2) == 0" ,
"movementPresent" :"pins.digitalReadPin(DigitalPin.P2) >= 1" , # >= 1000" ,
"sliderHigh":"pins.analogReadPin(AnalogPin.P2) >= 1000" ,
"sliderLow":"pins.analogReadPin(AnalogPin.P2) <= 100" ,
"sliderMid":"pins.analogReadPin(AnalogPin.P2) > 500 && pins.analogReadPin(AnalogPin.P2) <= 700",

"soilMoistureHigh":"pins.analogReadPin(AnalogPin.P1) >= 500",#new
"soilMoistureLow":"pins.analogReadPin(AnalogPin.P1) < 500",#new

"forecastHumidityHigh" :"forecastName == \"humid\" && forecastValue >= 0.4",
"forecastHumidityLow" :"forecastName == \"humid\" && forecastValue < 0.4",
"forecastprecipHigh" :"forecastName == \"precip\" && forecastValue >= 0.5",
"forecastprecipLow" :"forecastName == \"precip\" && forecastValue < 0.5",
"forecastTempHigh" :"forecastName == \"temp\" && forecastValue >= 28",
"forecastTempLow" :"forecastName == \"temp\" && forecastValue < 28",
"forecastWindHigh" :"forecastName == \"wind\" && forecastValue >= 0.5",
"forecastWindLow" :"forecastName == \"wind\" && forecastValue < 0.5",
"timeForSchool" :"forecastName == \"time\" && forecastValue >= 0745",
"todayNewYear" :"forecastName == \"year\" && forecastValue == 2022",
"todayStartOfMonth" :"forecastName == \"date\" && forecastValue == 1",
"todaySummerMonth" :"forecastName == \"month\" && (forecastValue >= 6 && forecastValue <= 8)",#6,7,8
"todayWeekday" :"forecastName == \"day\" && forecastValue <= 5",#1,2,3,4,5
"todayWeekend" :"forecastName == \"day\" && forecastValue >= 6",#6,7
"noInput":"true",
} 




#only for tweeting, logging paired physical sensorValues:
input_sensorValue = {
"noiseHigh" :"input.soundLevel()" , #v2
"noiseLow" :"input.soundLevel()" , #v2
"touchNo" :"input.logoIsPressed()" , #v2
"touchYes" :"input.logoIsPressed()" , #v2
"accelHigh":"input.acceleration(Dimension.X)" ,
"accelLow":"input.acceleration(Dimension.X)" ,
"buttonNotPress":"input.buttonIsPressed(Button.A)",
"buttonPress":"input.buttonIsPressed(Button.A)",
"compassE" :"input.compassHeading()" ,
"compassN" :"input.compassHeading()" ,
"compassS" :"input.compassHeading()" ,
"compassW" :"input.compassHeading()" ,
"gestureShake":"input.isGesture(Gesture.Shake)" ,
"gestureTilt" :"input.isGesture(Gesture.TiltLeft) || input.isGesture(Gesture.TiltRight)",
"lightlevelHigh":"input.lightLevel()",
"lightlevelLow" :"input.lightLevel()",
"tempHigh" :"input.temperature()" ,
"tempLow" :"input.temperature()",
"recieveData" :"recieveData",
"EB_humidityHigh":"envirobit.getHumidity()",
"EB_humidityLow":"envirobit.getHumidity()",
"EB_pressureHigh":"envirobit.getPressure()",
"EB_pressureLow":"envirobit.getPressure()",
"EB_noiseHigh" :"envirobit.getNoiseLevel()" ,  
"EB_noiseLow" :"envirobit.getNoiseLevel()" ,  
"EB_tempHigh" :"envirobit.getTemperature()" ,
"EB_tempLow" :"input.envirobit.getTemperature()",
"EB_lightlevelHigh":"envirobit.getLight()",
"EB_lightlevelLow":"envirobit.getLight()",
"EB_colorIsRed":"envirobit.getRed()",
"EB_colorIsGreen":"envirobit.getGreen()",
"EB_colorIsBlue":"envirobit.getBlue()",
"EB_colorIsBlack":"envirobit.getLight()",
"EB_clapYes":"envirobit.waitForClap(1000)",
"EB_clapNo":"!(envirobit.waitForClap(1000))",
"movementNotPresent":"pins.digitalReadPin(DigitalPin.P0)" ,
"movementPresent" :"pins.digitalReadPin(DigitalPin.P0)" ,
"sliderHigh":"pins.analogReadPin(AnalogPin.P0)" ,
"sliderLow":"pins.analogReadPin(AnalogPin.P0)" ,
"sliderMid":"pins.analogReadPin(AnalogPin.P0)",

"soilMoistureHigh":"pins.analogReadPin(AnalogPin.P1)",#new
"soilMoistureLow":"pins.analogReadPin(AnalogPin.P1)",#new


"forecastHumidityHigh" :"forecastValue",
"forecastHumidityLow" :"forecastValue",
"forecastprecipHigh" :"forecastValue",
"forecastprecipLow" :"forecastValue",
"forecastTempHigh" :"forecastValue",
"forecastTempLow" :"forecastValue",
"forecastWindHigh" :"forecastValue",
"forecastWindLow" :"forecastValue",
"timeForSchool" :"forecastValue",#should this be a value converted to str
"todayNewYear" :"forecastValue",
"todayStartOfMonth" :"forecastValue",
"todaySummerMonth" :"forecastValue",
"todayWeekday" :"forecastValue",
"todayWeekend" :"forecastValue",
"noInput" :"noInput",
"none" :"none",
"noOutput" :"noOutput",
"sendData" :"sendData",
}


output_code = {
"musicHappy" : "music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)\n\tbasic.pause(9000)",
"musicNone" : "music.stopMelody(MelodyStopOptions.All)\n\tbasic.pause(1000)" ,
"musicSad" : "music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Forever)\n\tbasic.pause(9000)",
"musicAlarm" : "music.playMelody(\"A C5 A C5 A C5 A C5\",110)\n\tbasic.pause(9000)",
"displayInput": "basic.showNumber(0)\n\tbasic.pause(1000)" ,
"displayNone" :"basic.clearScreen()\n\tbasic.pause(1000)" ,
"displayText" : "basic.showString(\"Ciao \")\n\tbasic.pause(1000)" ,
"iconHappy":"basic.showIcon(IconNames.Happy)\n\tbasic.pause(1000)",
"iconNone": "basic.clearScreen()\n\tbasic.pause(1000)",
"iconBig":"basic.showIcon(IconNames.Heart)\n\tbasic.pause(1000)",
"iconSmall":"basic.showIcon(IconNames.SmallHeart)\n\tbasic.pause(1000)",
"iconSad": "basic.showIcon(IconNames.Sad)\n\tbasic.pause(1000)",
"sendData": "radio.sendValue(\"inputName\",1)\n\tbasic.pause(2000)", #was: "radio.sendValue(\"inputName\",inputValue)",
"EB_whiteLEDon":"envirobit.setLEDs(envirobit.OnOff.On)",
"EB_whiteLEDoff":"envirobit.setLEDs(envirobit.OnOff.Off)",
"fanOff" : "pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)",
"fanOn" : "pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)",
"lightOff": "pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)",
"lightOn": "pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)",
"rotateMax" :"servos.P1.setAngle(180)\n\tbasic.pause(1000)" ,
"rotateMid" :"servos.P1.setAngle(90)\n\tbasic.pause(1000)" , #card not used 
"rotateMin" :"servos.P1.setAngle(0)\n\tbasic.pause(1000)" ,
"showStripBlack" : "strip.showColor(neopixel.colors(NeoPixelColors.Black))\n\tbasic.pause(1000)",
"showStripRainbow" : "strip.showRainbow(1, 360)\n\tbasic.pause(1000)",
"showStripGreen" : "strip.showColor(neopixel.colors(NeoPixelColors.Green))\n\tbasic.pause(1000)",
"showStripRed" : "strip.showColor(neopixel.colors(NeoPixelColors.Red))\n\tbasic.pause(1000)",
"forecastHumidityHigh" : "",
"forecastHumidityLow" : "",
"forecastprecipHigh" : "",
"forecastprecipLow" : "",
"forecastTempHigh" : "",
"forecastTempLow" : "",
"forecastWindHigh" : "",
"forecastWindLow" : "",
"logInput" : "radio.sendValue(\"&value\", 0)", #add input name and value directly??? use variable
"timeForSchool" : "",
"todayNewYear" : "",
"todayStartOfMonth" : "",
"todaySummerMonth" : "",
"todayWeekday" : "",
"todayWeekend" : "",
"tweetInput" : "radio.sendString(\"#nameValue\")\n\tbasic.pause(1000)" , #add input name and value directly???use variable
"tweetText" : "radio.sendString(\"#Ciao\")\n\tbasic.pause(1000)" ,
"noOutput":"",
}


#defining a dictionary for inverse code for each output: 
output_else_code={
"musicHappy": "music.stopMelody(MelodyStopOptions.All)\n\tbasic.pause(1000)",
"musicNone" : "music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)\n\tbasic.pause(1000)",
"musicSad" : "music.stopMelody(MelodyStopOptions.All)\n\tbasic.pause(1000)",
"musicAlarm" : "music.stopMelody(MelodyStopOptions.All)\n\tbasic.pause(1000)",
"displayInput": "basic.clearScreen()\n\tbasic.pause(1000)" ,
"displayNone" : "basic.showString(\"hello\")\n\tbasic.pause(1000)" ,
"displayText" : "basic.clearScreen()\n\tbasic.pause(1000)" ,
"iconHappy":"basic.clearScreen()\n\tbasic.pause(1000)",
"iconNone": "basic.showIcon(IconNames.Happy)\n\tbasic.pause(1000)",
"iconSad": "basic.clearScreen()\n\tbasic.pause(1000)",
"iconBig": "basic.clearScreen()\n\tbasic.pause(1000)",
"iconSmall": "basic.clearScreen()\n\tbasic.pause(1000)",
"sendData": "radio.sendValue(\"inputName\",0)\n\tbasic.pause(2000)", #was: "sendData":"basic.pause(1000)",
"EB_whiteLEDon":"LEDs On",
"EB_whiteLEDoff":"LEDs Off",
"fanOff" : "pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)",
"fanOn" : "pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)",
"lightOff": "pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)",
"lightOn": "pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)",
"rotateMax" :"servos.P1.setAngle(0)\n\tbasic.pause(1000)" , #card not used 
"rotateMid" :"servos.P1.setAngle(0)\n\tbasic.pause(1000)" , #card not used 
"rotateMin" :"servos.P1.setAngle(180)\n\tbasic.pause(1000)",#card not used 
"showStripBlack" :"strip.showRainbow(1, 360)\n\tbasic.pause(1000)",
"showStripRainbow": "strip.showColor(neopixel.colors(NeoPixelColors.Black))\n\tbasic.pause(1000)",
"showStripBlack" :"strip.showRainbow(1, 360)\n\tbasic.pause(1000)",
"showStripBlack" :"strip.showRainbow(1, 360)\n\tbasic.pause(1000)",
"forecastHumidityHigh" :"radio.sendString(\"get_humid\")\n\tbasic.pause(2000)",
"forecastHumidityLow" :"radio.sendString(\"get_humid\")\n\tbasic.pause(2000)",
"forecastprecipHigh" :"radio.sendString(\"get_precip\")\n\tbasic.pause(2000)",
"forecastprecipLow" :"radio.sendString(\"get_precip\")\n\tbasic.pause(2000)",
"forecastTempHigh" :"radio.sendString(\"get_temp\")\n\tbasic.pause(2000)",
"forecastTempLow" :"radio.sendString(\"get_temp\")\n\tbasic.pause(2000)",
"forecastWindHigh" :"radio.sendString(\"get_wind\")\n\tbasic.pause(2000)",
"forecastWindLow" :"radio.sendString(\"get_wind\")\n\tbasic.pause(2000)",
"logInput" : "basic.pause(1000)", #not needed for cloud cards, can else statement remains empty??
"timeForSchool" :"radio.sendString(\"get_time\")\n\tbasic.pause(2000)",
"todayNewYear" :"radio.sendString(\"get_year\")\n\tbasic.pause(2000)",
"todayStartOfMonth" :"radio.sendString(\"get_date\")\n\tbasic.pause(2000)",
"todaySummerMonth" :"radio.sendString(\"get_month\")\n\tbasic.pause(2000)",
"todayWeekday" :"radio.sendString(\"get_day\")\n\tbasic.pause(2000)",
"todayWeekend" :"radio.sendString(\"get_day\")\n\tbasic.pause(2000)",
"tweetInput" : "basic.pause(1000)" , #not needed for cloud cards, can else statement remains empty??
"tweetText" : "basic.pause(1000)" , #not needed for cloud cards, can else statement remains empty??
"noOutput":"",
}



