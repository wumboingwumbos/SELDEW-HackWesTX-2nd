#include "Arduino_LED_Matrix.h"
#include "Timer.h"
//*********************ULTRASONIC********************//
// Define the pin numbers for the ultrasonic sensor
const int echoPin = 3;
const int trigPin = 4;
bool running = 0;
float t_time = 0;
int s_time = 0;
int s_timeInt=0;
int user;
int day=5;
int dayinc=0;
// List of usernames
char users[4][10] = {"Nathan", "Johnny", "Leo", "Smarajit"};

// List of location IDs
char locations[3][10] = {"Bathroom1", "Bathroom2", "Kitchen"};

struct SESSION {
  char name[25];
  int waterTime;
  char locID[10];
};

Timer timer;
ArduinoLEDMatrix matrix;

const uint32_t happy[] = {
    0x19819,
    0x80000001,
    0x81f8000
};

const uint32_t heart[] = {
    0x3184a444,
    0x44042081,
    0x100a0040
};

void setup() {
  Serial.begin(9600);                    // Start serial communication with a baud rate of 9600
  matrix.begin();
  pinMode(echoPin, INPUT);               // Set echo pin as input
  pinMode(trigPin, OUTPUT);              // Set trig pin as output
  Serial.println("Ultrasonic sensor:");  // Print a message indicating the ultrasonic sensor is ready
}  

void loop() {
  float distance = readDistance();  // Call the function to read the sensor data and get the distance
  delay(50);                        // Delay for 50 milliseconds before repeating the loop

  if (distance > 20) {
    sessionStart(1);
    matrix.loadFrame(happy);
  } else {
    sessionStart(0);
    matrix.loadFrame(heart);
  }
}

// Function to read the sensor data and calculate the distance
float readDistance() {
  digitalWrite(trigPin, LOW);   // Set trig pin to low to ensure a clean pulse
  delayMicroseconds(2);         // Delay for 2 microseconds
  digitalWrite(trigPin, HIGH);  // Send a 10 microsecond pulse by setting trig pin to high
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);   // Set trig pin back to low
  // Measure the pulse width of the echo pin and calculate the distance value
  float distance = pulseIn(echoPin, HIGH) / 58.00;  // Formula: (340m/s * 1us) / 2
  return distance;
}

// Function to select a random user
char* getRandomUser() {
  int randomIndex = random(0, 4);  // Get a random number between 0 and 3 (for 4 users)
  return users[randomIndex];       // Return the selected user
}

// Function to select a random location ID
char* getRandomLocation() {
  int randomIndex = random(0, 3);  // Get a random number between 0 and 3 (for 4 locations)
  return locations[randomIndex];   // Return the selected location
}

float sessionStart(bool turnOff) {
  if (turnOff && !running) {
    running = 1;
    s_time = (timer.read());
    //s_timeInt=(int)(s_time);
    t_time += (timer.read());
    
    // Get a random user and random location for the session
    char* randomUser = getRandomUser();
    char* randomLocation = getRandomLocation();
    
    SESSION thisSession;
    strncpy(thisSession.name, randomUser, sizeof(thisSession.name));  // Copy the random username
    thisSession.waterTime = s_time;
    strncpy(thisSession.locID, randomLocation, sizeof(thisSession.locID));  // Copy the random location ID

    SendSession(thisSession);
    timer.stop();
  } else if (!turnOff && running) {
    running = 0;
    //Serial.println("Session Start...");
    timer.start();
  }
}

void SendSession(SESSION sesToPrint) {
  //Serial.print("{Time: ");
  
  //Serial.print(" ms, User: ");
  Serial.print(sesToPrint.name);
  Serial.print(",");
  Serial.print(sesToPrint.waterTime);
  Serial.print(",");
  //Serial.print(", Location ID: ");
  Serial.print(sesToPrint.locID);
  Serial.print(",");
  Serial.print("09/");
  Serial.print(day);
  Serial.println("/2024");
  if(dayinc==5){
    dayinc=0;
    if(day>31){
      day==0;
    }
    else{
      day++;
    }
  }
  dayinc++;
}
