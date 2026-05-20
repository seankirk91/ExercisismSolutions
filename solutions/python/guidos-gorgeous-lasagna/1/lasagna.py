
EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """ Calculate the remaining baking time.

    Parameters:
        elapsed_bake_time (int): How much time the lasagna has been baking.
    
    Returns:
        int: The amount of time the lasagna has spent in the oven.
    
    Subtracts the amount of time the lasagna has been in the oven from the expected time for the recipe.

    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(number_of_layers):
    """ Calculate the preparation time for the lasagna.

    Parameters:
        number_of_layers (int): The number of layers of our lasagna.
    
    Returns:
        int: The amount of time the lasagna will/ did take to prepare 
    
    Multiplies the preparation time for a single layer by the number of layers.

    """
    return PREPARATION_TIME * number_of_layers



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculate the current amount of time spent on the lasagna.

    Parameters:
        elapsed_bake_time (int): How much time the lasagna has been baking.
        number_of_layers (int): The number of layers of our lasagna.
    
    Returns:
        int: The amount of time spent preparing the lasagna so far.
    
    Multiplys the number of layers by the prep time, adding the result to amount of time spent baking the lasagna.

    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time

