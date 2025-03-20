#prompt customers to input a fruit (case insensitive); ignore input that's not a fruit
def main():
    item = str(input('Item: '))
    calorie_count(item)

#output number of calories of the fruit
def calorie_count(item):
    item = item.lower()
    fruits = {
        'apple' : 130,
        'avocado' : 50,
        'banana' : 110,
        'cantaloupe' : 50,
        'grapefruit' : 60,
        'grapes' : 90,
        'honeydew melon' : 50,
        'kiwifruit' : 90,
        'lemon' : 15,
        'lime' : 20,
        'nectarine' : 60,
        'orange' : 80,
        'peach' : 60,
        'pear' : 100,
        'pineapple' : 50,
        'plums' : 70,
        'strawberries' : 50,
        'sweet cherries' : 100,
        'tangerine' : 50,
        'watermelon' : 80
    }

    for fruit in fruits:
        if item == fruit:
            print('Calories: ', fruits[item])

main()
