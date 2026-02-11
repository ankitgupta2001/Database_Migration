-- Row counts for all migrated tables
-- Source: temp_iam_migration | Target: doha-iam-v15

-- =====================
-- SOURCE DB COUNTS
-- =====================
SELECT 'tabRole' as 'Table', count(*) as 'Count' FROM `temp_iam_migration`.`tabRole`
UNION ALL SELECT 'tabRole Profile', count(*) FROM `temp_iam_migration`.`tabRole Profile`
UNION ALL SELECT 'tabUser', count(*) FROM `temp_iam_migration`.`tabUser`
UNION ALL SELECT 'tabHas Role', count(*) FROM `temp_iam_migration`.`tabHas Role`
UNION ALL SELECT 'tabUser Social Login', count(*) FROM `temp_iam_migration`.`tabUser Social Login`
UNION ALL SELECT 'tabIAM Properties', count(*) FROM `temp_iam_migration`.`tabIAM Properties`
UNION ALL SELECT 'tabIAM Config', count(*) FROM `temp_iam_migration`.`tabIAM Config`
UNION ALL SELECT 'tabIAM Audit', count(*) FROM `temp_iam_migration`.`tabIam Audit`
UNION ALL SELECT 'tabApplication Name Master', count(*) FROM `temp_iam_migration`.`tabApplication Name Master`
UNION ALL SELECT 'tabApplication Master', count(*) FROM `temp_iam_migration`.`tabApplication Master`
UNION ALL SELECT 'tabApplication Access Roles', count(*) FROM `temp_iam_migration`.`tabApplication Access Roles`
UNION ALL SELECT 'tabApplication Role Child', count(*) FROM `temp_iam_migration`.`tabApplication Role Child`
UNION ALL SELECT 'tabUser Access Master', count(*) FROM `temp_iam_migration`.`tabUser Access Master`
UNION ALL SELECT 'tabUser Access Child', count(*) FROM `temp_iam_migration`.`tabUser Access Child`
UNION ALL SELECT 'tabUser Access Audit', count(*) FROM `temp_iam_migration`.`tabUser Access Audit`
UNION ALL SELECT 'tabIAM User Role Migration', count(*) FROM `temp_iam_migration`.`tabIAM User Role Migration`
UNION ALL SELECT 'tabImported Users', count(*) FROM `temp_iam_migration`.`tabImported Users`
UNION ALL SELECT 'tabDocument Map', count(*) FROM `temp_iam_migration`.`tabDocument Map`
UNION ALL SELECT 'tabData Sync Configuration', count(*) FROM `temp_iam_migration`.`tabData Sync Configuration`
UNION ALL SELECT 'tabData Sync Link Conversion', count(*) FROM `temp_iam_migration`.`tabData Sync Link Conversion`
UNION ALL SELECT 'tabData Sync Value Map', count(*) FROM `temp_iam_migration`.`tabData Sync Value Map`
UNION ALL SELECT 'tabData Sync Field', count(*) FROM `temp_iam_migration`.`tabData Sync Field`
UNION ALL SELECT 'tabField Map', count(*) FROM `temp_iam_migration`.`tabField Map`
UNION ALL SELECT 'tabMatch Field', count(*) FROM `temp_iam_migration`.`tabMatch Field`
UNION ALL SELECT 'tabSpine Consumer Handler Mapping', count(*) FROM `temp_iam_migration`.`tabSpine Consumer Handler Mapping`
UNION ALL SELECT 'tabSpine Producer Handler Mapping', count(*) FROM `temp_iam_migration`.`tabSpine Producer Handler Mapping`
UNION ALL SELECT 'tabParked Link Reference', count(*) FROM `temp_iam_migration`.`tabParked Link Reference`
UNION ALL SELECT 'tabSingles (Spine Consumer Config)', count(*) FROM `temp_iam_migration`.`tabSingles` WHERE doctype = 'Spine Consumer Config'
UNION ALL SELECT 'tabSingles (Spine Producer Config)', count(*) FROM `temp_iam_migration`.`tabSingles` WHERE doctype = 'Spine Producer Config';

-- =====================
-- TARGET DB COUNTS
-- =====================
SELECT 'tabRole' as 'Table', count(*) as 'Count' FROM `doha-iam-v15`.`tabRole`
UNION ALL SELECT 'tabRole Profile', count(*) FROM `doha-iam-v15`.`tabRole Profile`
UNION ALL SELECT 'tabUser', count(*) FROM `doha-iam-v15`.`tabUser`
UNION ALL SELECT 'tabHas Role', count(*) FROM `doha-iam-v15`.`tabHas Role`
UNION ALL SELECT 'tabUser Social Login', count(*) FROM `doha-iam-v15`.`tabUser Social Login`
UNION ALL SELECT 'tabIAM Properties', count(*) FROM `doha-iam-v15`.`tabIAM Properties`
UNION ALL SELECT 'tabIAM Config', count(*) FROM `doha-iam-v15`.`tabIAM Config`
UNION ALL SELECT 'tabIAM Audit', count(*) FROM `doha-iam-v15`.`tabIam Audit`
UNION ALL SELECT 'tabApplication Name Master', count(*) FROM `doha-iam-v15`.`tabApplication Name Master`
UNION ALL SELECT 'tabApplication Master', count(*) FROM `doha-iam-v15`.`tabApplication Master`
UNION ALL SELECT 'tabApplication Access Roles', count(*) FROM `doha-iam-v15`.`tabApplication Access Roles`
UNION ALL SELECT 'tabApplication Role Child', count(*) FROM `doha-iam-v15`.`tabApplication Role Child`
UNION ALL SELECT 'tabUser Access Master', count(*) FROM `doha-iam-v15`.`tabUser Access Master`
UNION ALL SELECT 'tabUser Access Child', count(*) FROM `doha-iam-v15`.`tabUser Access Child`
UNION ALL SELECT 'tabUser Access Audit', count(*) FROM `doha-iam-v15`.`tabUser Access Audit`
UNION ALL SELECT 'tabIAM User Role Migration', count(*) FROM `doha-iam-v15`.`tabIAM User Role Migration`
UNION ALL SELECT 'tabImported Users', count(*) FROM `doha-iam-v15`.`tabImported Users`
UNION ALL SELECT 'tabDocument Map', count(*) FROM `doha-iam-v15`.`tabDocument Map`
UNION ALL SELECT 'tabData Sync Configuration', count(*) FROM `doha-iam-v15`.`tabData Sync Configuration`
UNION ALL SELECT 'tabData Sync Link Conversion', count(*) FROM `doha-iam-v15`.`tabData Sync Link Conversion`
UNION ALL SELECT 'tabData Sync Value Map', count(*) FROM `doha-iam-v15`.`tabData Sync Value Map`
UNION ALL SELECT 'tabData Sync Field', count(*) FROM `doha-iam-v15`.`tabData Sync Field`
UNION ALL SELECT 'tabField Map', count(*) FROM `doha-iam-v15`.`tabField Map`
UNION ALL SELECT 'tabMatch Field', count(*) FROM `doha-iam-v15`.`tabMatch Field`
UNION ALL SELECT 'tabSpine Consumer Handler Mapping', count(*) FROM `doha-iam-v15`.`tabSpine Consumer Handler Mapping`
UNION ALL SELECT 'tabSpine Producer Handler Mapping', count(*) FROM `doha-iam-v15`.`tabSpine Producer Handler Mapping`
UNION ALL SELECT 'tabParked Link Reference', count(*) FROM `doha-iam-v15`.`tabParked Link Reference`
UNION ALL SELECT 'tabSingles (Spine Consumer Config)', count(*) FROM `doha-iam-v15`.`tabSingles` WHERE doctype = 'Spine Consumer Config'
UNION ALL SELECT 'tabSingles (Spine Producer Config)', count(*) FROM `doha-iam-v15`.`tabSingles` WHERE doctype = 'Spine Producer Config';
