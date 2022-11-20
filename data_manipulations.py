def numeric_income(income_string):
    """
    Converts an income range string to a numeric for further calculations.
    Uses the upper bound on household monthly income range.
    """
    if income_string == 'Rs. 10 thousand':
        x = 10000
    elif income_string == 'Rs. 10-20 thousand':
        x = 20000
    elif income_string == 'Rs. 20-30 thousand':
        x = 30000
    elif income_string == 'Rs. 30-50 thousand':
        x = 40000
    elif income_string == 'Rs. 50 thousand or more':
        x = 60000
    else:
        x = None
    return x

def poverty_histogram(frame, indicator):
    """
    For any frame with a boolean column "poverty", create a histogram and a percentage
    of the indicator for poverty == True and poverty == False
    """
    x = frame[frame['poverty']].groupby([indicator]).size().to_frame()
    c = f"{indicator}_poverty_count"
    x.rename(columns={0:c}, inplace=True)
    x['Poor'] = x[c] / x[c].sum() * 100

    y = frame[~frame['poverty']].groupby([indicator]).size().to_frame()
    c = f"{indicator}_no_poverty_count"
    y.rename(columns={0:c}, inplace=True)
    y['Not Poor'] = y[c] / y[c].sum() * 100

    return x.join(y)

def poverty_histogram_plot(hist):
    hist.plot.bar(y=['Poor', 'Not Poor'])
