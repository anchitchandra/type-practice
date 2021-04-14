import matplotlib.pyplot as plt
import time as t
times = []
mistakes = 0
print("This program will help you to type fast\n type 'programming' five times:")
input("press enter to continue :")

while len(times) < 5:
    start = t.time()
    word = input("type the word: ")
    end = t.time()
    time_taken = end - start
    times.append(time_taken)
    if word.lower() != "programming":
        mistakes +=1

print(f'you made {mistakes} mistakes')
print("lets take a look at your progress")
t.sleep(3)
plt.ylabel("time taken in seconds")
plt.xlabel("Attempts")
x=[1,2,3,4,5]
y = times
m = ["1st","2nd","3rd","4th","5th"]
plt.title("evolution")
plt.xticks(x,m)
plt.bar(x,y)
plt.show()

