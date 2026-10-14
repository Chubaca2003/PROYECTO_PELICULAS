-- =====================================================================
-- Evaluación N.º 2 - Backend
-- Proyecto 29: API de Películas y Series
-- Script 3 de 3: Asignación de permisos
--
-- Ejecutar como usuario administrador (root):
--     mysql -u root -p < sql/03_asignar_permisos.sql
-- =====================================================================

-- Permisos sobre la base de datos de la aplicación.
-- Django necesita DDL (CREATE/ALTER/DROP/INDEX/REFERENCES) para poder
-- aplicar las migraciones, además del DML habitual.
GRANT SELECT, INSERT, UPDATE, DELETE,
      CREATE, ALTER, DROP, INDEX, REFERENCES
    ON proyecto_peliculas.* TO 'peliculas_user'@'localhost';

-- Base de datos temporal que Django crea al ejecutar `manage.py test`.
GRANT ALL PRIVILEGES ON `test_proyecto_peliculas`.* TO 'peliculas_user'@'localhost';

-- Aplicar los cambios de inmediato.
FLUSH PRIVILEGES;

-- Verificación
SHOW GRANTS FOR 'peliculas_user'@'localhost';
