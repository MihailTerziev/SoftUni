def age_assignment(*args, **kwargs):
    output = {}
    for name in args:
        output[name] = kwargs.get(name[0])
    return output


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
