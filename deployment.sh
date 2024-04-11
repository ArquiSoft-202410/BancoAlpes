#!/bin/bash

PROJECT_ID="bancoalpes-419917"
ZONE="us-central1-a"

gcloud deployment-manager deployments create banco-alpes-deployment --config deployment.yaml --project $PROJECT_ID

echo "Waiting for the instances to start..."
sleep 350

INSTANCES_TO_STOP=("banco-alpes-b" "banco-alpes-c")
for INSTANCE_NAME in "${INSTANCES_TO_STOP[@]}"
do
   echo "Stopping the instance: $INSTANCE_NAME"
   gcloud compute instances stop $INSTANCE_NAME --zone=$ZONE --project $PROJECT_ID
done

echo "Successfully stopped instances."