#Countdown Simulator
import time

print("⏳ COUNTDOWN TIMER SIMULATOR")
number = eval(input("Enter the starting number for count down -->"))

for i in range(number,0,-1):
    print(i)
    time.sleep(1)

print("Liftoff!")