int cnt = 1; 
int DL = 1000;

void setup()
    {
        Serial.begin(115200);
    }

void loop()
    {
        Serial.print(cnt);
        Serial.println(" Tawsan");
        cnt = cnt+1;
        delay(DL);
    }