# cloudregion Documentation

Welcome to cloudregion - a lightweight Python library for canonical cloud region mapping across AWS, Azure, and Google Cloud Platform.

## Overview

`cloudregion` solves the problem of inconsistent region naming across cloud providers by providing a simple, intuitive interface using city-based names.

Instead of remembering that Virginia is called:
- `us-east-1` in AWS
- `eastus` in Azure
- `us-east1` in GCP

You can simply use `region('virginia')` and get the correct provider-specific name.

## Installation

```bash
pip install cloudregion
```

## Quick Example

```python
from cloudregion import region

# Use intuitive city names
r = region('virginia')
print(r.aws)    # us-east-1
print(r.azure)  # eastus
print(r.gcp)    # us-east1

# Works with aliases too
region('us-east').canonical  # virginia
region('eu-west').gcp       # europe-west1
```

## Core Concepts

### City-Based Naming
The library uses intuitive city names as canonical identifiers:
- `virginia` instead of `us-east-1`/`eastus`/`us-east1`
- `tokyo` instead of `ap-northeast-1`/`japaneast`/`asia-northeast1`
- `frankfurt` instead of `eu-central-1`/`germanywestcentral`/`europe-west3`

### Provider Properties
Each region object exposes provider-specific names through properties:
- `.aws` - Returns AWS region identifier
- `.azure` - Returns Azure region identifier
- `.gcp` - Returns Google Cloud Platform region identifier
- `.canonical` - Returns the canonical city name

### Aliases
Common aliases are supported for convenience:
- `us-east`, `us-west`, `eu-west`, `asia-southeast`
- Regional variations like `n-virginia`, `germany`, `japan`

## Use Cases

### Multi-Cloud Infrastructure
```python
from cloudregion import region

# Deploy to the same logical region across clouds
target_region = region('virginia')

# AWS deployment
aws_config = {'region': target_region.aws}

# Azure deployment
azure_config = {'location': target_region.azure}

# GCP deployment
gcp_config = {'region': target_region.gcp}
```

### SDK Integration
```python
from cloudregion.integrations import boto3_client_kwargs

# Simplified boto3 client creation
ec2_config = boto3_client_kwargs('ec2', 'virginia')
ec2 = boto3.client(**ec2_config)
```

### Configuration Management
```python
# Environment-specific region mapping
regions = {
    'dev': region('virginia'),
    'staging': region('oregon'),
    'prod': region('frankfurt')
}

env = 'prod'
aws_region = regions[env].aws  # eu-central-1
```

## API Reference

See the [API Reference](modules.md) for detailed documentation of all classes and functions.

## Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/prassanna-ravishankar/cloudregion/blob/main/CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License.
