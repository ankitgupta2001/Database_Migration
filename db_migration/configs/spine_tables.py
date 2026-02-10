SPINE_TABLES = [
    {
        "table_name": "tabDocument Map",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "remote_doctype", "remote_name", "local_doctype", "local_name", "remote_host"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "remote_doctype", "remote_name", "local_doctype", "local_name", "remote_host"],
        "where": "1=1"
    },
    {
        "table_name": "tabData Sync Configuration",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "topic", "remote_host", "remote_doctype", "module", "disabled", "is_standard", "is_producer", "is_consumer", "local_doctype", "skip_document_map", "omit_spine_events", "do_not_create", "recreate_on_update", "force_replace", "filter_string", "post_process_script"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "topic", "remote_host", "remote_doctype", "module", "disabled", "is_standard", "is_producer", "is_consumer", "local_doctype", "skip_document_map", "omit_spine_events", "do_not_create", "recreate_on_update", "force_replace", "filter_string", "post_process_script"],
        "where": "1=1"
    },
    {
        "table_name": "tabData Sync Link Conversion",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "remote_doctype", "local_doctype"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "remote_doctype", "local_doctype"],
        "where": "1=1"
    },
    {
        "table_name": "tabData Sync Value Map",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "local_field", "from_value", "to_value", "remote_value", "local_value", "fieldtype", "force_convert", "evaluate_jinja"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "local_field", "from_value", "to_value", "remote_value", "local_value", "fieldtype", "force_convert", "evaluate_jinja"],
        "where": "1=1"
    },
    {
        "table_name": "tabData Sync Field",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "local_field", "field_data_type"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "local_field", "field_data_type"],
        "where": "1=1"
    },
    {
        "table_name": "tabField Map",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "remote_field", "local_field"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "remote_field", "local_field"],
        "where": "1=1"
    },
    {
        "table_name": "tabMatch Field",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "local_field", "is_reqd"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "local_field", "is_reqd"],
        "where": "1=1"
    },
    {
        "table_name": "tabSpine Consumer Handler Mapping",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "document_type", "event_handler", "topic", "queue", "delete_on_status", "akka_key", "is_local", "session_user"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "document_type", "event_handler", "topic", "queue", "delete_on_status", "akka_key", "is_local", "session_user"],
        "where": "1=1"
    },
    {
        "table_name": "tabSpine Producer Handler Mapping",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "document_type", "event_handler", "topic", "throttle_duplicates", "cache_key", "queue", "custom_events", "akka_key", "session_user"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "document_type", "event_handler", "topic", "throttle_duplicates", "cache_key", "queue", "custom_events", "akka_key", "session_user"],
        "where": "1=1"
    },
    {
        "table_name": "tabParked Link Reference",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "ref_doctype", "ref_docname"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "ref_doctype", "ref_docname"],
        "where": "1=1"
    },
    {
        "table_name": "tabSingles",
        "select_fields": ["doctype", "field", "value"],
        "insert_fields": ["doctype", "field", "value"],
        "where": "doctype IN ('Spine Consumer Config', 'Spine Producer Config')",
        "order_by": None
    }
]
