# this is a terrible function with bad behavior
def rand_func_1(param1, param2):
    """print a statement param1 and 2 do nothing."""
    
    return "This is a static function"



#calling the user to input a thing and check
# making body first




def prompt_input(behavior_list, acceptable_inputs, message):
    """prompt message of user input for behavior
        all outputs will be of type string."""
    
    print(message)
    user_input = repeat_ask(behavior_list, acceptable_inputs)
    
    return user_input



def repeat_ask(behavior_list, acceptable_inputs):
    """repeatedly ask ask question untill user enters input that is in
        acceptable list."""
    
    user_input = "-1"
    while not(user_input in acceptable_inputs):
        for i in behavior_list:
            print(i)
        user_input = input(":")
    return user_input





def main():

    var1 = rand_func_1(2, "string") # when a function is evaluated it BECOMES
                                    # the return object
    print(var1)

    print(prompt_input(['behavior 1', 'behavior 2'], ['1', '2'], "choose one brah"))


if __name__=="__main__":
    main()
