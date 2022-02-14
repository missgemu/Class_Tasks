from audioop import avg
from gettext import find
from this import d


def findAverage(dictionary):
    for value in dictionary:
        sumArray = 0
        for i in dictionary[value]:
            sumArray = sumArray + i
            avg = round(sumArray / len(dictionary[value]), 2)
            print(f'the average score for {value} is {str(avg)}')


dictionary = {'Valentine': [30, 40, 60],
              'Romie': [40, 50, 76],
              'Juliet': [49, 67, 64]
              }
findAverage(dictionary)
