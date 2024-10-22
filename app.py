pip install streamlit
import streamlit as st
import math

# Define the basic calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def exponent(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def log(x):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive values."
    else:
        return math.log(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Streamlit App
st.title("Scientific Calculator")

operation = st.selectbox("Choose operation:", 
                         ["Add", "Subtract", "Multiply", "Divide", 
                          "Exponent", "Square Root", "Logarithm", 
                          "Sine", "Cosine", "Tangent"])

# Operations with two inputs
if operation in ["Add", "Subtract", "Multiply", "Divide", "Exponent"]:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Exponent":
            result = exponent(num1, num2)
        
        st.write(f"Result: {result}")

# Square root, logarithm, and trigonometric functions with one input
elif operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent"]:
    num = st.number_input("Enter the number/angle", value=0.0)
    
    if st.button("Calculate"):
        if operation == "Square Root":
            result = square_root(num)
        elif operation == "Logarithm":
            result = log(num)
        elif operation == "Sine":
            result = sin(num)
        elif operation == "Cosine":
            result = cos(num)
        elif operation == "Tangent":
            result = tan(num)
        
        st.write(f"Result: {result}")
