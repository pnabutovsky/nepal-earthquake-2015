import random

def perturb(df, column, gamma, min=None, max=None): 
  if min != None and max != None:
    domain = list(range(min, max))
  else:
    domain = df[column].unique().tolist()
    domain = [x for x in domain if str(x) != 'nan']
 
  df[f"{column}_p"] = df[column].apply(perturb_field, args=(gamma, domain))
  return df

def perturb_field(value, gamma, domain):
  x = value
  lie_threshold = 0.5 - gamma
  r_value = random.uniform(0, 1)
  if r_value < lie_threshold: 
    # Lie!
    domain = [x for x in domain if x != value]
    x = random.choice(domain)
  return x