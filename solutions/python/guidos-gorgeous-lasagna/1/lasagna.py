EXPECTED_BAKE_TIME = 40
   # """ Ammount of time it takes to bake a cake according to the recipe book
    
    #"""
def bake_time_remaining(time):
    """ Time left to bake
    
    """
    return EXPECTED_BAKE_TIME - time
    
def preparation_time_in_minutes(number_of_layers):
    """Lyaers

    """
    return number_of_layers * 2

    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Time in minutes
    
    """
    return elapsed_bake_time + 2 * number_of_layers
