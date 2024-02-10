from taipy.gui import Gui

input_nutrition_specs = """

"""
input_meal = """

"""
run = """

"""
output = """

"""

if __name__ == "__main__":

    gui = Gui(page=input_meal+input_nutrition_specs+output)
    gui.run(title="Macro Calculator", dark_mode=True)