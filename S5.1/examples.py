def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print "Warning: divide by zero!"
        return float('NaN') #Not a number
    else: # ELSE IS THE ELSE OF EXCEPT. IT ONLY RUNS IF NO EXCEPTION IS
          # IS CALLED. IT SEEMS TO ME TO BE EXACTLY EQUIVALENT TO PUTTING
          # SOMETHING DIRECTLY IN TRY, SO I DON'T THINK I WILL EVER, EVER
          # USE IT
        return result
    # HOLY SHIT FINALLY IS THE STUPIDEST THING I HAVE EVER HEARD OF
    # IT SUPERCEDES ANY PREVIOUS RETURN STATEMENT, SO YOU CAN'T RETURN OUT OF
    # ANY FUNTION IN AN IF/ELSE IF YOU HAVE A FINALLY STATEMENT
    finally:
        print "executing final clause"
        return 1

print divide('A','B')
