
source_scale_pick = input('This program helps to convert temperature value from Celsius scale to Fahrenheit scale. \n'
                          'Please choose the scale from which you want to convert value\n'
                          '\'C\' for Celsius or \'F\' for Fshrenheit: ')
convert_scale_pick = input('Please choose the scale into which you want to convert value\n'
                          '\'C\' for Celsius or \'F\' for Fshrenheit: ')
if source_scale_pick == convert_scale_pick:
    print('You entered the same scales. What for?')
else:
    if source_scale_pick == 'C' or source_scale_pick == 'c' and convert_scale_pick == 'F' or convert_scale_pick == 'f':
        C_temp = input('Please, input Celsius temperature value: ')
        F_temp = 9/5 * float(C_temp) + 32
        print(C_temp,'grades in Celsius scale is equal to', F_temp, 'grades in Fahrenheit scale')
    else:
        if source_scale_pick == 'F' or source_scale_pick == 'f' and convert_scale_pick == 'C' or convert_scale_pick == 'c':
            F_temp = input('Please, input Fahrenheit temperature value: ')
            C_temp = (float(F_temp) - 32) * 5 / 9
            print(F_temp, 'grades in Fahrenheit scale is equal to', C_temp, 'grades in Celsius scale')


