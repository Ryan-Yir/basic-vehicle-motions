int IN1 = 2;
int IN2 = 3;
int IN3 = 4;
int IN4 = 5;
int EN1 = 6;
int EN2 = 7;


void stopMoving(speed);
void moveForward(speed);
void moveLeft(speed);
void moveRight(speed);
void moveBackwards(speed);
.
void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(EN1, OUTPUT);
  pinMode(EN2, OUTPUT);
}
void loop() {
void moveBackwards(speed) {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogueWrite(EN1, speed);
  analogueWrite(EN2, speed); 
}  
  
void moveForward(speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogueWrite(EN1, speed);
  analogueWrite(EN2, speed);
 
}

void moveLeft(speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogueWrite(EN1, speed);
  
}

void moveRight(speed) {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogueWrite(EN2, speed);
 

void stopMoving(speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, HIGH);
  
  
void stp(speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, low);
  digitalWrite(IN3, low);
  digitalWrite(IN4, HIGH);
  
  
  
void rpg(speed) {
  digitalWrite(IN1, low);
  digitalWrite(IN2, low);
  digitalWrite(IN3, low);
  digitalWrite(IN4, low);
  
  
  
  
}

}
