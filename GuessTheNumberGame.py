import sys
import random

sys.stdout.buffer.write(b'This is a game where you guess a random number between a specified minimum and maximum value\n')

sys.stdout.buffer.write(b'Please enter the minimum value\n')
sys.stdout.flush()
n = sys.stdin.buffer.readline().decode()

sys.stdout.buffer.write(b'Please enter the maximum value\n')
sys.stdout.flush()
m = sys.stdin.buffer.readline().decode()
randomNum = random.randint(int(n), int(m))

while True:
    sys.stdout.buffer.write(b'Please your enter answer\n')
    sys.stdout.flush()
    userIn = sys.stdin.buffer.readline().decode()
    if(randomNum == int(userIn)):
        sys.stdout.buffer.write(b'Correct!!\n')
        sys.stdout.flush()
        break
    else: 
        sys.stdout.buffer.write(b'Oh dear! That is not right!\n')
        sys.stdout.flush()


