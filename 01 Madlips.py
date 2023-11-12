def get_input(user_word):
    my_word=input(f'Enter the {user_word}:')
    return my_word
    
name_1=get_input('name 1')
verb_1=get_input("verb 1")
name_2=get_input('name 2')
verb_2=get_input('verb 2 ')

my_story=f""" In the quirky town of Gigglesville, two pals, {name_1} and {name_2},
            set out on a wild mission—to {verb_1} cats synchronized swimming. 
             
             {name_1}, armed with a pool noodle,
             and {name_2}, armed with a rubber ducky, faced the challenge head-on.
             
             As they tried to {verb_2} the cats to do a perfect backflip, chaos ensued,
             with wet fur and confused felines. 
             
             In the end, though, the cats didn't quite master synchronized swimming,
            but {name_1} and {name_2} sure mastered the art of laughter in Gigglesville.  """

print(my_story)