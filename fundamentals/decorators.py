def hey_frank_decorator(function):

    def higher_order_function():
        print('HEY FRANK! ')
        function()
        print('please? ')

    return higher_order_function

@hey_frank_decorator
def question():
    print('what time is it')

question()
