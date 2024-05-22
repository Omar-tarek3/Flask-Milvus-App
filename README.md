# Flask-Milvus App
 ## Flask Server Manifest Overview

1. ### Deployment
- **Labels and Selectors:** `app: flask-app`
- **Image:** `omartarekabdelall/flask-api:latest`

2. ### Service
- **Type:** `ClusterIP`
- **Port:** 5000
- **TargetPort:** 5000
- **Selector:** `app: flask-app`

3. ### Ingress Resource
- **NameSpace:** `flask-milvus`
- **No Host Specified.**
- **Path:**`/api`
- **Path:**`test_milvus_connection` to test Milvus connection
- **Backend Service**: `name: flask-svc`
- **Port:** 5000

## Usage on Minikube Cluster

1. Install NGINX Ingress-controller
   ```
   helm install <my-release> oci://registry-1.docker.io/bitnamicharts/nginx-ingress-controller
    ```
2. Create the `flask-milvus` NameSpace    
    ```
    kubectl create ns flask-milvus
    ```

3. Run the following command at `/Helm` dir
    ```
    helm install milvus-app ./milvus --set cluster.enabled=false --set etcd.replicaCount=1 --set minio.mode=standalone --set pulsar.enabled=false -n flask-milvus
   ```
 
2. Acces the app by forwarding port 80 on your local machine to the port used by the NGINX Ingress-controller **LoadBalancer** Service:
    ```
    kubectl port-forward svc/<ingress-controller-service-name> 80
    ```
    Navigate to `http://localhost/` to access your flask-milvus app

