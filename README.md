This script divides numbers in list into two batches to fit sum of one of the batches (primary batch) as close to preset percentage of the whole sum as possible using all combinations from the list. 

Example:
List of numers [1,5,3,2,5]
Percentage 60%

Output:
60.0 % batch is  [5, 3, 2]
40.0 % batch is  [1, 5]
The diffenrence between ideal split is  0.40000000000000036




WARNING: if the ideal fit doesn't have at least one number in the primary batch it won't show the correct answer. The program assumes that there is at least one element in primary batch. 
There is a couple of ways how to work around it, but the simplest would be to type into program a percentage that is higher than 50%, that way it wil
