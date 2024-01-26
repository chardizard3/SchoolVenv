#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE 11
DHT TH(DHTPIN, DHTTYPE);
int buttonPin = 7;
int button = 0;
float tempC;
float tempF;
float humidity;


void setup() 
{
    Serial.begin(115200);
    TH.begin();
    pinMode(buttonPin, INPUT);
}

void loop() 
{
    tempC = TH.readTemperature();
    tempF = TH.readTemperature(true);
    humidity = TH.readHumidity();
    button = digitalRead(buttonPin);
    Serial.print(tempF);
    Serial.print(",");
    Serial.print(tempC);
    Serial.print(",");
    Serial.print(humidity);
    Serial.print(",");
    Serial.println(button);
}