#include <DigiMouse.h>
#include "img.h"

void setup() {

  DigiMouse.begin(); //start or reenumerate USB - BREAKING CHANGE from old versions that didn't require this


  DigiMouse.delay(2000);
}

int sign(int value) {
  return int((value > 0) - (value < 0));
}

void moveX(int num) {
  int dir = sign(num);
  for (int i = 0; i < abs(num) ; i++) {
    DigiMouse.moveX(dir);
    DigiMouse.delay(4);
  }
}

void moveY(int num) {
  int dir = sign(num);
  for (int i = 0; i < abs(num) ; i++) {
    DigiMouse.moveY(dir);
    DigiMouse.delay(4);
  }
}
void loop() {
  moveX(10);
  moveY(10);
  moveX(-10);
  moveY(-10);
  for (int i = 0; i < len ; i++) {
    int axis = path[i][0];
    int color = path[i][1];
    int distance = path[i][2];
    if (color == 1) {
      DigiMouse.setButtons(1 << 0); //left click
    } else {
      DigiMouse.setButtons(0);  //unclick all
    }
    
    DigiMouse.delay(50);
    
    if (axis == 0) { // x-axis
      moveX(distance);
    } else { // y-axis
      moveY(distance);
    }  
  }
}
