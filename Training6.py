# y = lambda x : x**2 + 5*x + 2
# print(y(2))

f_x_y = lambda x : x**2 + 5*x +2
newList = [1,2,3,4,5,6]
# print(f_x_y(2,6))
print(list(map(f_x_y,newList)))

# f_string = lambda x : x.title().split()

new_string ="hello how are you ?"

def preprocess_string(x:str)->list:
    y=x.title()
    y=y.split(" ")
    return y

f_string= lambda x: x.title().split(" ")
print(preprocess_string(new_string))


sqr = lambda x : x**2
print(sqr(2))

def get_odd_even_checker(a):
    if a%2 ==0:
        print("number is even")
    else:
        print("Number is odd")
  
# print(get_odd_even_checker(2))

number = [1,2,4,5,7,8,9]
result = map(sqr, number)
print(tuple(result))


ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return True
  else:
    return False

adults =list(filter(myFunc, ages)) 

print(adults)

def get_odd_even(a):
   if a%2==0:
      return True
   else:
      return False
   
cal_age = list(filter(get_odd_even, number))

print(cal_age) 

# package manager in python
# venv-> virtual environment


  









