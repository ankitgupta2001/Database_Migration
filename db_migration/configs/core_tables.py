CORE_TABLES = [
    {
        "table_name": "tabRole",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "role_name", "disabled", "desk_access", "two_factor_auth", "restrict_to_domain"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "role_name", "disabled", "desk_access", "two_factor_auth", "restrict_to_domain"],
        "where": "1=1"
    },
    {
        "table_name": "tabRole Profile",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "role_profile"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "role_profile"],
        "where": "1=1"
    },
    {
        "table_name": "tabUser",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "enabled", "email", "first_name", "middle_name", "last_name", "full_name", "send_welcome_email", "unsubscribed", "username", "language", "time_zone", "user_image", "role_profile_name", "gender", "phone", "mobile_no", "birth_date", "location", "bio", "mute_sounds", "new_password", "logout_all_sessions", "reset_password_key", "redirect_url", "thread_notify", "send_me_a_copy", "email_signature", "simultaneous_sessions", "user_type", "login_after", "login_before", "restrict_ip", "last_login", "last_ip", "last_active", "api_key", "api_secret"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "enabled", "email", "first_name", "middle_name", "last_name", "full_name", "send_welcome_email", "unsubscribed", "username", "language", "time_zone", "user_image", "role_profile_name", "gender", "phone", "mobile_no", "birth_date", "location", "bio", "mute_sounds", "new_password", "logout_all_sessions", "reset_password_key", "redirect_url", "thread_notify", "send_me_a_copy", "email_signature", "simultaneous_sessions", "user_type", "login_after", "login_before", "restrict_ip", "last_login", "last_ip", "last_active", "api_key", "api_secret"],
        "where": "name NOT IN ('Administrator', 'Guest', 'bg_worker@nomail.com', 'spine_producer@nomail.com', 'spine_consumer@nomail.com')"
    },
    {
        "table_name": "__Auth",
        "select_fields": ["doctype", "name", "fieldname", "password", "encrypted"],
        "insert_fields": ["doctype", "name", "fieldname", "password", "encrypted"],
        "where": "name NOT IN ('Administrator')"
    },
    {
        "table_name": "tabHas Role",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "role"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "role"],
        "where": "1=1"
    },
    {
        "table_name": "tabUser Social Login",
        "select_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "provider", "username", "userid"],
        "insert_fields": ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx", "parent", "parentfield", "parenttype", "provider", "username", "userid"],
        "where": "1=1"
    }
]
