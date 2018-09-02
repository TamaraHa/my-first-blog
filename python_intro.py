#print('Hello, Django girls!')

#if 3 > 2:
    #print('Math\'s easy, man')
#elif 3 == 2:
    #print('Math is an illusion')
#else:
    #print('Math\'s hard, man')


#def hallo():
    #print('Hallo')
    #print('Wie geht\'s?')

#hallo()

#name = input('What\'s your name, girl? ')

#def hallo(name):
    #print('Hello, \'' + name + '\'')
    #if name == 'Tamara':
        #print('Nice to meet you')
    #elif name != 'Tamara':
        #print('What are you doing at Tamara\'s laptop?')

#hallo(name)

def format_info(name, age, country):
    return 'Student: ' + name + '\nAge: ' + str(age) + '\nCountry: ' + country

print(format_info('Tobias Ledford', 15, 'England'))

Student = {}

for student in range[5]:
    studentnumber = student+1
    name = (input('First name: '), input('Last name: ')
    age = int(input('Age: '))
    country = input('Country of origin: ')
    dict.update(studentnumber, name, age, country)
    print('The student ' + name + 'has the studentnumber ' + studentnumber + ', is ' + age + ' years old and comes from ' + country)
