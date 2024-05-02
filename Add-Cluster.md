# Get Cluster Name
```
kubectl config get-contexts -o name
```

## Then Add Cluster 
```
argocd cluster add "Cluster-Name"
```

## Deploy Sample Helm Application
```
argocd app create helm-guestbook --repo https://github.com/argoproj/argocd-example-apps.git --path helm-guestbook --dest-server https://kubernetes.default.svc --dest-namespace default
```
