#include "MFRC522.h"
/*
 * Initial Author: ryand1011 (https://github.com/ryand1011)
 *
 * Reads data written by a program such as "rfid_write_personal_data.ino"
 *
 * See: https://github.com/miguelbalboa/rfid/tree/master/examples/rfid_write_personal_data
 *
 * Uses MIFARE RFID card using RFID-RC522 reader
 * 
 * Uses MFRC522 - Library
 * -----------------------------------------------------------------------------------------
 *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 * Signal      Pin          Pin           Pin       Pin        Pin              Pin
 * -----------------------------------------------------------------------------------------
 * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 * SPI SS      SDA(SS)      10            53        D10        10               10
 * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
*/

MFRC522 rfid(10, 9);
MFRC522::MIFARE_Key key;
String channel="1";
int LED_Green = 3;
int LED_Red = 2;
int scanStateFlag = 0;

#define RFID_AccessCards 1
String RFID_Correct[RFID_AccessCards] = {"2c:d7:c3:a5"};
unsigned long RFID_ScanTime;

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  pinMode(LED_Green, OUTPUT);
  pinMode(LED_Red, OUTPUT);
  digitalWrite(LED_Red,HIGH);
}

void loop() {
  processStateFlag();
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial()) {
    
    return;
    
  }else {
    String strID = "";
    for (byte i = 0; i < 4; i++) {
      strID += (rfid.uid.uidByte[i] < 0x10 ? "0" : "") + String(rfid.uid.uidByte[i], HEX) + (i!=3 ? ":" : "");
    }
    processStateFlag();
    RFID_ScanTime = millis(); //12000
    //Serial.print("Card key: ");
    //channel:>channelNumber<; songId:>0xz212<;
    digitalWrite(LED_Red,LOW);
    analogWrite(LED_Green,255);
    String fin= "channel:>"+channel+"<; songId:>"+strID+"<;";
    Serial.println(fin);
    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();
  }
  for(int i=255;i>=0;i--){
    analogWrite(LED_Green,i);
    delay(10);
    }
    digitalWrite(LED_Red,HIGH);
}

void processStateFlag() {
  if(scanStateFlag == 1) {
      if(millis() - RFID_ScanTime < 2000) {
        digitalWrite(LED_Red,HIGH);
        digitalWrite(LED_Green,LOW);
      }else {
        digitalWrite(LED_Green,HIGH);
        scanStateFlag = 0;
      }
  }else if(scanStateFlag == 2) {
      if(millis() - RFID_ScanTime < 2000) {
        digitalWrite(LED_Green,HIGH);
        digitalWrite(LED_Red,LOW);
      }else {
        digitalWrite(LED_Red,HIGH);
        scanStateFlag = 0;
      }    
  }else {
    
  }
}

