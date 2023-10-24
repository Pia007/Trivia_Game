import fontstyle

def show_intro():

    text = fontstyle.apply('|           Welcome to Trivia Game             |', 'bold/italic/cyan')
    border_side = fontstyle.apply('|                                              |', 'bold/italic/cyan')
    border_horizontal = fontstyle.apply('--------------------------------------------', 'bold/italic/cyan')
    mid_horizontal = fontstyle.apply('| 🌟--------------------------------------🌟   |', 'bold/italic/cyan')
    dash_options_1 = fontstyle.apply('|  |    1. Play        |     2. Exit       |   |', 'bold/italic/cyan')
    # border_horizontal = fontstyle.apply('------------------------------------------------------', 'bold/italic/cyan')
    print("")


    print(f"🌟{border_horizontal}⭐")
    print(border_side)
    print(text) 
    print(border_side)                    
    print(border_side)                    
    print(border_side)  
    print(mid_horizontal) 
    print(dash_options_1)
    print(mid_horizontal)   
    print(border_side)                    
    print(border_side) 
    print(f"🌟{border_horizontal}⭐")



def show_difficulty():
    difficulty_text = fontstyle.apply('       ===  Difficulty Level ===           ', 'bold/italic/yellow')
    difficulty_horizontal = fontstyle.apply('----------------------------------------', 'bold/italic/yellow')
    difficulty_selections = fontstyle.apply('|   1. Easy       |   2. Medium        |', 'bold/italic/yellow')
    difficulty_selections_2 = fontstyle.apply('|   3. Hard       |   4. Home          |', 'bold/italic/yellow')

    print("")   
    print(f"{difficulty_text}")
    print(difficulty_horizontal)
    print(difficulty_selections)
    print(difficulty_horizontal)
    print(difficulty_selections_2)
    print(difficulty_horizontal)
    
    