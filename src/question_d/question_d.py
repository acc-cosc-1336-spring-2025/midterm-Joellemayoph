#write functions here, don't add input('') statements here!

def get_person_category(age):

    if age >= 20 and age <= 124:
        category = 'Adult'
    elif age >= 13 and age < 20: 
        category = 'Teenager'
    elif age > 1 and age < 13: 
        category = 'Child'
    elif age == 1: 
        category = 'Infant'
    else:
        category = 'Invalid Number'
    return category