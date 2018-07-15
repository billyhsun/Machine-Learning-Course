#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range (len(net_worths)):
        diff = net_worths[i][0] - predictions[i][0]
        print abs(diff)
        if abs(diff) >= 80:
            continue
        cleaned_data.append((ages[i], net_worths[i], diff))

    print len(cleaned_data)
    return cleaned_data

