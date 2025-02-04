Step 1: Create a Kind Cluster
kind create cluster --name my-cluster --config cluster/kind-cluster.yaml
Step 2: Install Nginx Ingress Controller
kubectl create -f ingress/ingress-nginx.yaml
Step 3: Deploy Juice Shop App
kubectl create -f juice-shop/juice-shop-deployment.yaml
Step 5: Expose Juice Shop via Ingress
kubectl create -f juice-shop/juice-shop-ingress.yaml
Step 6: Add Local DNS Entry
127.0.0.1 juice-shop.local
Step 7: Monitoring Recommendations
Prometheus & Grafana: Monitor application metrics.
Loki: Collect logs.
kube-state-metrics: Gather cluster health data.
Promtail: Forward logs to Loki.
