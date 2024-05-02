# ArgoCD
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. Argo CD automates the deployment of the desired application states in the specified target environments. 
Application deployments can track updates to branches, tags, or pinned to a specific version of manifests at a Git commit. See tracking strategies for additional details about the different tracking strategies available.

## create the argocd namespace in your cluster
```
kubectl create namespace argocd
```

## Deploy the argocd in Kubernetes 
```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Install Homebrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
``
## Install Argo CD Binary for COmmandline install

```
brew install argocd
```

## Extract ArgoCD Initial Password
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

## Commandline argocd login
```
argocd login svc-io:nodeport
```

