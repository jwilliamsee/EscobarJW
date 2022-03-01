/* A demo sketch for the Modern Device Rev P Wind Sensor
* Requires a Wind Sensor Rev P from Modern Device
* http://moderndevice.com/product/wind-sensor-rev-p/
* 
* The Rev P requires at least at least an 8 volt supply. The easiest way to power it 
* if you are using an Arduino is to use a 9 volt or higher supply on the external power jack
* and power the sensor from Vin.
* 
* Hardware hookup 
* Sensor     Arduino Pin
* Ground     Ground
* +10-12V      Vin
* Out          A0
* TMP          A2
*
* Paul Badger 2014
* code in the public domain
**************************************************
* Adapted for 6 sensors by Rafael Moya & Daniel Prohasky 06/2015
*/
//FUENTE: https://miniwindtunnel.wordpress.com/tutorial/
//RANGO: 0 a 4.5 m/s
const int OutPin[1]  = {A0};   // 4 wind sensor analog pin  hooked up to Wind P sensor "OUT" pin
const int TempPin[1] = {A1};   // 4 temp sesnsor analog pin hooked up to Wind P sensor "TMP" pin

void setup(){
  Serial.begin(9600);
 
}

void loop(){

    // wind formula derived from a wind tunnel data, annemometer and some fancy Excel regressions
    // this scalin doesn't have any temperature correction in it yet
    //Puede conectarse hasta los 6 sensores que probaron en esta Fuente de información
    for (int i=0; i<1; i++){
        int windADunits = analogRead(OutPin[i]);
        float windMPH =  pow((((float)windADunits - 264.0) / 85.6814), 3.36814);
        Serial.print(windMPH);
        //Descomentar la línea de babajo para más sensores
        //Serial.print(",");
        Serial.print(" MPH\t");
        // temp routine and print raw and temp C
        
        //CONVERSIÓN A m/s
        float windMPS = windMPH * 0.44704;
        Serial.print(windMPS, 4);
        //Descomentar la línea de abajo para más sensores
        //Serial.print(",");
        Serial.print(" m/s\t ");
    }
    for (int i=0; i<1; i++){
        int tempRawAD = analogRead(TempPin[i]);  
        // Serial.print("RT ");    // print raw A/D for debug
        // Serial.print(tempRawAD);
        // Serial.print("\t");
        
        // convert to volts then use formula from datatsheet 
        // Vout = ( TempC * .0195 ) + .400
        // tempC = (Vout - V0c) / TC   see the MCP9701 datasheet for V0c and TC
        
        float tempC = ((((float)tempRawAD * 5.0) / 1024.0) - 0.400) / .0195; 
        Serial.print(tempC, 3);
        //Descomentar la línea de abajo para más sensores
        //Serial.print(",");
        Serial.print(" °C");
                
    }
   Serial.println(); 
   
    delay(750);
}
