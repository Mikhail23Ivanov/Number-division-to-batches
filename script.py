import itertools
from collections import Counter

TESTLIST = [34060,56380,294000,14536,45800,72328,16959,11722.15,203104,39785.7]
PERCENTAGE = 0.4

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
            print(score)
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
    print("40% batch is ", batch40)
    print("60% batch is ", batch60)
    print("The diffenrence between ideal split is ", dif)

main(TESTLIST)
    
