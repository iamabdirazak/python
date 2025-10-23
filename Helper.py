# function to return greeting message
def lambda_greet(name):
    return (lambda n: f"Hello, {n}! Welcome to the world of Python.")(name)