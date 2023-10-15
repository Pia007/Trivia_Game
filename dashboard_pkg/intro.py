import fontstyle

def show_intro():

    text = fontstyle.apply('|                Welcome to Trivia Game                  |', 'bold/italic/cyan')
    
    border_side = fontstyle.apply('|                                                        |', 'bold/italic/cyan')
    border_horizontal = fontstyle.apply('------------------------------------------------------', 'bold/italic/cyan')
    mid_horizontal = fontstyle.apply('|    🌟-------------------------------------------🌟     |', 'bold/italic/cyan')
    dash_options_1 = fontstyle.apply('|     | 1. Instructions      |     2. Play Game    |     |', 'bold/italic/cyan')
    dash_options_2 = fontstyle.apply('|     | 3. Stats             |     4. Exit         |     |', 'bold/italic/cyan')
    print("")

    # print(text)
    # print(border_side)


    print(f"🌟{border_horizontal}⭐")
    print(border_side)
    print(text) 
    print(border_side)                    
    print(border_side)                    
    print(border_side)  
    print(mid_horizontal) 
    print(dash_options_1)  
    print(mid_horizontal)               
    print(dash_options_2)   
    print(mid_horizontal)   
    print(border_side)                    
    print(border_side) 
    print(f"🌟{border_horizontal}⭐")
    
    