#include <Servo.h>
Servo m;
Servo u;
Servo d;
int i,t,c,b;
int x=0;
int y=0;
int j;
void setup()
{
  Serial.begin(9600);
  m.attach(9);
  u.attach(5);
  d.attach(11);
  pinMode(6,INPUT);
  pinMode(7,INPUT);

  m.write(90);
  delay(100);
  u.write(0);
  delay(100);
  d.write(45);
  delay(4000);
  c=90;
  t=0;
  b=45;
  start();
}



void start ()
{
  delay(1500); // up movement
  for(i=c;i>=15;i--)
  {
    m.write(i);
    delay(10);
    c=10;
  }
  delay(1000);
  t=45;
  u.write(t);
  delay(1000);

  for(i=b;i>=0;i--)
  {
    d.write(i);
    delay(10);
    b=0;
  }

  delay(1500); 

  u.write(0);
  delay(1500);
  for(i=c;i<=90;i++) //down movement
  {
    m.write(i);
    delay(10);
    c=90;
  }
  delay(1000);
  t=0;

  digitalWrite(2,LOW);
  digitalWrite(4,HIGH);
  delay(1500);

  digitalWrite(2,LOW);
  digitalWrite(4,LOW);
  delay(1000);

}


class move
{
  public:
    
  void color(int n)
  {
    delay(1500);            
    digitalWrite(2,HIGH);//close grip
    digitalWrite(4,LOW);
    delay(1500);
    for(i=90;i>=15;i--) //up movement of centre and top motor
    {
      m.write(i);
      delay(10);

    }
    delay(1500);
    for(j=0;j<=45;j++) //up movement of centre and top motor
    {
      u.write(j);
      delay(10);

    }
    delay(1500);
    for(i=0;i<=n;i++) //bottom motor
    {
      d.write(i);
      delay(10);

    }
    delay(1500);

    for(j=45;j>=0;j--) //down movement of centre and top
    {
      u.write(j);
      delay(10);
    }
    delay(1500);
    for(i=15;i<=90;i++) //down movement of centre and top
    {
      m.write(i);
      delay(10);


    }
    delay(1500);
    digitalWrite(2,LOW);
    digitalWrite(4,HIGH);
    delay(1500);

    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    delay(1000);

    delay(1500);

    for(i=90;i>=15;i--) //up movement of centre and top
    {
      m.write(i);
      delay(10);
    }
    delay(1500);
    for(j=0;j<=45;j++) //up movement of centre and top
    {
      u.write(j);
      delay(10);
    }
    delay(1500);
    for(i=n;i>=0;i--) // move down to 0
    {
      d.write(i);
      delay(10);

    }
    delay(1500);
    for(j=45;j>=0;j--) //down
    {
      u.write(j);
      delay(10);

    }
    delay(1500);
    for(i=15;i<=90;i++) //down
    {
      m.write(i);
      delay(10);

    }



  }
};
void loop()
{

  x=digitalRead(6);
  y=digitalRead(7);
  if((x==HIGH)&&(y==LOW))
  {
    move b;
    b.color(90);
  }
else if((x==LOW)&&(y==HIGH))
   {
   
   move g;
   g.color(135);
   }
   
   else if((x==HIGH)&&(y==HIGH))
   {
   move r;
   r.color(180);
   }
   else
   {
   }
   
   
   x=LOW;
   y=LOW;
}



