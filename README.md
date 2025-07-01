# cloudregion

[![Release](https://img.shields.io/github/v/release/prassanna-ravishankar/cloudregion)](https://img.shields.io/github/v/release/prassanna-ravishankar/cloudregion)
[![Build status](https://img.shields.io/github/actions/workflow/status/prassanna-ravishankar/cloudregion/main.yml?branch=main)](https://github.com/prassanna-ravishankar/cloudregion/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/prassanna-ravishankar/cloudregion/branch/main/graph/badge.svg)](https://codecov.io/gh/prassanna-ravishankar/cloudregion)
[![Commit activity](https://img.shields.io/github/commit-activity/m/prassanna-ravishankar/cloudregion)](https://img.shields.io/github/commit-activity/m/prassanna-ravishankar/cloudregion)
[![License](https://img.shields.io/github/license/prassanna-ravishankar/cloudregion)](https://img.shields.io/github/license/prassanna-ravishankar/cloudregion)

## Problem Statement
**Multi-cloud developers waste time dealing with inconsistent region naming across cloud providers.** Each cloud uses different naming conventions:
- AWS: `us-east-1`, `eu-west-1`
- Azure: `eastus`, `westeurope`
- GCP: `us-east1`, `europe-west1`

This forces developers to:
- Maintain separate region mappings in their code
- Remember provider-specific names for equivalent regions
- Update configuration files for each cloud when deploying multi-cloud infrastructure
- Write cloud-specific code instead of cloud-agnostic code

## Current State
- **No simple Python library exists** for region conversion
- **Multy** (Go-based) has region mapping but focuses on infrastructure deployment
- **Apache Libcloud** abstracts APIs but doesn't solve region naming
- **Service comparison charts** exist but aren't programmatic
- Developers resort to manual mapping or cloud-specific code

## Proposed Solution
**A lightweight Python library for canonical cloud region mapping with SDK integration.**

### Core API Design
```python
from cloudregions import region

# Simple conversion
aws_region = region('us-east').aws        # "us-east-1"
azure_region = region('us-east').azure    # "eastus"
gcp_region = region('us-east').gcp        # "us-east1"

# SDK integration
import boto3
ec2 = boto3.client('ec2', region_name=region('us-east').aws)

# Wrapper functions (future)
from cloudregions.boto3 import client
ec2 = client('ec2', region='us-east')  # auto-resolves to us-east-1
```

### Key Features
1. **Canonical regions**: `us-east`, `us-west`, `eu-west`, `asia-southeast`
2. **Provider properties**: `.aws`, `.azure`, `.gcp`
3. **SDK integration**: Drop-in replacement for region parameters
4. **Fallback handling**: Sensible defaults when regions don't exist in a cloud
5. **Extensible**: Easy to add new clouds/regions

### Value Proposition
- **Write once, deploy anywhere**: Single region definition works across clouds
- **Zero learning curve**: Intuitive API with obvious naming
- **Drop-in compatibility**: Works with existing boto3/Azure SDK/GCP client code
- **Multi-cloud ready**: Enables true cloud-agnostic infrastructure code

### Target Use Cases
- Multi-cloud infrastructure builders (primary target)
- Cloud migration projects
- Disaster recovery across clouds
- Cost optimization tools that compare regions
- DevOps automation scripts

### Future Extensions
- Terraform/Pulumi variable generation
- Compliance zone mapping (EU, US-Gov, etc.)
- Latency/proximity data
- Available services per region metadata

**Why now?** Multi-cloud adoption is accelerating, but tooling still requires cloud-specific knowledge. This library would remove a fundamental friction point in multi-cloud development.
