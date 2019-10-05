from cs115 import map, filter

'''
function will take an amount and try to match that amount from coin valuable
and then return the amount of coins that it took to do it

take amount and see all possible combinations of this addition
take all options and return the combination with the lowest coins count
use it or lose it

amount == max of the coin value
coins == list of the coin value

function that takes the amount (max) value and then the coins that can be used to fill \
the vaule

'''
    


def change(amount, coins):
    #takes an amount of currency and a list coin values and calcs most efficient combo

    if amount == 0:
        return 0
    #if the amount has not changed yet AND the coins list was entered empty or has become empty
    #return the value 0

    elif coins == []:
        return float('inf')
    #if the amount is less than or equal to 0 OR the coins list is empty
    #return 0

    elif coins[0] > amount:
        return change(amount, coins[1:])
    #if the first element in the coins list is greater than the amount
    #recursively move onto the next rest of the elements of the list, starting at L[1:]

    else:
    #if the first element in the coins is less than the amount entered
        lose = change(amount, coins[1:])
        #recursively move onto the next element of the coin list at L[1:]
        
            #PROBLEM: Leads to (amount, []) every time
        
        use = 1 + change(amount - coins[0], coins)
        #add 1 to the sequence count and then recursively call change again with the \
        #amount = amount - coins[0] for the rest of the coins list

        return min(use, lose)


        #take the smallest option out the use or lose variables
    '''
    *PROBLEM*
    lose produces the value 0 every time so when the min is taken at this point \
    the vaule 0 will be given as the min every time which is not good

    *SOLUTION*
    need to find a way to get all the use and lose values cancatinated in a list and \
    find the min value of those items when theyre all in there
    *ADDITION*
    need to also filter this list and take out all elements that have the value \
    *MIN PLACEMENT*
    when i place the reduce outside the elif then it returns 0
    when i place the reduce inside the elif it still returns 0
    '''
        

    #PROBLEM: the min is used only on the 2 current elements and this is a prob \
    #because there is a zero value every time lose runs

    #Need help on how to format that this so the min is not calculated with the zero variable

    #Do I need to filter or map all the data that change produces
    '''
    returns the lower of the two values
    set up in a way that lose will be returned every time
    need to fix so that it will return the min of all the actions instead of lose everytime
    '''
#problem is it is doing the calc right its just that the min is 0 \
#because the lose it function checks the option (48,[])
#print(change(48, [1, 5, 10, 25, 50]))

