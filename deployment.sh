#!/bin/bash

PROJECT_ID="arquisoft-202410"
ZONE="us-central1-a"

gcloud deployment-manager deployments create banco-alpes-deployment --config deployment.yaml --project $PROJECT_ID

echo "Waiting for the instances to start..."
sleep 180

INSTANCES_TO_STOP=("kong-instance" "rabbit-instance" "db-instance" "banco-alpes-d" "banco-alpes-c" "banco-alpes-b" "banco-alpes-a")
for INSTANCE_NAME in "${INSTANCES_TO_STOP[@]}"
do
   echo "Stopping the instance: $INSTANCE_NAME"
   gcloud compute instances stop $INSTANCE_NAME --zone=$ZONE --project $PROJECT_ID
done

echo "Successfully stopped instances."
echo "Running deployment.py script..."
sudo python3 deployment.py