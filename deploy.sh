kubectl create -f kubernetes/deploy-app-simple.yaml
kubectl expose deploy app --target-port=5000 --type=LoadBalancer
minikube service app