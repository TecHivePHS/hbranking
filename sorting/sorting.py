numbers = [i for i in range(20)]
squares = {i: i**2 for i in range(20)}
odds = (i              # Output expression
        for i          # Input variable
        in range(20)   # Input sequence
        if i % 2 == 1) # Conditional

