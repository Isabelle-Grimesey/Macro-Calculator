from taipy.gui import Gui

input_nutrition_specs = """
**Input macro goals:**
<|{cal}|number|label=Total number of calories|>
<|{perc_carb}|number|label=% carb|>
<|{perc_fat}|number|label=% fat|>
<|{perc_protein}|number|label=% protein|>
"""
input_meal = """
**Input 3 Food Items:**
<|layout|columns=6*300px|

Name:        &emsp;                     <|{food1}|input|> <|{food2}|input|> <|{food3}|input|>

Grams of carbs per serving:                <|{carb_f1}|number|> <|{carb_f2}|number|> <|{carb_f3}|number|>

Grams of fat per serving:                  <|{fat_f1}|number|> <|{fat_f2}|number|> <|{fat_f3}|number|>

Grams of protein per serving:              <|{protein_f1}|number|> <|{protein_f2}|number|> <|{protein_f3}|number|>

(Optional) Number of units per serving: <|{conversion_factor_f1}|number|> <|{conversion_factor_f2}|number|> <|{conversion_factor_f3}|number|>

(Optional) Type of units:               <|{unit_f1}|input|> <|{unit_f2}|input|> <|{unit_f3}|input|>

|>
"""
run = """

"""
output = """

"""

if __name__ == "__main__":

    #initialize variables

    cal = 0
    perc_carb = 0
    perc_fat = 0
    perc_protein = 0

    food1 = ""
    food2 = ""
    food3 = ""
    carb_f1 = 0
    carb_f2 = 0
    carb_f3 = 0
    fat_f1 = 0
    fat_f2 = 0
    fat_f3 = 0
    protein_f1 = 0
    protein_f2 = 0
    protein_f3 = 0
    conversion_factor_f1 = 0
    conversion_factor_f2 = 0
    conversion_factor_f3 = 0
    unit_f1 = ""
    unit_f2 = ""
    unit_f3 = ""

    gui = Gui(page=input_nutrition_specs+input_meal+output)
    gui.run(title="Macro Calculator", dark_mode=True)