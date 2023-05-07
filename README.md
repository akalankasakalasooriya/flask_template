# flask_template
flask template with waitress

## docker commands
eval $(minikube docker-env)
docker compose up --build -d

## kubectl commands
minikube kubectl -- apply -f k8s/deployment.yaml
minikube kubectl -- apply -f k8s/service.yaml.yaml
minikube kubectl -- expose deployment flask-test-deployment --type=LoadBalancer --port=8000
