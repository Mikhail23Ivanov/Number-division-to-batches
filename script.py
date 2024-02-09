import itertools
from collections import Counter

TESTLIST = [1,5,3,2,5]
PERCENTAGE = 0.6

def divideInTwoBaskets(numList):
    suma = sum(numList)
    baskets = getRandomBaskets(numList)
    bestBasket = baskets[0]
    bestScore = abs(float(sum(baskets[0])) - suma*PERCENTAGE)

    for basket in baskets[1:]:
        score = abs(sum(basket) - suma*PERCENTAGE)
        if(score < bestScore):
            bestBasket = basket
            bestScore = abs(sum(basket) - suma*PERCENTAGE)
    return list(bestBasket.elements()), list((Counter(numList) - bestBasket).elements()), bestScore


def getRandomBaskets(numList):
    result = list()
    for r in range(1,len(numList)+1):
        one_list = Counter(itertools.combinations(numList, r))
        list_updated = [Counter(ele) for ele in one_list]

        result.append(list_updated)
    result = list(map(Counter, itertools.chain.from_iterable(result)))

    return result
     
def main(numList):
    batch40, batch60, dif = divideInTwoBaskets(numList)
    print(PERCENTAGE*100, "% batch is ", batch40)
    print((1-PERCENTAGE)*100, "% batch is ", batch60)
    print("The difference between ideal split is ", dif)

main(TESTLIST)
    
