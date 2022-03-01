#include <WiFiEspClient.h>
#include <WiFiEsp.h>
#include <WiFiEspUdp.h>
#include "SoftwareSerial.h"
#include <ThingsBoard.h>

#define WIFI_AP "INFINITUM0A0D05"
#define WIFI_PASSWORD "ED03217156"
#define TOKEN "xEBrkdL8msSw174XoZj0"
char thingsboardServer[]= "iot.ier.unam.mx";

WiFiEspClient espClient;
ThingsBoard tb (espClient);

SoftwareSerial soft(10,11);
int status = WL_IDLE_STATUS;
unsigned long lastSend = 0;
int adc_max=700;        //Reemplazar por valor adc_max entregado por el sketch: volt_ac_cal
int adc_min=335;        //Reemplazar por valor adc_min entregado por el sketch: volt_ac_cal
float volt_multi=120;   //Reemplazar por el "voltaje ac rms" entregado por un multimetro
float volt_multi_p;
float volt_multi_n;

int pinpf1 = 7;
float rads = 57.29577951;
float degree = 360;
float frequency = 60;
float nano = 1 * pow (10,-6);
float pf1;
float angle;
float pf_max = 0;
float angle_max = 0;

void setup() {
  pinMode(pinpf1,INPUT);
  Serial.begin(9600);
  volt_multi_p = volt_multi * 1.4142;   //Voltaje pico= Voltaje RMS * 1.4142 (Corriente Monofasica)
  volt_multi_n = volt_multi_p * -1;
  InitWiFi();
  lastSend=0;
}

void loop() {
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

  if ( millis() - lastSend > 1000 ) { // Update and send only after 1 seconds
    get_parametros();
    lastSend = millis();
  }

  tb.loop();
}
//------------obtener-parametros---------------------//
void get_parametros() {

  angle = ((((pulseIn(pinpf1, HIGH)) * nano)* degree)* frequency);
  pf1 = cos(angle / rads);
  if (angle > angle_max)
  {
  angle_max = angle;
  pf_max = cos(angle_max / rads);
  }
  float volt_rms=get_voltage(); //Voltage eficaz (V-RMS)
  float I=get_corriente(); //Corriente eficaz (A) 

  Serial.print("Vrms: ");
  Serial.print(volt_rms,3);
  Serial.println(" VAC");
  
  Serial.print("Irms: ");
  Serial.print(I,3);
  Serial.println("A");

  Serial.print("F.P: ");
  Serial.println(pf_max, 2);
  tb.sendTelemetryFloat("voltaje", volt_rms);
  tb.sendTelemetryFloat("corriente", I);
  tb.sendTelemetryFloat("F.P.", pf_max);
  
  delay(50); 
  angle_max = 0; // Reset variables for next test
  pf_max = 0;
}
//----------------------initwifi-----------------//
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
//-------------voltaje------------------//
float get_voltage()
{
  float adc_sample;
  float volt_inst=0;
  float Sumatoria=0;
  float volt;
  long tiempo_init=millis();
  int N=0;
  
  while( (millis() - tiempo_init) < 500)//Duración 0.5 segundos(Aprox. 30 ciclos de 60Hz)
  { 
    adc_sample = analogRead(A0);    //voltaje del sensor
    volt_inst = map(adc_sample,adc_min,adc_max,volt_multi_n,volt_multi_p);
    Sumatoria = Sumatoria+sq(volt_inst);    //Sumatoria de Cuadrados
    N = N+1;
    delay(1);
  }
  volt=sqrt((Sumatoria)/N); //ecuación del RMS
  return(volt);
}
//-----------CORRIENTE------------------------//
float get_corriente()
{
  float voltajeSensor;
  float corriente=0;
  float Sumatoria=0;
  long tiempo=millis();
  int n=0;
  while(millis()-tiempo<500)//Duración 0.5 segundos(Aprox. 30 ciclos de 60Hz)
  { 
    voltajeSensor = analogRead(A3) * (5 / 1023.0);////voltaje del sensor
    corriente=voltajeSensor*6; //corriente=VoltajeSensor*(30A/1V)
    Sumatoria=Sumatoria+sq(corriente);//Sumatoria de Cuadrados
    n=n+1;
    delay(1);
  }
  Sumatoria=Sumatoria*2;//Para compensar los cuadrados de los semiciclos negativos.
  corriente=sqrt((Sumatoria)/n); //ecuación del RMS
  return(corriente);
}
