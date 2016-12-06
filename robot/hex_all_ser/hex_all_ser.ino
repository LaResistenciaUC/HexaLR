#include <PololuMaestro.h>
#define maestroSerial SERIAL_PORT_HARDWARE_OPEN
#define LOWER_PULSE 496
#define UPPER_PULSE 2496
#define BUF_SIZE 18

#define FRONT_LEFT_TIBIA 0
#define FRONT_LEFT_FEMUR 1
#define FRONT_LEFT_COXA 2

#define FRONT_RIGHT_TIBIA 3
#define FRONT_RIGHT_FEMUR 4
#define FRONT_RIGHT_COXA 5

#define MID_LEFT_TIBIA 6
#define MID_LEFT_FEMUR 7
#define MID_LEFT_COXA 8

#define MID_RIGHT_TIBIA 9
#define MID_RIGHT_FEMUR 10
#define MID_RIGHT_COXA 11

#define REAR_LEFT_TIBIA 12
#define REAR_LEFT_FEMUR 13
#define REAR_LEFT_COXA 14

#define REAR_RIGHT_TIBIA 16
#define REAR_RIGHT_FEMUR 15
#define REAR_RIGHT_COXA 17

MiniMaestro maestro(maestroSerial);
byte angles[BUF_SIZE];

void pre_fill();
void fill_list(byte *data, int n, int size_array);
int sum_arr(byte data[]);
int qmcs(int deg);

void setup() {
  fill_list(angles, 90, BUF_SIZE);
  Serial.begin(115200);
  Serial3.begin(115200);
  maestroSerial.begin(9600);
}

void loop() {
  // Read data from ESP
  if (Serial3.available()) {
    Serial3.readBytes(angles, BUF_SIZE);
    Serial.println("Received data! Sending confirm...");
    // 'c' is 99 ASCII
    Serial3.write(99);
  }
  // Set servo positions
  maestro.setTarget(FRONT_LEFT_TIBIA, qmcs(angles[FRONT_LEFT_TIBIA]));
  maestro.setTarget(FRONT_LEFT_FEMUR, qmcs(angles[FRONT_LEFT_FEMUR]));
  maestro.setTarget(FRONT_LEFT_COXA, qmcs(angles[FRONT_LEFT_COXA]));
  
  maestro.setTarget(FRONT_RIGHT_TIBIA, qmcs(angles[FRONT_RIGHT_TIBIA]));
  maestro.setTarget(FRONT_RIGHT_FEMUR, qmcs(angles[FRONT_RIGHT_FEMUR]));
  maestro.setTarget(FRONT_RIGHT_COXA, qmcs(angles[FRONT_RIGHT_COXA]));
  
  maestro.setTarget(MID_LEFT_TIBIA, qmcs(angles[MID_LEFT_TIBIA]));
  maestro.setTarget(MID_LEFT_FEMUR, qmcs(angles[MID_LEFT_FEMUR]));
  maestro.setTarget(MID_LEFT_COXA, qmcs(angles[MID_LEFT_COXA]));
  
  maestro.setTarget(MID_RIGHT_TIBIA, qmcs(angles[MID_RIGHT_TIBIA]));
  maestro.setTarget(MID_RIGHT_FEMUR, qmcs(angles[MID_RIGHT_FEMUR]));
  maestro.setTarget(MID_RIGHT_COXA, qmcs(angles[MID_RIGHT_COXA]));
  
  maestro.setTarget(REAR_LEFT_TIBIA, qmcs(angles[REAR_LEFT_TIBIA]));
  maestro.setTarget(REAR_LEFT_FEMUR, qmcs(angles[REAR_LEFT_FEMUR]));
  maestro.setTarget(REAR_LEFT_COXA, qmcs(angles[REAR_LEFT_COXA]));
  
  maestro.setTarget(REAR_RIGHT_TIBIA, qmcs(angles[REAR_RIGHT_TIBIA]));
  maestro.setTarget(REAR_RIGHT_FEMUR, qmcs(angles[REAR_RIGHT_FEMUR]));
  maestro.setTarget(REAR_RIGHT_COXA, qmcs(angles[REAR_RIGHT_COXA]));
  // Delay main loop  
  delay(20);
}

void pre_fill() {
  for (int i = 0; i < BUF_SIZE; i++) {
    angles[i] = 0;
  }
}

void fill_list(byte *data, int n, int size_array) {
  for (int i = 0; i < size_array; i++) {
    *(data+i) = n;
  }
}

int sum_arr(byte data[]) {
  int summ = 0;
  for (int i = 0; i < sizeof(data) - 1; i++) {
    summ += data[i];
  }
  return summ;
}

int qmcs(int xdeg) {
  int deg = 1.40625*xdeg - 180;
  return map(deg, 0, 180, LOWER_PULSE * 4, UPPER_PULSE * 4);
}


