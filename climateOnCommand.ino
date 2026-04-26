/*
while(Serial.available()){
  input = Serial.read();
  handleInput(input);
}
*/


#include "Seeed_BME280.h"
#include <Wire.h>

BME280 bme280;

void setup() {
    Serial.begin(9600);
    if(!bme280.init()){
    Serial.println("Device error!");
    }
}

void loop() {
  float pressure;

    if (Serial.available()) {
        String command = Serial.readString();
        command.trim();

        if (command == "TEMP") {
            Serial.print("Temp: ");
            Serial.print(bme280.getTemperature());
            Serial.println("C");//The unit for  Celsius because original arduino don't support speical symbols
        } 
        if (command == "HUMIDITY") {
            Serial.print("Humidity: ");
            Serial.print(bme280.getHumidity());
            Serial.println("%");
        }
        if (command == "CHEESE"){
            Serial.println("TAX");
        } 
        if (command == "BARO") {
            Serial.print("Pressure: ");
            Serial.print(pressure = bme280.getPressure());
            Serial.println("Pa");
        }
        Serial.flush();

    }
}
