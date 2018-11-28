'''
AI:Assignment2	4105056005	Yun-Ting Cheng
python 2.7.15
'''
import math
import random

#calculate the travelling length
def total_length(x, y):
	global total_dist
	for i in range(0, len(x)-1):
		distance_list.append(city_distance(x[i],y[i],x[i+1],y[i+1]))
		total_dist += city_distance(x[i],y[i],x[i+1],y[i+1])
	distance_list.append(city_distance(x[len(x)-1],y[len(y)-1],x[0],y[0]))
	total_dist += city_distance(x[len(x)-1],y[len(y)-1],x[0],y[0])
	print(total_dist)

#calculate the distance between two cities(Euclidean distance)
def city_distance(x1, y1, x2, y2):
	return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

def swap_cities(x,y):
	global total_dist
	global check_input
	max_decrease = 0
	a = 0
	b = 0
	new_total = 0
	temp1 = 0
	temp2 = 0
	temp3 = 0
	temp4 = 0
	for i in range(0, len(x)):
		for j in range(0, len(x)):
			if j<=i:
				continue
			#two cities that are currently in sequence
			if (i == 0) and (j != len(x)-1):
				temp_dis1 = city_distance(x[len(x)-1],y[len(y)-1],x[j],y[j])
				temp_dis2 = city_distance(x[i],y[i],x[j+1],y[j+1])
				temp_total = total_dist - distance_list[j] -  distance_list[len(x)-1]
			elif (j == len(x)-1) and (i != 0):
				temp_dis1 = city_distance(x[i-1],y[i-1],x[j],y[j])
				temp_dis2 = city_distance(x[i],y[i],x[0],y[0])
				temp_total = total_dist - distance_list[j] -  distance_list[i-1]
			elif (i != 0) and (j != len(x)-1):
				temp_dis1 = city_distance(x[i-1],y[i-1],x[j],y[j])
				temp_dis2 = city_distance(x[i],y[i],x[j+1],y[j+1])
				temp_total = total_dist - distance_list[j] -  distance_list[i-1]
			temp_total += (temp_dis1 + temp_dis2)
			#two cities that aren't in sequence
			if i != j-1:
				temp_dis3 = city_distance(x[i+1],y[i+1],x[j],y[j])
				temp_dis4 = city_distance(x[i],y[i],x[j-1],y[j-1])
				temp_total -= distance_list[j-1] -  distance_list[i]
				temp_total += (temp_dis1 + temp_dis2)
			#find the swap that has the maximum decrease in the total distance
			if max_decrease < (total_dist - temp_total):
				max_decrease = (total_dist - temp_total)
				a = i
				b = j
				new_total = temp_total
				temp1 = temp_dis1
				temp2 = temp_dis2
				if i != j-1:
					temp3 = temp_dis3
					temp4 = temp_dis4
	if max_decrease != 0:
		print "Swap",
		print a+1,
		print "and",
		print b+1
		x[a] , x[b] = x[b], x[a]
		y[a] , y[b] = y[b], y[a]
		total_dist = new_total
		distance_list[j] = temp2
		if (a == 0) and (b != len(x)-1):
			distance_list[len(x)-1] = temp1
		elif a != 0:
			distance_list[a-1] = temp1
		if a != b-1:
			distance_list[a] = temp3
			distance_list[b-1] = temp4

	else:
		print("End of hill climbing")
		check_input = 1


check_input = 1
distance_list = []
total_dist = 0
while check_input == 1:		#make sure the inputs are integers and the same amounts
	#input x-coordinates
	x_string = raw_input("Input the x-coordinates: ")
	x = x_string.split()
	try:
		x = map(float, x)		#turn str elements to int elements
	except:
		print("Input type error, please input integer.")
		continue

	#input y-coordinates
	y_string = raw_input("Input the y-coordinates: ")
	y = y_string.split()
	try:
		y = map(float, y)		#turn str elements to int elements
	except:
		print("Input type error, please input integer.")
		continue

	if len(x) == len(y):
		check_input = 0;
	else:
		print("Wrong input, the amongs of variables are different.")

print("\nPath:")
print(x)
print(y)
print"\nLength =",
total_length(x,y)
print("")

while True:
	swap_cities(x,y)
	if check_input == 1:
		break
	print(x)
	print(y)
	print"\nLength =",
	print(total_dist)
	print("")

