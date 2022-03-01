#include <Wire.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <SoftwareSerial.h>
#include "ThingsBoard.h"


#define WIFI_AP             "INFINITUM377B_2.4" //INFINITUM377B_2.4 IER
#define WIFI_PASSWORD       "fh7aSE6DmP"        //fh7aSE6DmP acadier2014
#define TOKEN               "DdRIZk8TRO4Rb9iLPd2z"
#define THINGSBOARD_SERVER  "demo.thingsboard.io"


WiFiClient espClient;
ThingsBoard tb(espClient);
int status = WL_IDLE_STATUS;
SoftwareSerial Serialp(13,15); //rxD8, txD7

float A, B, C, D;
char data;

void setup() {
  
  WiFi.begin(WIFI_AP, WIFI_PASSWORD);
  InitWiFi();
  Serial.begin(57600);
  Serialp.begin(57600);
}

void loop() {
  delay(1000);

  if (WiFi.status() != WL_CONNECTED) {
    reconnect();
  }

  if (!tb.connected()) {
    // Connect to the ThingsBoard
    Serial.print("Connecting to: ");
    Serial.print(THINGSBOARD_SERVER);
    Serial.print(" with token ");
    Serial.println(TOKEN);
    if (!tb.connect(THINGSBOARD_SERVER, TOKEN)) {
      Serial.println("Failed to connect");
      return;
    }
  }
  while (Serialp.available() > 0){ 
           
            data= Serialp.read();

             if (data=='A'){
                            A= Serialp.parseFloat();
                            Serial.println("FLUJO DE CALOR S1 = ");
                            Serial.println(A); 
                            Serial.println("Sending data..."); 
                            tb.sendTelemetryFloat("FCS1", A);
                            }
             if (data=='B'){
                            B= Serialp.parseFloat();
                            Serial.println("TEMPERATURA S1 = ");
                            Serial.println(B);
                            Serial.println("Sending data...");
                            tb.sendTelemetryFloat("TPS1", B);
                            }  
             if (data=='C'){
                            C= Serialp.parseFloat();
                            Serial.println("FLUJO DE CALOR S2 = ");
                            Serial.println(C); 
                            Serial.println("Sending data...");  
                            tb.sendTelemetryFloat("FCS2", C);
                               }
             if (data=='D'){
                            D= Serialp.parseFloat();
                            Serial.println("TEMPERATURA S2 = ");
                            Serial.println(D); 
                            Serial.println("Sending data...");  
                            tb.sendTelemetryFloat("TPS2", D);
                               }                   
                        
             }
  

  // Uploads new telemetry to ThingsBoard using MQTT.
  // See https://thingsboard.io/docs/reference/mqtt-api/#telemetry-upload-api
  // for more details

  
  

  tb.loop();
}

void InitWiFi()
{
  Serial.println("Connecting to AP ...");
  // attempt to connect to WiFi network

  WiFi.begin(WIFI_AP, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to AP");
}

void reconnect() {
  // Loop until we're reconnected
  status = WiFi.status();
  if ( status != WL_CONNECTED) {
    WiFi.begin(WIFI_AP, WIFI_PASSWORD);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("Connected to AP");
  }
}
