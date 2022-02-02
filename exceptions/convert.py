def convert(s):
    try:
        result=0
        s/0
    except TypeError:
        print('TypeError')
        result ='error'
    except Exception as e:
        print(f'default exception--> {e}')
    print(result)
    return result


convert(123)

