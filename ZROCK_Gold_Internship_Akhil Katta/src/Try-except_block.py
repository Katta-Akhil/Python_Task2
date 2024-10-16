def divide_numbers(a, b):
    try:
        
        result = a / b
        print(f"Result of division: {result}")
    except TypeError:
        
        print("TypeError: Both inputs must be numbers!")
    except ZeroDivisionError:
        
        print("Error: Division by zero is not allowed!")
    except Exception as e:
        
        print(f"An error occurred: {e}")

divide_numbers(10, 3)    
divide_numbers(10, 'a')  

        
 
