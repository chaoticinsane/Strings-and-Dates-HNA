while True:
    question="Enter Date: " 
    user_input = input(question)
    if user_input != "-1":
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        if ',' in user_input:
            noComma = user_input.replace(',', '')
            inputArr = noComma.split(' ')
            month = months.index(inputArr[0])
            print(f'{month +1 }/{inputArr[1]}/{inputArr[2]}')
        else:
            print('Date entered is not valid')
    else:
        break 