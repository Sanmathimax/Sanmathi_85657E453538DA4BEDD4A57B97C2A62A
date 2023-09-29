def linear_search_product(product_list, target_product):
  indices = []
  for i, product in enumerate(product_list):
    if product == target_product:
      indices.append(i)
  return indices

# Example usage
products = [
    'red currant', 'hamburger', 'sausages', 'red currant', 'boysenberry',
    'spagetti', 'red currant'
]
target_product = 'red currant'
result = linear_search_product(products, target_product)
print("Indices of '{}' in the product list: {}".format(target_product, result))
