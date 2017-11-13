# Sample flask app

Based on [honestbee/flask_app_k8s](https://github.com/honestbee/flask_app_k8s)

## Step 1 - Build the image
```bash
export DOCKER_REPO=<docker-hub-user>
docker build -t $DOCKER_REPO/flask-app:1.0 .
```

## Step 2 - Push image

```bash
docker push $DOCKER_REPO/flask-app:1.0
```

## Step 3 - Deploying to Kubernetes

```bash
kubectl create -f kubernetes/deploy-app-simple.yaml
```

## Step 4 - Exposing the Deployment through a Service Resource

```bash
kubectl expose deploy app --target-port=5000 --type=LoadBalancer
```

## Step 5 - Access the app through the service

```bash
minikube service app
```

## Step 6 - Scale

```bash
kubectl scale deployment app --replicas=10
```

## Cleanup

```bash
kubectl delete deploy app
kubectl delete service app
```

## Helpfull commands

```bash
kubectl get services # List all services in the namespace
kubectl get pods --all-namespaces             # List all pods in all namespaces

kubectl describe svc app # Get info about the exposed service
kubectl explain deployment.spec.template.spec # Show man pages for options
``

See also this [cheatsheet](https://kubernetes.io/docs/user-guide/kubectl-cheatsheet/)