#include <stdio.h>
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
#include <wiringPi.h>
 
int kbhit(void);
#define in1 0
#define in2 1
#define in3 2
#define in4 3
#define enA 26
#define enB 23


void forward();
void turn_right();
void turn_left();
void stop();
void reverse();

 
int main(void)
{
  wiringPiSetup();
  char last_key='s';
  char new_key='s';
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  pinMode(enA,PWM_OUTPUT);
  pinMode(enB,PWM_OUTPUT);
  
  while(1){
    while(!kbhit()){
        if(new_key!=last_key){
            last_key=new_key;
            switch(new_key){
                case 'w':
                    forward();
                    printf("forward\n");
                    break;
                case 'a':
                    turn_left();
                    printf("left\n");
                    break;
                case 's':
                    stop();
                    printf("stop\n");
                    break;
                case 'd':
                    turn_right();
                    printf("right\n");
                    break;
                case 'r':
                    reverse();
                    printf("reverse\n");
                    break;
                case '1':
                    pwmWrite(enA,310);
                    pwmWrite(enB,310);
                    printf("Brzina 1\n");
                    break;
                case '2':
                    pwmWrite(enA,400);
                    pwmWrite(enB,400);
                    printf("Brzina 2\n");
                    break;
                case '3':
                    pwmWrite(enA,600);
                    pwmWrite(enB,600);
                    printf("Brzina 3\n");
                    break;
                case '0':
                    pwmWrite(enA,0);
                    pwmWrite(enB,0);
                    printf("Brzina 0\n");
                    break;
            }
        }
    }
    new_key=getchar();
  }
  return 0;
}

int kbhit(void)
{
  struct termios oldt, newt;
  int ch;
  int oldf;
 
  tcgetattr(STDIN_FILENO, &oldt);
  newt = oldt;
  newt.c_lflag &= ~(ICANON | ECHO);
  tcsetattr(STDIN_FILENO, TCSANOW, &newt);
  oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
  fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);
 
  ch = getchar();
 
  tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
  fcntl(STDIN_FILENO, F_SETFL, oldf);
 
  if(ch != EOF)
  {
    ungetc(ch, stdin);
    return 1;
  }
 
  return 0;
}

void forward(){
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
    digitalWrite(in3,LOW);
    digitalWrite(in4,HIGH);
}
void turn_right(){
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,HIGH);
}
void turn_left(){
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
}
void stop(){
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
}
void reverse(){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
}

