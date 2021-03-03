# Google Cloud Run FastAPI

This demonstrates a workflow for developing FastAPI python applications deployed using Google Cloud Run.

## Setup

To set up the deployment workflow, fork this repository. Navigate to Github's `Settings > Secrets` and define the following variables.

| Name           | Value                                                           |
| -------------- | --------------------------------------------------------------- |
| `GCP_SA_KEY`   | JSON service account key with Cloud Run Admin IAM authorization |
| `PROJECT_NAME` | Name of python service, used for naming Cloud Run services      |

The project ID is inferred from the project that created the service account key. The GCP project must be created prior to deploying Cloud Run services using these tools.
