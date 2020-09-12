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
    DigiMouse.delay(1);
  }
}

void moveY(int num) {
  int dir = sign(num);
  for (int i = 0; i < abs(num) ; i++) {
    DigiMouse.moveY(dir);
    DigiMouse.delay(1);
  }
}
void loop() {
  moveX(10);
  moveY(10);
  moveX(-10);
  moveY(-10);
  int prev_color = 0;
  for (int i = 0; i < len ; i++) {
    int axis = axises[i];
    int color = colors[i];
    int distance = distances[i] * 30;
    if(prev_color != color){
      if (color == 1) {
        DigiMouse.setButtons(1 << 0); //left click
      } else {
        DigiMouse.setButtons(0);  //unclick all
      }
    }
    DigiMouse.delay(200);
    
    if (axis == 0) { // x-axis
      moveX(distance);
    } else { // y-axis
      moveY(distance);
    }  

    prev_color = color;
  }
}
