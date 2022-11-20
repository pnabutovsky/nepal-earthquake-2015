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

def numeric_damage_grade(damage):
    if damage == 'Grade 1':
        x = 1
    elif damage == 'Grade 2':
        x = 2
    elif damage == 'Grade 3':
        x = 3
    elif damage == 'Grade 4':
        x = 4
    elif damage == 'Grade 5':
        x = 5
    else:
        x = None
    return x

def histogram(frame, indicator, disaggregate_by):
    """
    For any frame with a boolean column "poverty", create a histogram and a percentage
    of the indicator for poverty == True and poverty == False
    """
    x = frame[frame[disaggregate_by]].groupby([indicator]).size().to_frame()
    c = f"{indicator}_{disaggregate_by}_true_count"
    x.rename(columns={0:c}, inplace=True)
    x[f"{indicator}_{disaggregate_by}_true_percentage"] = x[c] / x[c].sum() * 100

    y = frame[~frame[disaggregate_by]].groupby([indicator]).size().to_frame()
    c = f"{indicator}_{disaggregate_by}_false_count"
    y.rename(columns={0:c}, inplace=True)
    y[f"{indicator}_{disaggregate_by}_false_percentage"] = y[c] / y[c].sum() * 100

    return x.join(y)

def histogram_plot(hist, indicator, disaggregate_by):
    hist.plot.bar(y=[f"{indicator}_{disaggregate_by}_true_percentage", f"{indicator}_{disaggregate_by}_false_percentage"])
