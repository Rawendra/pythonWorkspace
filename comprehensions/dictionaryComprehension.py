

employees = [{'name': 'Marc', 'dept': 'HR'},
             {'name': 'Anna', 'dept': 'HR'},
             {'name': 'Rose', 'dept': 'MNGMT'},
             {'name': 'Paula', 'dept': 'IT'},
             {'name': 'Antoine', 'dept': 'IT'}]
depts = {}


def getDeptCount(dept):
    if(dept in depts):
        depts[dept] += 1
    else:
        depts[dept] = 1
    return depts[dept]


departments = {emp['dept']: getDeptCount(emp['dept']) for emp in employees}
print(departments)
countryToCapital = {'UK': 'London',
                    'India': 'NewDelhi', 'Australia': 'Canberra'}
capitalToCountry = {capital: country for country,
                    capital in countryToCapital.items()}
print(capitalToCountry)
