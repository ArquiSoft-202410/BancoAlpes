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
chmod +x deployment.sh
```
#### 4. Ejecutar Script de despliegue
```console
./deployment.sh
```
### Eliminar proyecto
```console
gcloud deployment-manager deployments delete banco-alpes-deployment
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
