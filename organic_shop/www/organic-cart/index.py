import frappe
import json
# from erpnext.shopping_cart.cart import get_cart_quotation
from erpnext.e_commerce.shopping_cart.cart import get_cart_quotation

# def get_context(context):
# 	context.update(get_cart_quotation())


def get_context(context):
    # if frappe.session.user == 'Guest':
    #     frappe.local.flags.redirect_location = '/'
    #     raise frappe.Redirect

    context.session = frappe.session
    context.user = frappe.session.user
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.item_group = frappe.get_all("Item Group",filters={"show_in_website":1,"is_group":0},fields=["name"])
    # context.item = frappe.get_all("Item",filters={"show_in_website":1},fields=["name","image","item_group"])
    context.item_result = get_items()
    context.update(get_cart_quotation())

    return context


def get_items():
    result_items = []
    items = frappe.db.sql(""" select name,item_name,route,has_variants,item_group,website_warehouse,image from `tabItem` it where it.show_in_website = 1 and it.is_sales_item = 1""",as_dict = 1)

    for item in items:
        if item.has_variants == 1:
            variant = frappe.db.sql("""select name,item_name,item_group,website_warehouse from `tabItem` it where it.variant_of = %s""",item.name,as_dict = 1)
            variant_list = []
            in_stock = 0
            for var in variant:
                price = frappe.db.get_value("Item Price",{"item_code":var.name,"price_list":frappe.db.get_value("Shopping Cart Settings",None,"price_list"),"selling":1},"price_list_rate")
                stock = frappe.db.get_value("Bin",{"item_code":var.name,"warehouse":var.website_warehouse},"actual_qty")
                if stock != None and stock != 0:
                    in_stock=1
                
                variant_list.append({
                    "variant_name":var.item_name,
                    "variant":var.name,
                    "stock":stock,
                    "price":price,
                    
                })
            result_items.append({
                "route":item.route,
                "has_variant":item.has_variants,
                "item":item.name,
                "item_name":item.item_name,
                "image":item.image,
                "variant":variant_list,
                "item_group":item.item_group,
                "in_stock":in_stock
            })
        else:
            in_stock = 0
            price = frappe.db.get_value("Item Price",{"item_code":item.name,"price_list":frappe.db.get_value("Shopping Cart Settings",None,"price_list"),"selling":1},"price_list_rate")
            stock = frappe.db.get_value("Bin",{"item_code":item.name,"warehouse":item.website_warehouse},"actual_qty")
            if stock != None and stock != 0:
                in_stock=1
            result_items.append({
                "route":item.route,
                "has_variant":item.has_variants,
                "item":item.name,
                "item_name":item.item_name,
                "image":item.image,
                "variant":None,
                "stock":stock,
                "price":price,
                "item_group":item.item_group,
                "in_stock":in_stock
            })

    return result_items




