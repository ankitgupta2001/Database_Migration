# Spine Module Field Mappings

This document lists all 13 DocTypes migrated in the Spine module.

## 1. [tabDocument Map]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `remote_doctype`
- `remote_name`
- `local_doctype`
- `local_name`
- `remote_host`

## 2. [tabData Sync Configuration]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `topic`
- `remote_host`
- `remote_doctype`
- `module`
- `disabled`
- `is_standard`
- `is_producer`
- `is_consumer`
- `local_doctype`
- `skip_document_map`
- `omit_spine_events`
- `do_not_create`
- `recreate_on_update`
- `force_replace`
- `filter_string`
- `post_process_script`

## 3. [tabData Sync Link Conversion]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `remote_doctype`
- `local_doctype`

## 4. [tabData Sync Value Map]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `local_field`
- `from_value`
- `to_value`
- `remote_value`
- `local_value`
- `fieldtype`
- `force_convert`
- `evaluate_jinja`

## 5. [tabData Sync Field]
- `name`
- `creation"
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `local_field`
- `field_data_type`

## 6. [tabField Map]
- `name`
- `creation"
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `remote_field`
- `local_field`

## 7. [tabMatch Field]
- `name`
- `creation"
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `local_field`
- `is_reqd`

## 8. [tabSpine Consumer Handler Mapping]
- `name`
- `creation"
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `document_type`
- `event_handler`
- `topic`
- `queue`
- `delete_on_status`
- `akka_key`
- `is_local`
- `session_user`

## 9. [tabSpine Producer Handler Mapping]
- `name`
- `creation"
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `document_type`
- `event_handler`
- `topic`
- `throttle_duplicates`
- `cache_key`
- `queue`
- `custom_events`
- `akka_key`
- `session_user`

## 10. [tabMessage Log]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `title`
- `json_message`
- `throttle_duplicates`
- `topic`
- `direction`
- `received_at`
- `event`
- `sha256`
- `status`
- `remote_doctype`
- `remote_docname`
- `local_doctype`
- `local_docname`
- `last_error`
- `retries_left`
- `error`

## 11. [tabParked Link Reference]
- `name`
- `creation"
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `parent`
- `parentfield`
- `parenttype`
- `ref_doctype`
- `ref_docname`

## 12. [Spine Consumer Config] (via `tabSingles`)
- `doctype`
- `field`
- `value`

## 13. [Spine Producer Config] (via `tabSingles`)
- `doctype`
- `field`
- `value`
