IAM_TABLES = [
    {
        "table_name": "tabIAM Properties",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "key", "value", "description"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "key", "value", "description"],
        "where": "1=1"
    },
    {
        "table_name": "tabIAM Config",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "prop_key", "prop_value"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "prop_key", "prop_value"],
        "where": "1=1"
    },
    {
        "table_name": "tabIam Audit",
        "target_table_name": "tabIAM Audit",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "entity_id", "entity_type", "action", "action_by", "action_date", "old_value", "new_value", "comments"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "entity_id", "entity_type", "action", "action_by", "action_date", "old_value", "new_value", "comments"],
        "where": "1=1",
        "batch_size": 500
    },
    {
        "table_name": "tabApplication Name Master",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "application_name"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "application_name"],
        "where": "1=1"
    },
    {
        "table_name": "tabApplication Master",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "application_name", "access_type"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "application_name", "access_type"],
        "where": "1=1"
    },
    {
        "table_name": "tabApplication Access Roles",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "for_application", "access_id", "access_type"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "for_application", "access_id", "access_type"],
        "where": "1=1"
    },
    {
        "table_name": "tabApplication Role Child",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "assigned"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "assigned"],
        "where": "1=1"
    },
    {
        "table_name": "tabUser Access Master",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "email_id", "manual_audits"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "email_id", "manual_audits"],
        "where": "1=1"
    },
    {
        "table_name": "tabUser Access Child",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "access_doc", "application", "assigned_access", "action", "ticket_no", "access_type", "remove AS remove_role"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "access_doc", "application", "assigned_access", "action", "ticket_no", "access_type", "remove_role"],
        "where": "1=1"
    },
    {
        "table_name": "tabUser Access Audit",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "application", "assigned_access", "action", "ticket_no", "updated_by", "updated_on", "remark"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "application", "assigned_access", "action", "ticket_no", "updated_by", "updated_on", "remark"],
        "where": "1=1"
    },
    {
        "table_name": "tabIAM User Role Migration",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "application", "access_type", "token", "secreat", "api_name", "base_url", "status", "params"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "application", "access_type", "token", "secreat", "api_name", "base_url", "status", "params"],
        "where": "1=1"
    },
    {
        "table_name": "tabImported Users",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "user", "role", "application", "status", "error"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "user", "role", "application", "status", "error"],
        "where": "1=1"
    }
]
