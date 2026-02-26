
# Demo code not  correct

# holiday is not defined in this context
# Will throw an error stating that holiday is not defined
#if holiday:
#    if weather == "sunny":
#        print('Go to the beach!')
#    else:
#        print('Stay home and enjoy your holiday!')
#else:
#    print('Work is waiting on you!')

# CORRECTED CODE
#  holiday must be defined first
#  here holiday is defined as False

holiday = False

if holiday:
    if weather == "sunny":
        print('Go to the beach!')
    else:
        print('Stay home and enjoy your holiday!')
else:
    print('Work is waiting on you!')

