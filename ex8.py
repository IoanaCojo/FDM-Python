"""
Write a Python program to sort a list of dictionaries using lambda function. Sort the mobile phone models by their colour in alphabetical order. Example: Original list of dictionaries: [{'make': 'Nokia', 'model': 216, 'colour': 'Black'}, {'make': 'Mi Max', 'model': '2', 'colour': 'Gold'}, {'make': 'Samsung', 'model': 7, 'colour': 'Blue'}]

Sorted list of dictionaries: [{'make': 'Nokia', 'model': 216, 'colour': 'Black'}, {'make': 'Samsung', 'model': 7, 'colour': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'colour': 'Gold'}]

"""
mobile_models = [{'make': 'Nokia', 'model': 216, 'colour': 'Black'}, {'make': 'Mi Max', 'model': '2', 'colour': 'Gold'}, {'make': 'Samsung', 'model': 7, 'colour': 'Blue'}]
sorted_models_by_coulour = sorted(mobile_models, key = lambda x: x['colour'])
print (sorted_models_by_coulour)