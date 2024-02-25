import frappe
import json
from frappe.website.page_renderers.error_page import ErrorPage
from frappe.website.page_renderers.not_found_page import NotFoundPage
from frappe.website.page_renderers.not_permitted_page import NotPermittedPage
from frappe.website.page_renderers.redirect_page import RedirectPage
from frappe.website.path_resolver import PathResolver
from erpnext.stock.doctype.repost_item_valuation.repost_item_valuation import repost_entries

@frappe.whitelist(allow_guest = True)
def get_list_custom(doctype, fields=None, filters=None, order_by=None,
	limit_start=None, limit_page_length=20, parent=None):
	'''Returns a list of records by filters, fields, ordering and limit

	:param doctype: DocType of the data to be queried
	:param fields: fields to be returned. Default is `name`
	:param filters: filter list by this dict
	:param order_by: Order by this fieldname
	:param limit_start: Start at this index
	:param limit_page_length: Number of records to be returned (default 20)'''
	return frappe.db.get_all(doctype, fields=fields, filters=filters, order_by=order_by,
		limit_start=limit_start, limit_page_length=limit_page_length, ignore_permissions=True)


@frappe.whitelist(allow_guest=True)
def get_customer_reviews():
	repost_entries()
	return frappe.get_all('Customer Review',  filters={
        'show_in_website': 1
    }, fields=['customer_name', 'content', 'rating', 'customer_image'])


def get_response_wishlist(path=None, http_status_code=200):
	"""Resolves path and renders page"""
	response = None
	path = path or frappe.local.request.path

	endpoint = path

	try:
		path_resolver = PathResolver(path)
		endpoint, renderer_instance = path_resolver.resolve()
		response = renderer_instance.render()
	except frappe.Redirect:
		return RedirectPage(endpoint or path, http_status_code).render()
	except frappe.PermissionError as e:
		response = NotPermittedPage(endpoint, http_status_code, exception=e).render()
	except frappe.PageDoesNotExistError:
		response = NotFoundPage(endpoint, http_status_code).render()
	except Exception as e:
		response = ErrorPage(exception=e).render()

	return response


@frappe.whitelist(allow_guest=True)
def wishlist_content():
	path="/wishlist"
	http_status_code=200
	response = get_response_wishlist(path, http_status_code)
	return str(response.data, "utf-8")
