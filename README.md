# flask_template
flask template with waitress WSGI server and kubernetes (minikube)

## Docker commands
```eval $(minikube docker-env)```
```docker compose up --build -d```

## Kubectl commands
```minikube kubectl -- apply -f k8s/deployment.yaml``` <br>
```minikube kubectl -- apply -f k8s/service.yaml.yaml``` <br>
```minikube kubectl -- expose deployment flask-test-deployment --type=LoadBalancer --port=8000``` <br>
