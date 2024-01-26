#include "DHT.h"
#define DHTPIN 4
#define  DHTTYPE 11
DHT TH(DHTPIN, DHTTYPE);
float tempC;
float tempF;
float humidity;
int setTime = 500;
int DL = 1000;

void setup()
    {
        Serial.begin(115200);
        TH.begin();
        delay(setTime);
    }

void loop()
    {
        tempC = TH.readTemperature();
        tempF = TH.readTemperature(true);
        humidity = TH.readHumidity();
        Serial.print(tempC);
        //Serial.print("degC ");
        Serial.print(tempF);
        //Serial.print("degF ");
        Serial.print(humidity);
        //Serial.println("%humidity");
        delay(DL);
    }