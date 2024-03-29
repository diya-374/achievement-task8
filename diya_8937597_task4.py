#Conversion of weight kg to lb and vice versa
def weight_conversion(weight, presentunit):
    if presentunit.lower() == 'kg':
        new_weight = weight * 2.20462
        return new_weight
    elif presentunit.lower() == 'lb':
        new_weight = weight / 2.20462
        return new_weight
    else:
        return None
#Conversion of length meters to feet and vice versa
def length_conversion(length, presentunit):
    if presentunit.lower() == 'm':
        new_length = length * 3.28084
        return new_length
    elif presentunit.lower() == 'ft':
        new_length = length / 3.28084
        return new_length
    else:
        return None

# User input and output
def main():
    conversion_type = input('Choose what you want to convert ? Enter 1 for weight or 2 for length: ')
    conversion_type = conversion_type.strip()

    if conversion_type == '1':
        weight = float(input('Input weight: '))
        presentunit = input('Input present unit used for the weight (kg or lb): ')
        presentunit = presentunit.strip()
        
        new_weight = weight_conversion(weight, presentunit)
#Display converted weight 
        if new_weight:
            print('The new weight after conversion is {:.2f} {}'.format(new_weight, 'lb' if presentunit.lower() == 'kg' else 'kg'))
        else:
            print('Invalid present unit for weight!')
    elif conversion_type == '2':
        length = float(input('Input length: '))
        presentunit = input('Input present unit used for the length (m or ft): ')
        presentunit = presentunit.strip()
        
        new_length = length_conversion(length, presentunit)
#Display converted length
        if new_length:
            print('The new length after conversion is {:.2f} {}'.format(new_length, 'ft' if presentunit.lower() == 'm' else 'm'))
        else:
            print('Invalid present unit for length!')
    else:
        print('Invalid conversion type!')
main()