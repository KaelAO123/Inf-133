def render_products(products):
    return[
        {
            "id":product.id,
            "name":product.name,
            "price":product.price,
            "stock":product.price_unit,
        }
        for product in products
    ]

def render_product_detail(product):
    return {
        "id":product.id,
        "name": product.name,
        "price":product.price,
        "stock":product.stock,
    }