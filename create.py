import random 

file = open("image.ppm",'w')

file.write("P3 500 500 256 \n")

for i in range(500):
    for j in range(500):
        file.write(str(random.randint(0,255)) + " " + str(random.randint(0,255)) + " " + str(random.randint(0,255)) + " ") 
    file.write("\n")

file.close()
