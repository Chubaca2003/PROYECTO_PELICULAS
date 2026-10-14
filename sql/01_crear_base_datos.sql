-- =====================================================================
-- Evaluación N.º 2 - Backend
-- Proyecto 29: API de Películas y Series
-- Script 1 de 3: Creación de la base de datos
--
-- Ejecutar como usuario administrador (root):
--     mysql -u root -p < sql/01_crear_base_datos.sql
-- =====================================================================

-- utf8mb4 permite almacenar tildes, ñ y cualquier carácter Unicode.
-- La collation *_unicode_ci hace que las comparaciones y ordenamientos
-- ignoren mayúsculas y acentos.
CREATE DATABASE IF NOT EXISTS proyecto_peliculas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Verificación
SHOW DATABASES LIKE 'proyecto_peliculas';
