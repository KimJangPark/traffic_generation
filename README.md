# traffic_generation

## Deploy Pods
```
docker run -it --rm --network host img-python
docker run -it --rm --network host vid-python
docker run -it --rm --network host jetson-service

kubectl apply -f deployment.yaml
kubectl get pods -o wide

```


## Send Request
```
python3 request.py img_links
```
