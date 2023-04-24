# Notes

## Steps to run the services:

```bash
# First spin up the deployment and service per server
kubectl apply -f fastapp.yaml -f expapp.yaml

# List down the services using the following cmd
kubectl get svc

# Then expose the fastapp service
minikube service fastapp
```

## To validate the responses from both the servers

1. First hit the IP address which you would get from the last command. This will output the response from the FastAPI server

   ```bash
   curl http://localhost:<portno>/
   ```

2. To check the response from the express server, hit the following curl command:

   ```bash
   curl http://localhost:<portno>/expapp/
   ```
