-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

SET SESSION group_concat_max_len = 1000000;
SELECT GROUP_CONCAT('ALTER TABLE `', table_name, '` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
INTO @alter_statements
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0'
    AND table_type = 'BASE TABLE';
PREPARE alter_tables FROM @alter_statements;
EXECUTE alter_tables;
DEALLOCATE PREPARE alter_tables;

SET SESSION group_concat_max_len = 1000000;
SELECT GROUP_CONCAT('ALTER TABLE `', table_name, '` MODIFY COLUMN `', column_name, '` ', column_type, ' CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
INTO @alter_column_statements
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
    AND collation_name != 'utf8mb4_unicode_ci';
PREPARE alter_columns FROM @alter_column_statements;
EXECUTE alter_columns;
DEALLOCATE PREPARE alter_columns;
