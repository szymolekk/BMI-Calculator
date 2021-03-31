from time import sleep

print ('BMI Calculator')
weight = int(input('Input your weight in kilograms : ')) 
height = float(input('Input your height in meters : ')) 
a = weight/(height*height)
bmi = round(a,2)


if bmi < 16.0 :
    print('Your BMI is  : ' , bmi , 'and it means that you have starvation')
elif bmi > 16.1 and bmi < 17 : 
    print('Your BMI is : ' , bmi , 'and it means that you have emaciation ')
elif bmi > 17 and bmi < 18.5 :
    print('Your BMI is : ' , bmi , 'and it means that you have underweight ' )
elif bmi > 18.5 and bmi < 25 : 
    print('Your BMI is : ' , bmi , 'and it means that your weight is perfect')
elif bmi > 25 and bmi < 30 :
    print('Your BMI is : ' , bmi , 'and it means that you have overweight')
elif bmi > 30 and bmi < 35 :
    print('Your BMI is : ' , bmi , 'and it means that you have I degree overweight')
elif bmi > 35 and bmi < 40 :
    print('Your BMI is : ' , bmi , 'and it means that you have II degree overweight')
elif bmi > 40 : 
    print('Your BMI is :' , bmi , 'and it means that you have III degree overweight')
else :
    print('Something went wrong...')
sleep(10)
