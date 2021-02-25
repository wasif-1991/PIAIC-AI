import pandas as pd

inventory = pd.read_csv("inventory.csv")

combine_lambda = lambda row:
    '{} - {}'.format(row.product_type,
                     row.product_description)