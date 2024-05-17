'''
def get_inputs():
    height = float(input("Enter height: "))
    weight = float(input("Enter weight: "))
    return height,weight

def calc(height,weight):
    BMI = weight/(height*height)
    return BMI 

def main():
    height,weight = get_inputs()
    BMI = calc(height,weight)
    print("This is the calculated Bmi value:",BMI,type(BMI))

if __name__ == "__main__":
  main()'''

