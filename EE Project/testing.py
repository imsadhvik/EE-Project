# date='27-06-2021'
passenger_names=['sadhvik','rithvik']
age=['18','10']
gender=['male','male']
price=['1000','500']
temp=[['passenger name','age','gender','price']]
for i in range(len(passenger_names)):
    x=[passenger_names[i],age[i],gender[i],price[i]]
    temp.append(x)
print(temp)