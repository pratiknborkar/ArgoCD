# ArgoCD

## create the argocd namespace in your cluster
```
kubectl create namespace argocd
```

## Deploy the argocd in Kubernetes 
```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

