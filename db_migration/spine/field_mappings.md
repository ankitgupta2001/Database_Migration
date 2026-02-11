# Spine Module Field Mappings

This document lists all tables and fields migrated in the Spine module.

## [tabDocument Map]
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

## [tabData Sync Configuration]
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

## [tabData Sync Link Conversion]
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

## [tabData Sync Value Map]
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

## [tabData Sync Field]
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
- `field_data_type`

## [tabField Map]
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
- `remote_field`
- `local_field`

## [tabMatch Field]
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
- `is_reqd`

## [tabSpine Consumer Handler Mapping]
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
- `document_type`
- `event_handler`
- `topic`
- `queue`
- `delete_on_status`
- `akka_key`
- `is_local`
- `session_user`

## [tabSpine Producer Handler Mapping]
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
- `document_type`
- `event_handler`
- `topic`
- `throttle_duplicates`
- `cache_key`
- `queue`
- `custom_events`
- `akka_key`
- `session_user`

## [tabMessage Log]
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
- `remote_name`
- `remote_docname`
- `local_doctype`
- `local_docname`
- `origin_sitename`
- `last_error`
- `retries_left`
- `error`

## [tabParked Link Reference]
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
- `ref_doctype`
- `ref_docname`

## [tabSingles]
- `doctype`
- `field`
- `value`
