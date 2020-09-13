#include <DigiMouse.h>
#include "img.h"

#define scale 10

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
  int prev_color = 0;
  int width_count = 0;
  for (int i = 0; i < len ; i++) {
    int distance = (int)distances[i] ;
    byte color = colors[i];
    if (prev_color != color) {
      if (color == 1) {
        DigiMouse.setButtons(1 << 0); //left click
      } else {
        DigiMouse.setButtons(0);  //unclick all
      }
    }
    DigiMouse.delay(200);

    moveX(distance * scale);

    width_count += distance;
    if (width_count >= width) {
      width_count = 0;
      DigiMouse.delay(200);
      moveX(-width * scale);
      DigiMouse.delay(200);
      moveY(1 * scale);
    }
    prev_color = color;
  }
}
