# traffic_generation

## Deploy Pods
```
kubectl apply -f deployment.yaml
kubectl get pods -o wide

```


## Send Request
```
python3 request.py img_links 5000
python3 request.py vid_links 5001
python3 request.py img_links 5002

```
