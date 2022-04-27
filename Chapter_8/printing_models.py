# when you pass a list to a function, the function can modify the list
# any changes made to the list inside the function's body are permanent,
# allowing you to work efficiently even when you're dealing with large 
# amounts of data

# the following code moves data from one list to another without a function

# start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each design, until none are left.
# move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print("\n")

# we can recognize this code by writing two functions, each of which does
# one specific job

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# this program is easier to extend and maintain than the version without functions
# this technique is more efficient than having to update code separately in several places of the program
# this example also demonstrates the idea that every function should have one specific job
# if you're writing a function and notice the function is doing too many different tasks, try to split the
# code into two functions. Remember that you can always call a function from another function,
# this helps split up a complex task into a series of steps.


# sometimes you'll want to prevent a function from modifying a list
# you can address this issue by passing the function a copy of the list,
# not the original. Any changes the function makes to the list will affect
# only the copy, leaving the original list intact.
# you can send a copy of a list like this:
# function_name(list_name[:])

# if we didn't want to empty the list of unprinted designs in print_models.py,
# we could call print_models() like this:
# print_models(unprinted_designs[:], completed_models)

# its best to send the original list for data efficieny but you may pass a copy if need be