# IAM Module Field Mappings

This document lists all tables and fields migrated in the IAM module.

## [tabIAM Properties]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `key`
- `value`
- `description`

## [tabIAM Config]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `prop_key`
- `prop_value`

## [tabIam Audit] -> [tabIAM Audit]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `entity_id`
- `entity_type`
- `action`
- `action_by`
- `action_date`
- `old_value`
- `new_value`
- `comments`

## [tabApplication Name Master]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `application_name`

## [tabApplication Master]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `application_name`
- `access_type`

## [tabApplication Access Roles]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `for_application`
- `access_id`
- `access_type`

## [tabApplication Role Child]
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
- `assigned`

## [tabUser Access Master]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `email_id`
- `manual_audits`

## [tabUser Access Child]
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
- `access_doc`
- `application`
- `assigned_access`
- `action`
- `ticket_no`
- `access_type`
- `remove_role` (Source: `remove`)

## [tabUser Access Audit]
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
- `application`
- `assigned_access`
- `action`
- `ticket_no`
- `updated_by`
- `updated_on`
- `remark`

## [tabIAM User Role Migration]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `application`
- `access_type`
- `token`
- `secreat`
- `api_name`
- `base_url`
- `status`
- `params`

## [tabImported Users]
- `name`
- `creation`
- `modified`
- `modified_by`
- `owner`
- `docstatus`
- `idx`
- `user`
- `role`
- `application`
- `status`
- `error`
