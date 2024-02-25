# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "organic_shop"
app_title = "Organic Shop"
app_publisher = "GreyCube Technologies"
app_description = "Customization for a Organic Shop"
app_icon = "octicon octicon-thumbsup"
app_color = "green"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/organic_shop/css/organic_shop.css"
# app_include_js = "/assets/organic_shop/js/organic_shop.js"

# include js, css files in header of web template
# web_include_css = "/assets/organic_shop/css/organic_shop.css"
# web_include_css = "/app-assets/css/theme.css"
# web_include_js = "/assets/organic_shop/js/organic_shop.js"

web_include_js = "/app-assets/js/plugin/jquery-2.2.4.min.js"
web_include_js = "/app-assets/js/plugin/bootstrap.min.js"
web_include_js = "/app-assets/js/plugin/bootstrap-select.min.js"
web_include_js = "/app-assets/js/plugin/owl.carousel.min.js"
web_include_js = "/app-assets/js/plugin/jquery.plugin.min.js"
web_include_js = "/app-assets/js/plugin/jquery.countdown.js"
web_include_js = "/app-assets/js/plugin/jquery.subscribe-better.min.js"


# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "organic_shop.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "organic_shop.install.before_install"
# after_install = "organic_shop.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "organic_shop.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"organic_shop.tasks.all"
# 	],
# 	"daily": [
# 		"organic_shop.tasks.daily"
# 	],
# 	"hourly": [
# 		"organic_shop.tasks.hourly"
# 	],
# 	"weekly": [
# 		"organic_shop.tasks.weekly"
# 	]
# 	"monthly": [
# 		"organic_shop.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "organic_shop.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "organic_shop.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "organic_shop.task.get_dashboard_data"
# }