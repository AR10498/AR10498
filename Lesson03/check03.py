def test0301(square_geometry):
    try: 
        assert square_geometry(10)==(40, 100)
        print("Correct result!")
    except NameError: 
        print('Your function is not named "square_geometry"')
    except AssertionError:
        print(f"""Your function does not produce the correct result!
        # expected calling:
        square_geometry(10) 

        # to return the result:
        (40, 100)

        # your function returned: 
        {square_geometry(10)}""")
        
        
def test0302(rectangle_geometry):
    def MODEL_rg(W, H):
        P = 2*W + 2*H
        A = W*H
        return P, A
    ans1 = rectangle_geometry(2,5)
    ans2 = MODEL_rg(2, 5)
    try: 
        assert ans1==ans2
        print("Correct result!")
    except NameError: print('Your function is not named "rectangle_geometry"')
    except AssertionError:
        print(f"""Your function does not produce the correct result!
        # expected calling:
        rectangle_geometry(2,5) 

        # to return the result:
        {ans1}

        # your function returned: 
        {ans2}""")

    
def test0303(twice):
    #test function to give to your twice() function
    def x_squared(x):
        return x**2

    # the x_squared function will be given as an argument to evaluate (x^2)^2
    ### BEGIN HIDDEN TESTS
    print("Test 1.")
    try: 
        assert twice(x_squared, 2) == 16
        print("Correct result!\nIn: twice(x_squared, 2)\nOut: 16\n")
    except NameError: print('Your function is not named "twice"')
    except AssertionError:
        print(f"""Your function does NOT produce the correct result!
        # when trying to pass the x_squared function and the value 2:
        In: twice(x_squared, 2)
        Out: {twice(x_squared, 2)}

        Make sure:
        1. your function takes a function name (without brackets) and a value as two arguments
        2. this dummy-name is used inside the function block in place of a specific function name""")
    ### END HIDDEN TESTS

    from math import sqrt

    # the sqrt function will also be used to evaluate sqrt(sqrt(16))

    ### BEGIN HIDDEN TESTS
    print("Test 2.")
    try: 
        assert twice(sqrt, 16) == 2.0
        print("Correct result!\nIn: twice(sqrt, 16)\nOut: 2.0\n")
    except NameError: print('Your function is not named "twice"')
    except AssertionError:
        print(f"""Your function does NOT produce the correct result!
        # when trying to pass the sqrt function and the value 16:
        In: twice(sqrt, 16)
        Out: {twice(sqrt, 16)}

        Make sure:
        1. your function takes a function name (without brackets) and a value as two arguments
        2. this dummy-name is used inside the function block in place of a specific function name""")
    ### END HIDDEN TESTS
    
    
    