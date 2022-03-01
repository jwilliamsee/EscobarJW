
const int OutPin = A1;

float P1 = 8.8945e-9;
float P2 = -1.2185e-5;
float P3 = 0.0063302;
float P4 = -1.4628;
float P5 = 126.23;

void setup() {
    Serial.begin(9600);
}

void loop() {
  int wind = analogRead(OutPin);
  float V = ((P1*(pow(wind,4))) + (P2*(pow(wind,3))) + (P3*(pow(wind,2)) + (P4 * wind) + P5)); 
  Serial.println(wind);
  Serial.print(V, 5);
  Serial.println(" m/s ");
  delay(1000);

}
