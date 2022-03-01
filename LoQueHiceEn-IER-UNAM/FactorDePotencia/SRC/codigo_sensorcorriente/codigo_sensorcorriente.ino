//----Librerias-------------------//
//#include <WiFiEspClient.h>
#include <WiFiEsp.h>
//#include <WiFiEspUdp.h>
#include "SoftwareSerial.h"
#include <ThingsBoard.h> 
#include <Wire.h>
#include "factores.h"
//-------------------------------//

//-----datos de la red-------//
//#define WIFI_AP "IER"
//#define WIFI_PASSWORD "acadier2014"
#define WIFI_AP "INFINITUM0A0D05"
#define WIFI_PASSWORD "ED03217156"

#define TOKEN "asm8CrU6nQfGsW3Xl7Fn"  //--------Dispositivo tb-------//  
char thingsboardServer[] = "iot.ier.unam.mx"; //------Servidor ThingsBoard--------//

// Initialize the Ethernet client object
WiFiEspClient espClient;                                     
ThingsBoard tb(espClient);                                    

SoftwareSerial soft(2, 3); // RX, TX                          
int status = WL_IDLE_STATUS;
unsigned long lastSend = 0;


int pinpf = 7;
int pinvolts = 1;
int pincorriente = 3;

factores fact;

//------------------------------------------------------------//
void setup() { 
  // initialize serial for debugging
  Serial.begin(9600);
  InitWiFi();                                                
  fact.defvar(pinvolts, pinpf, pincorriente);
}
//------------------------------------------------------------//

//-------------------------------------------------------------//
void loop() {
  conectar();
  if ( millis() - lastSend > 1000 ) { // Update and send only after 1 seconds

 fact.calcular();   
    
   tb.sendTelemetryFloat("voltaje", fact.volts);
    tb.sendTelemetryFloat("corriente", fact.Irms);
    tb.sendTelemetryFloat("factor_p", fact.pf);
    
    lastSend = millis();
  }
  tb.loop();
}
//..........................................................//


//-------------------------------------------------------------------------------------------------------------//
void InitWiFi()
{
  // initialize serial for ESP module
  soft.begin(9600);
  // initialize ESP module
  WiFi.init(&soft);
  // check for the presence of the shield
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    // don't continue
    while (true);
  }
  Serial.println("Connecting to AP ...");
  // attempt to connect to WiFi network
  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(WIFI_AP);
    // Connect to WPA/WPA2 network
    status = WiFi.begin(WIFI_AP, WIFI_PASSWORD);
    delay(500);
  }
  Serial.println("Connected to AP");
}
//---------------------------------------------------------------------------------------------------------------//

//---------------------------------------------------------------------------------------------------------------//
void reconnect() {
  // Loop until we're reconnected
  while (!tb.connected()) {
    Serial.print("Connecting to ThingsBoard node ...");
    // Attempt to connect (clientId, username, password)
    if ( tb.connect(thingsboardServer, TOKEN) ) {
      Serial.println( "[DONE]" );
    } else {
      Serial.print( "[FAILED]" );
      Serial.println( " : retrying in 5 seconds" );
      // Wait 5 seconds before retrying
      delay( 5000 );
    }
  }
}

 void conectar() {
  status = WiFi.status();
  if ( status != WL_CONNECTED) {
    while ( status != WL_CONNECTED) {
      Serial.print("Attempting to connect to WPA SSID: ");
      Serial.println(WIFI_AP);
      // Connect to WPA/WPA2 network
      status = WiFi.begin(WIFI_AP, WIFI_PASSWORD);
      delay(500);
    }
    Serial.println("Connected to AP");
  }
  if ( !tb.connected() ) {
    reconnect();
  }
  }
//-------------------------------------------------------------------------------------------------------------------//
