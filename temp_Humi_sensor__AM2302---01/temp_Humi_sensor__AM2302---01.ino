

// 라이브러리
#include "DHT.h"

// 핀설정
#define DHT01PIN 2        // define the digital I/O pin
#define DHT02PIN 3        // define the digital I/O pin (핀번호만 수정할 것)

// 센서 타입
#define DHT01TYPE DHT22         // DHT 22
#define DHT02TYPE DHT22         // DHT 22

// 센서초기화
DHT dht01(DHT01PIN, DHT01TYPE);
DHT dht02(DHT02PIN, DHT02TYPE);

// 변수
float h11;
float t11;
float h22;
float t22;
char caracter;   // 입력 신호


void setup() {
  Serial.begin(9600);
  dht01.begin();
  dht02.begin();
}

void loop() {
  float h11 = dht01.readHumidity();
  float t11 = dht01.readTemperature();
  float h22 = dht02.readHumidity();
  float t22 = dht02.readTemperature();
  delay(500);


  if (Serial.available()) {
    caracter = Serial.read();

    if (caracter == 'a') {               // 'a'  입력시  1번센서 출력
      Serial.print("Humidity 11: ");
      Serial.print(h11);
      Serial.print(" %\t");
      Serial.print("Temperature 11: ");
      Serial.print(t11);
      Serial.println(" *C");
    }
    if (caracter == 'b') {               // 'b' 입력시  2번센서 출력
      Serial.print("Humidity 22: ");
      Serial.print(h22);
      Serial.print(" %\t");
      Serial.print("Temperature 22: ");
      Serial.print(t22);
      Serial.println(" *C");
    }
  }
}


