-- =====================================================================
-- Evaluación N.º 2 - Backend
-- Proyecto 29: API de Películas y Series
-- Script 2 de 3: Creación del usuario de la aplicación
--
-- Ejecutar como usuario administrador (root):
--     mysql -u root -p < sql/02_crear_usuario.sql
--
-- IMPORTANTE: la contraseña debe coincidir con la variable DB_PASSWORD
-- del archivo .env del proyecto.
-- =====================================================================

-- Se crea un usuario propio para la aplicación en lugar de usar root,
-- de modo que Django se conecte con los permisos mínimos necesarios.
CREATE USER IF NOT EXISTS 'peliculas_user'@'localhost'
    IDENTIFIED BY 'Peliculas2026.IEI';

-- Verificación
SELECT User, Host FROM mysql.user WHERE User = 'peliculas_user';
