int potPin = A0;
int potVal;
int DL = 100;

void setup()
    {
        pinMode(potPin, INPUT);
        Serial.begin(115200);
    }

void loop()
    {
        potVal=analogRead(potPin);
        Serial.println(potVal);
        delay(DL);
    }