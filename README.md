# Banco los Alpes
## Instrucciones de despliegue
### Requisitos previos
1. [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) instalado y configurado con la cuenta de Google.
2. Permisos adecuados en el proyecto de GCP para crear instancias y reglas de firewall.
3. Una terminal de Cloud Shell (GCP)
### Pasos para el despliegue
#### 1. Clonar el repositorio
```console
git clone https://github.com/ArquiSoft-202410/BancoAlpes.git
```
#### 2. Cambiar al directorio del proyecto
```console
cd BancoAlpes
```
#### 3. Permisos de despliegue
```console
sudo chmod +x deployment.sh
```
#### 4. Ejecutar Script de despliegue
```console
./deployment.sh
```
### Eliminar proyecto
```console
gcloud deployment-manager deployments delete banco-alpes-deployment
```
## Acceso a la base de datos
Para acceder a la base de datos directamente desde su terminal (conexión SSH) y hacer consultas.
```console
psql -U banco_alpes -d banco_alpes_db
```
luego, escribir la contraseña de la base de datos.
Algunos comandos útiles:
```console
# Ver todas las tablas de DB
\dt

# Datos de una tabla
SELECT * FROM "<Nombre-Tabla>";

# Actualizar información
UPDATE "<Nombre-Tabla>" SET <párametro> = '<Nuevo-Valor>' WHERE id = <id-dato>;

# Eliminar datos de una tabla
DELETE FROM "<Nombre-Tabla>";

# Salir
\q
```
### Ver procesos en segundo plano
```console
ps -ef | grep python
```
### Quitar procesos en segundo plano
```console
sudo kill 
```
y despues el id del proceso
