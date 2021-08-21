#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "credentials.h"
#define PWM analogWrite
#define GLOW digitalWrite
#define LED1 14
#define LED2 12
#define LED3 4
#define LED4 5
#define EN1 9        //DEFINE A PWM GPIO HERE
#define EN2 10       //TODO: 

// WiFi
const char* ssid = WIFI_SSID;
const char* pass = WIFI_PASS;

// MQTT Broker
const char *mqtt_broker = "test.mosquitto.org";
const char *topic = "MOVEMENT";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);
void forward() {
          PWM(EN1,124);
           PWM(EN2,124);
           GLOW(LED1,HIGH);
           GLOW(LED2,LOW);
           GLOW(LED3,HIGH);
           GLOW(LED4,LOW);

}
void reverse() {
  PWM(EN1,124);
           PWM(EN2,124);
           GLOW(LED1,LOW);
           GLOW(LED2,HIGH);
           GLOW(LED3,LOW);
           GLOW(LED4,HIGH);

}
void right() {
  PWM(EN1,80);
           PWM(EN2,80);
          GLOW(LED1,HIGH);
          GLOW(LED2,LOW);
          GLOW(LED3,LOW);
          GLOW(LED4,HIGH);
          PWM(EN1,124);
           PWM(EN2,124);
}
void left() {
  PWM(EN1,80);
           PWM(EN2,80);
            GLOW(LED1,LOW);
            GLOW(LED2,HIGH);
            GLOW(LED3,HIGH);
            GLOW(LED4,LOW);
            PWM(EN1,124);
           PWM(EN2,124);
}
void setup() {
  // Set software serial baud to 115200;
  Serial.begin(115200);
  // connecting to a WiFi network
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  pinMode(LED3,OUTPUT);
  pinMode(LED4,OUTPUT);
  pinMode(EN1,OUTPUT);
  pinMode(EN2,OUTPUT);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  //connecting to a mqtt broker
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);
  while (!client.connected()) {
      String client_id = "esp8266-client-";
      client_id += String(WiFi.macAddress());
      Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
      if (client.connect(client_id.c_str())) {
          Serial.println("Public mosquitto mqtt broker connected");
      } else {
          Serial.print("failed with state ");
          Serial.print(client.state());
          delay(2000);
      }
  }
  client.subscribe(topic);
}

void callback(char *topic, byte *payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Message:");
  String s="";
  for (int i = 0; i < length; i++) {
      Serial.print((char) payload[i]);
      s+=(char)payload[i];
  }
  switch(s.toInt())
  {
    case 1: forward();
    break;
    case 2: reverse();
    break;
    case 3: right();
    break;
    case 4: left();
    break;
    default: PWM(EN1,0);
           PWM(EN2,0);
    // default: GLOW(LED1,LOW);
    //         GLOW(LED2,LOW);
    //         GLOW(LED3,LOW);
    //         GLOW(LED4,LOW);
    break;
  }
  Serial.println();
  Serial.println("-----------------------");
}

void loop() {
  client.loop();
}
