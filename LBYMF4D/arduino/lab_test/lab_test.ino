/*int lastButtonState;
int currentButtonState;
int ledState = LOW;

void setup()
    {
        pinMode(4, OUTPUT);
        pinMode(7, INPUT);
    }

void loop()
    {
        lastButtonState = currentButtonState;
        currentButtonState = digitalRead(7);
        if((lastButtonState==HIGH)&&(currentButtonState==LOW))
        {
            ledState = !ledState;
            digitalWrite(4, ledState);
        }
        delay(10);
    }
*/

const int buttonPin = 7;
int buttonState = 0;

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  Serial.println(buttonState);
  delay(100);
}
