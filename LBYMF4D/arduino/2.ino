int x = 1;
int y = 2;
int z = 3;
int DL = 1000;

void setup()
  {
    Serial.begin(115200);
  }

void loop(){
  x = x+2;
  y = y+3;
  z = z+5;
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(z);
  delay(DL);
}