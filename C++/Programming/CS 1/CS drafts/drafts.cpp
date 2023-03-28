#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 4;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}

void updateButtons() {

  unsigned long currentMillis = millis();

  bool button1State = !digitalRead(button1_pin);
  bool button2State = !digitalRead(button2_pin);

  if (button1State)
  {
    if (!firstButtonPressed || (firstButtonPressed && currentMillis - previousMillisButton1 >= (firstButtonPressed ? 300 : 1000))) 
    {
      number = (number + 1) % 16;
      previousMillisButton1 = currentMillis;
    }
    firstButtonPressed = true;

  } else 
  {
    firstButtonPressed = false;
  }

  if (button2State) 
  {
    if (!secondButtonPressed || (secondButtonPressed && currentMillis - previousMillisButton2 >= (secondButtonPressed ? 300 : 1000))) 
    {
      number = (number - 1) % 16;
      if (number < 0) number += 16;
      previousMillisButton2 = currentMillis;
    }
    secondButtonPressed = true;

  } else 
  {
    secondButtonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}

void updateButtons() {

  unsigned long currentMillis = millis();

  bool button1State = !digitalRead(button1_pin);
  bool button2State = !digitalRead(button2_pin);

  if (button1State) {

    if (!firstButtonPressed || (firstButtonPressed && currentMillis - previousMillisButton1 >= (firstButtonPressed ? 300 : 1000))) {

      number = (number + 1) % 16;
      previousMillisButton1 = currentMillis;

    }
    firstButtonPressed = true;

  } else 
  {
    firstButtonPressed = false;
  }

  if (button2State) {

    if (!secondButtonPressed || (secondButtonPressed && currentMillis - previousMillisButton2 >= (secondButtonPressed ? 300 : 1000))) 
    {

      number = (number + 15) % 16;
      previousMillisButton2 = currentMillis;

    }
    secondButtonPressed = true;

  } else 
  {
    secondButtonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void handleButton(bool buttonState, bool &buttonPressed, unsigned long &previousMillis, int increment) 
{
  unsigned long currentMillis = millis();

  if (buttonState) 
  {
    if (!buttonPressed || (buttonPressed && currentMillis - previousMillis >= (buttonPressed ? 300 : 1000))) 
    {
      number = (number + increment + 16) % 16;
      previousMillis = currentMillis;
    }
    
    buttonPressed = true;
  } else 
  {
    buttonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void updateButtons() {
  bool firstButtonState = !digitalRead(button1_pin);
  bool secondButtonState = !digitalRead(button2_pin);

  handleButton(firstButtonState, firstButtonPressed, previousMillisButton1, 1);
  handleButton(secondButtonState, secondButtonPressed, previousMillisButton2, -1);
}

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void handleButton(bool buttonState, bool &buttonPressed, unsigned long &previousMillis, int increment) 
{
  unsigned long currentMillis = millis();

  if (buttonState) 
  {
    if (!buttonPressed || (buttonPressed && currentMillis - previousMillis >= (buttonPressed ? 300 : 1000))) 
    {
      number = (number + increment + 16) % 16;
      previousMillis = currentMillis;
    }
    
    buttonPressed = true;
  } else 
  {
    buttonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void updateButtons() {
  bool firstButtonState = !digitalRead(button1_pin);
  bool secondButtonState = !digitalRead(button2_pin);

  handleButton(firstButtonState, firstButtonPressed, previousMillisButton1, 1);
  handleButton(secondButtonState, secondButtonPressed, previousMillisButton2, -1);
}

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillis = 0;
unsigned long buttonStateMillis[numButtons] = {0};
bool buttonPressed[numButtons] = {false};

void handleButton(int btn_idx, int increment, unsigned long &previousButtonMillis) {
  bool buttonState = !digitalRead(buttonPins[btn_idx]);
  unsigned long currentMillis = millis();

  if (buttonState) {
    if (!buttonPressed[btn_idx]) {
      // initial button press
      buttonPressed[btn_idx] = true;
      number = (number + increment + 16) % 16;
      previousButtonMillis = currentMillis;
    } else if (currentMillis - previousButtonMillis >= 1000 && (currentMillis - previousButtonMillis - 1000) % 300 == 0) {
      // periodic button press every 300ms after 1000ms delay
      number = (number + increment + 16) % 16;
      previousButtonMillis = currentMillis;
    }
  } else {
    buttonPressed[btn_idx] = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void updateButtons() {
  unsigned long currentMillis = millis();
  
  handleButton(0, 1, buttonStateMillis[0]);
  handleButton(1, -1, buttonStateMillis[1]);
  
  // Reset button state if both buttons are pressed simultaneously
  if (buttonPressed[0] && buttonPressed[1]) 
  {
    buttonStateMillis[0] = currentMillis;
    buttonStateMillis[1] = currentMillis;
  }
}

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  unsigned long currentMillis = millis();
  if ((currentMillis - previousMillis) >= 10) 
  {
    updateButtons();
    displayNumberBin();
    previousMillis = currentMillis;
  }
  for (int i = 0; i < numButtons; i++) 
  {
    bool buttonState = !digitalRead(buttonPins[i]);
    if (!buttonState) 
    {
      buttonPressed[i] = false;
    }
  }
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

constexpr int activational = 1000;
constexpr int periodical = 300;

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void Count(bool increment) {
  int valueToAdd = increment ? 1 : -1;
  number = (number + valueToAdd + 16) % 16;
  displayNumberBin();
}

void handleButton(int btn_idx, unsigned long currentMillis) {
  static unsigned long pressedTimes[numButtons] = {0};
  static bool buttonStates[numButtons] = {false, false};

  bool buttonState = !digitalRead(buttonPins[btn_idx]);

  if (buttonState != buttonStates[btn_idx]) {
    if (buttonState) {
      Count(btn_idx == 0);
      pressedTimes[btn_idx] = currentMillis;
    }
    buttonStates[btn_idx] = buttonState;
  } else if (buttonState && currentMillis - pressedTimes[btn_idx] >= activational) {
    Count(btn_idx == 0);
    pressedTimes[btn_idx] += periodical;
  }
}

void updateButtons() {
  unsigned long currentMillis = millis();
  for (int i = 0; i < numButtons; ++i) {
    handleButton(i, currentMillis);
  }
}

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 4;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}

void updateButtons() {

  unsigned long currentMillis = millis();

  bool button1State = !digitalRead(button1_pin);
  bool button2State = !digitalRead(button2_pin);

  if (button1State)
  {
    if (!firstButtonPressed || (firstButtonPressed && currentMillis - previousMillisButton1 >= (firstButtonPressed ? 300 : 1000))) 
    {
      number = (number + 1) % 16;
      previousMillisButton1 = currentMillis;
    }
    firstButtonPressed = true;

  } else 
  {
    firstButtonPressed = false;
  }

  if (button2State) 
  {
    if (!secondButtonPressed || (secondButtonPressed && currentMillis - previousMillisButton2 >= (secondButtonPressed ? 300 : 1000))) 
    {
      number = (number - 1) % 16;
      if (number < 0) number += 16;
      previousMillisButton2 = currentMillis;
    }
    secondButtonPressed = true;

  } else 
  {
    secondButtonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}

void updateButtons() {

  unsigned long currentMillis = millis();

  bool button1State = !digitalRead(button1_pin);
  bool button2State = !digitalRead(button2_pin);

  if (button1State) {

    if (!firstButtonPressed || (firstButtonPressed && currentMillis - previousMillisButton1 >= (firstButtonPressed ? 300 : 1000))) {

      number = (number + 1) % 16;
      previousMillisButton1 = currentMillis;

    }
    firstButtonPressed = true;

  } else 
  {
    firstButtonPressed = false;
  }

  if (button2State) {

    if (!secondButtonPressed || (secondButtonPressed && currentMillis - previousMillisButton2 >= (secondButtonPressed ? 300 : 1000))) 
    {

      number = (number + 15) % 16;
      previousMillisButton2 = currentMillis;

    }
    secondButtonPressed = true;

  } else 
  {
    secondButtonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void handleButton(bool buttonState, bool &buttonPressed, unsigned long &previousMillis, int increment) 
{
  unsigned long currentMillis = millis();

  if (buttonState) 
  {
    if (!buttonPressed || (buttonPressed && currentMillis - previousMillis >= (buttonPressed ? 300 : 1000))) 
    {
      number = (number + increment + 16) % 16;
      previousMillis = currentMillis;
    }
    
    buttonPressed = true;
  } else 
  {
    buttonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void updateButtons() {
  bool firstButtonState = !digitalRead(button1_pin);
  bool secondButtonState = !digitalRead(button2_pin);

  handleButton(firstButtonState, firstButtonPressed, previousMillisButton1, 1);
  handleButton(secondButtonState, secondButtonPressed, previousMillisButton2, -1);
}

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}
----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillisButton1 = 0;
unsigned long previousMillisButton2 = 0;

bool firstButtonPressed = false;
bool secondButtonPressed = false;

void handleButton(bool buttonState, bool &buttonPressed, unsigned long &previousMillis, int increment) 
{
  unsigned long currentMillis = millis();

  if (buttonState) 
  {
    if (!buttonPressed || (buttonPressed && currentMillis - previousMillis >= (buttonPressed ? 300 : 1000))) 
    {
      number = (number + increment + 16) % 16;
      previousMillis = currentMillis;
    }
    
    buttonPressed = true;
  } else 
  {
    buttonPressed = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void updateButtons() {
  bool firstButtonState = !digitalRead(button1_pin);
  bool secondButtonState = !digitalRead(button2_pin);

  handleButton(firstButtonState, firstButtonPressed, previousMillisButton1, 1);
  handleButton(secondButtonState, secondButtonPressed, previousMillisButton2, -1);
}

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  updateButtons();
  displayNumberBin();
}
----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long previousMillis = 0;
unsigned long buttonStateMillis[numButtons] = {0};
bool buttonPressed[numButtons] = {false};

void handleButton(int btn_idx, int increment, unsigned long &previousButtonMillis) {
  bool buttonState = !digitalRead(buttonPins[btn_idx]);
  unsigned long currentMillis = millis();

  if (buttonState) {
    if (!buttonPressed[btn_idx]) {
      // initial button press
      buttonPressed[btn_idx] = true;
      number = (number + increment + 16) % 16;
      previousButtonMillis = currentMillis;
    } else if (currentMillis - previousButtonMillis >= 1000 && (currentMillis - previousButtonMillis - 1000) % 300 == 0) {
      // periodic button press every 300ms after 1000ms delay
      number = (number + increment + 16) % 16;
      previousButtonMillis = currentMillis;
    }
  } else {
    buttonPressed[btn_idx] = false;
  }
}

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void updateButtons() {
  unsigned long currentMillis = millis();
  
  handleButton(0, 1, buttonStateMillis[0]);
  handleButton(1, -1, buttonStateMillis[1]);
  
  // Reset button state if both buttons are pressed simultaneously
  if (buttonPressed[0] && buttonPressed[1]) 
  {
    buttonStateMillis[0] = currentMillis;
    buttonStateMillis[1] = currentMillis;
  }
}

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
}

void loop() {
  unsigned long currentMillis = millis();
  if ((currentMillis - previousMillis) >= 10) 
  {
    updateButtons();
    displayNumberBin();
    previousMillis = currentMillis;
  }
  for (int i = 0; i < numButtons; i++) 
  {
    bool buttonState = !digitalRead(buttonPins[i]);
    if (!buttonState) 
    {
      buttonPressed[i] = false;
    }
  }
}

----------------------------------------------------------

#include "funshield.h"

constexpr int ledPins[] = {led4_pin, led3_pin, led2_pin, led1_pin};
constexpr int buttonPins[] = {button1_pin, button2_pin};
constexpr int activation = 1000;
constexpr int periodical = 300;
constexpr int numLeds = 4;
constexpr int numButtons = 2;
int number = 0;

unsigned long pressedTimes[numButtons];
bool buttonStates[numButtons];

void displayNumberBin() {
  for (int i = 0; i < numLeds; i++) {
    int light = (number & (1 << i)) ? ON : OFF;
    digitalWrite(ledPins[i], light);
  }
}

void Counter(bool increment) {
  int valueToAdd = increment ? 1 : -1;
  number = (number + valueToAdd + 16) % 16;
  displayNumberBin();
}


void Buttons() {

  unsigned long currentMillis = millis();

  for (int i = 0; i < numButtons; ++i) {

    bool buttonState = !digitalRead(buttonPins[i]);

    if (buttonState != buttonStates[i]) {

      if (buttonState) {

        Counter(i == 0);
        pressedTimes[i] = currentMillis;

      }

      buttonStates[i] = buttonState;
    }
    else if (buttonState && currentMillis - pressedTimes[i] >= activation) {

      Counter(i == 0);
      pressedTimes[i] += periodical;
      
    }
  }
}

void setup() {
  for (int i = 0; i < numLeds; i++)
  {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], OFF);
  }
  for (int i = 0; i < numButtons; i++) pinMode(buttonPins[i], INPUT);
  for (int i = 0; i < numButtons; ++i) {
    pressedTimes[i] = 0;
    buttonStates[i] = false;
  }
}

void loop() {
  Buttons();
}
