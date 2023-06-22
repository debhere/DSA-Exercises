'''
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.
'''


def getBestScores(my_list) -> None:
    scores = list(set(my_list.copy()))
    scores.sort(reverse=True)
    print(scores[0], scores[1])


getBestScores([84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0])
