import frappe

def merge_boot(bootinfo):
    settings = frappe.get_cached_doc("ERPSuite Settings")
    bootinfo["suite_btn_listview"] = settings.add_info_button