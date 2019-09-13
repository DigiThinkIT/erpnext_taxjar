# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_taxjar"
app_title = "ERPNext TaxJar"
app_publisher = "DigiThinkIT Inc"
app_description = "TaxJar Integration with ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "valmik@digithinkit.com"
app_license = "MIT"

# Includes in <head>
# ------------------


doc_events = {
	"Quotation": {
		"validate": "erpnext_taxjar.api.set_sales_tax"
	},
	"Sales Order": {
		"validate": "erpnext_taxjar.api.set_sales_tax"
	},
	"Sales Invoice": {
		"validate": "erpnext_taxjar.api.set_sales_tax",
		"on_submit": "erpnext_taxjar.api.create_transaction",
		"on_cancel": "erpnext_taxjar.api.delete_transaction"
	}
}

awc_address_validation = [
	"erpnext_taxjar.api.validate_address"
]

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_taxjar/css/erpnext_taxjar.css"
# app_include_js = "/assets/erpnext_taxjar/js/erpnext_taxjar.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_taxjar/css/erpnext_taxjar.css"
# web_include_js = "/assets/erpnext_taxjar/js/erpnext_taxjar.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_taxjar.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_taxjar.install.before_install"
# after_install = "erpnext_taxjar.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_taxjar.notifications.get_notification_config"

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
# 		"erpnext_taxjar.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_taxjar.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_taxjar.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_taxjar.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_taxjar.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_taxjar.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_taxjar.event.get_events"
# }
