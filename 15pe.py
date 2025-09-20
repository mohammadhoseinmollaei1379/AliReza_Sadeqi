product = [
    ("mouse", 120),
    ("hed phone", 350),
    ("charjer", 80)
]
def get_price(product_tuple):
    return product_tuple[1]

product.sort(key=lambda item: get_price(item))
print(product)





