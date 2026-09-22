from pyscript import display, document

def display_char(e):
    document.getElementById("output1").innerHTML = ""

    get_category = document.getElementById("category").value
    get_product = document.getElementById("product").value
    get_stock = document.getElementById("stock").value

    display(get_category[:3] + get_product[:3] + get_stock[:3], target="output1") #get the 1st 3 letters of the word