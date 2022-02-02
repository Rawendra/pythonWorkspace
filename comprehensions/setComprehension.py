employees = ['ANNA', 'MARK', 'ALITA','NYOMI',"NOMU"]


def getFirstLetter(emp):
    result = 'emp-{}'.format(emp[0:1])
    return result


result = {getFirstLetter(emp) for emp in employees }
print(result)
