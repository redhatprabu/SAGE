
# 1. AWS ECS Deployment : 

1) Create Docker images from build file (Tried sample blog and home page for sage) #not from task1 

2) Created Repo on ECS 

eg : You can scan your docker images locally using (aquasec ) to make sure you have secured images and push 

3) Pushed docker images to repo (screenshots in SAGE-AWS docx file) 

4) Create Launch config and Autoscaling group to spin up EC@ instances 

  tag : Dev
  tag : Prod (If you want one for prod copy the template and spin up on your selected VPC's (for prod we deploy on secured VPC which don't have direct internet access ) Config sidecra VPC and pass through the traffic via NAT gateway for accessing application 

5) Create ECS cluster ans services ) : added screenshot in docs file under stage 3 dir 

6) Try attaching your ALB and add reules to ALB and attach with your target group which you have already spun up Autoscaling group 
      make sure you have mapped 80 to 5000 and add 8081 also in rules when you access your api (still need to be corrected) 

7) Access your load balanbcer URL http:<localbalancer_URL>:80/ for sage flask home page.



# Kubernetes Deployment : 
Make sure you have mysql installed and tables created on localhost 

 1) Build docker file and crate and push image 

 2) Install K8s master and worker nodes

 3) Attached deployment file (inclusing autoscaling and Horizantal Pod Autocaling ) 

  4) kubectl apply -f sage-transaction-kube.yml

  5) Kubectl get svc | grep sage

  6) Access the curl -v -k 'http://localhost:8081/api/v1/transactions?day=2'

       should result last two days db transactions details 




note : DB table already shold be crated and tables are inserted. 

DB table name : transaction




 
