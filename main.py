from pyscript import display, document

def display_char(e):
    document.getElementById("output1").innerHTML = ""

    get_category = document.getElementById("category").value
    get_product = document.getElementById("product").value
    get_stock = document.getElementById("stock").value

    SKU = get_category[:3].upper() + "product" + get_product[:4].upper() + "stock" + str(get_stock)

    display("SKU: ", SKU, target='output1')