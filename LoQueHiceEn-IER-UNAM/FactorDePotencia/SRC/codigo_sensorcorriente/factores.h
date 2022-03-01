#include "EmonLib.h"

EnergyMonitor emon1;

class factores{
  
  private:
    #define VOLT_CAL 148.7  //calibración del ZMPT101B
    int pinvolts;
    int pincorriente;
    int pinpf;


    
  public:

    float Irms;
    float volts;
    float pf;
//-------------------setup-------------------------------
  void defvar(int pinvolts, int pinpf, int pincorriente2){
    emon1.voltage(pinvolts, VOLT_CAL, 1.7);  // Voltage: input pin, calibration, phase_shift
    pinMode(pinpf, INPUT);
    pincorriente = pincorriente2;
  };
//---------------------------------------

//----------getvoltaje------------------------------
  float getvoltaje()
{
  emon1.calcVI(20,2000);
  float supplyVoltage = emon1.Vrms;
  return supplyVoltage; 
};
//---------------------------------

//-------------getcorriente---------------------------------
float getcorriente()
{
  int N = 0;
  float corriente = 0;
  float Sumatoria = 0;
  long tiempo = millis();
  while (millis() - tiempo < 500) //Duración 0.5 segundos(Aprox. 30 ciclos de 60Hz)
  {
    float Sensordecorriente = analogRead(pincorriente) * (1.0 / 1023.0); //voltaje del sensor de corriente alterna
    corriente = Sensordecorriente; //corriente=VoltajeSensor*(100A/1V)
    Sumatoria = Sumatoria + sq(corriente); //Sumatoria de Cuadrados
    N = N + 1;
    delay(1);
  }
  //Sumatoria = Sumatoria * 2; //Para compensar los cuadrados de los semiciclos negativos.
   corriente = sqrt((Sumatoria) / N); //Ecuación del RMS corriente=corriente;
  Serial.println(pincorriente);
  return corriente;
};
//--------------------------------------------------

//-----------------------------------------------------------------------------------------------------//
float getpower()
{ 
float rads = 57.29577951; // 1 radian = aprox. 57 grados
float degree = 360;
float frequency = 60;
float nano = 1 * pow (10, -6); // Factor de multiplicación para convertir nano segundos en segundos

float pf;
float angle;
float pf_max = 0;
float angle_max = 0;
int ctr;
  
  for (ctr = 0; ctr <= 4; ctr++) // Realice 4 mediciones y luego reinicie
  {
    // 1ª línea calcula el ángulo de fase en grados a partir del impulso de tiempo diferenciado
    // La función COS usa radianes no grados. Por lo tanto, la conversión se realizó dividiendo el ángulo / 57.2958
    angle = ((((pulseIn(pinpf, HIGH)) * nano) * degree) * frequency);
    pf = cos (angle / rads);
    if (angle > angle_max) // Probar si el ángulo es el ángulo máximo
    {
      angle_max = angle; // Si el registro máximo en la variable "angle_max"
      pf_max = cos(angle_max / rads); // Calc PF de "angle_max"
    }
  }
  if (angle_max > 360) // Si el cálculo es mayor que 360, haga lo siguiente
  {
    angle_max = 0; // asigna el 0 a "angle_max"
    pf_max = 1; // Asigna el Unity PF a "pf_max"
  }
  if (angle_max == 0) // Si el cálculo es más alto que 360, haga lo siguiente
  {
    angle_max = 1; // asigna el 0 a "angle_max"
    pf_max = 0; // Asigna el Unity PF a "pf_max"
  }
  pf_max = pf_max;

  return pf_max;
}
//---------------------------------------------------------------------------------------------------------//

//------------------calcular-------------------
float calcular() {
    float Irms = getcorriente();
    float volts = getvoltaje();
    float pf = getpower();

    //Serial.println("Sending data to ThingsBoard:"); 
    Serial.print("voltaje --> ");
    Serial.println(volts);
    Serial.print("corriente --> "); 
    Serial.println(Irms);
    Serial.print("factor_p --> ");
    Serial.println(pf);

    return Irms;
    return volts;
    return pf;
};
//---------------------------------

};
