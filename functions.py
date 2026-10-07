def say_hi (name, age):
    print( "hello " +name+ ",your age" + str(age))
    print("top")
    say_hi()
    print("bottom")
   
    say_hi("mike",70)
    say_hi("rick",30)