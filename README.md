# cloudregion

[![PyPI version](https://img.shields.io/pypi/v/cloudregion.svg)](https://pypi.org/project/cloudregion/)
[![Python versions](https://img.shields.io/pypi/pyversions/cloudregion.svg)](https://pypi.org/project/cloudregion/)
[![Release](https://img.shields.io/github/v/release/prassanna-ravishankar/cloudregion)](https://github.com/prassanna-ravishankar/cloudregion/releases)
[![Build status](https://img.shields.io/github/actions/workflow/status/prassanna-ravishankar/cloudregion/main.yml?branch=main)](https://github.com/prassanna-ravishankar/cloudregion/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/prassanna-ravishankar/cloudregion/branch/main/graph/badge.svg)](https://codecov.io/gh/prassanna-ravishankar/cloudregion)
[![License](https://img.shields.io/github/license/prassanna-ravishankar/cloudregion)](https://img.shields.io/github/license/prassanna-ravishankar/cloudregion)

**A lightweight Python library for canonical cloud region mapping across AWS, Azure, and Google Cloud Platform.**

Tired of remembering that AWS uses `us-east-1`, Azure uses `eastus`, and GCP uses `us-east1` for the same region? `cloudregion` provides a simple, consistent interface using intuitive city-based names.

## 🚀 Quick Start

```bash
pip install cloudregion
```

```python
from cloudregion import region

# Use intuitive city names
r = region('virginia')
print(r.aws)    # us-east-1
print(r.azure)  # eastus
print(r.gcp)    # us-east1

# Works with aliases too
region('us-east').aws   # us-east-1
region('eu-west').gcp   # europe-west1
```

## 💡 Why cloudregion?

**Multi-cloud developers waste time dealing with inconsistent region naming.** Each cloud provider uses different conventions:

| Region | AWS | Azure | GCP |
|--------|-----|-------|-----|
| US East | `us-east-1` | `eastus` | `us-east1` |
| US West | `us-west-2` | `westus2` | `us-west1` |
| EU West | `eu-west-1` | `northeurope` | `europe-west1` |

This forces developers to:
- 🔄 Maintain separate region mappings in code
- 🧠 Remember provider-specific names for equivalent regions
- 📝 Update configuration files for each cloud provider
- 🔧 Write cloud-specific code instead of cloud-agnostic code

## 🎯 Features

- **🏙️ City-based names**: Use intuitive names like `virginia`, `tokyo`, `frankfurt`
- **🔄 Multi-cloud**: Single interface for AWS, Azure, and GCP
- **🏷️ Smart aliases**: `us-east`, `eu-west`, `asia-southeast` work too
- **🧰 SDK integration**: Helper functions for boto3, Azure SDK, GCP clients
- **✅ Type safe**: Full mypy support with proper type hints
- **⚡ Zero dependencies**: Pure Python with no external requirements
- **🧪 Well tested**: Comprehensive test suite with 100% coverage

## 📖 Usage

### Basic Usage

```python
from cloudregion import region

# Create region objects
virginia = region('virginia')
tokyo = region('tokyo')
frankfurt = region('frankfurt')

# Access provider-specific names
print(virginia.aws)    # us-east-1
print(tokyo.azure)     # japaneast
print(frankfurt.gcp)   # europe-west3

# Use aliases
us_east = region('us-east')      # resolves to virginia
eu_west = region('eu-west')      # resolves to dublin
asia = region('asia-southeast')  # resolves to singapore
```

### SDK Integration

```python
from cloudregion.integrations import boto3_client_kwargs, azure_credential_kwargs, gcp_client_kwargs

# AWS boto3
import boto3
client_config = boto3_client_kwargs('ec2', 'virginia')
ec2 = boto3.client(**client_config)  # auto-resolves to us-east-1

# Azure
azure_config = azure_credential_kwargs('frankfurt', subscription_id='my-sub')
# Use with Azure SDK clients

# GCP
gcp_config = gcp_client_kwargs('tokyo', project='my-project')
# Use with Google Cloud client libraries
```

### Error Handling

```python
from cloudregion import region, UnknownRegionError

try:
    r = region('unknown-place')
except UnknownRegionError as e:
    print(f"Error: {e}")
    # Error: Unknown region 'unknown-place'. Available regions: virginia, oregon, ...
```

## 🗺️ Supported Regions

| Canonical Name | AWS | Azure | GCP |
|----------------|-----|-------|-----|
| `virginia` | `us-east-1` | `eastus` | `us-east1` |
| `ohio` | `us-east-2` | `eastus2` | `us-east4` |
| `oregon` | `us-west-2` | `westus2` | `us-west1` |
| `california` | `us-west-1` | `westus` | `us-west2` |
| `toronto` | `ca-central-1` | `canadacentral` | `northamerica-northeast1` |
| `dublin` | `eu-west-1` | `northeurope` | `europe-west1` |
| `london` | `eu-west-2` | `uksouth` | `europe-west2` |
| `paris` | `eu-west-3` | `francecentral` | `europe-west9` |
| `frankfurt` | `eu-central-1` | `germanywestcentral` | `europe-west3` |
| `stockholm` | `eu-north-1` | `swedencentral` | `europe-north1` |
| `singapore` | `ap-southeast-1` | `southeastasia` | `asia-southeast1` |
| `sydney` | `ap-southeast-2` | `australiaeast` | `australia-southeast1` |
| `tokyo` | `ap-northeast-1` | `japaneast` | `asia-northeast1` |
| `seoul` | `ap-northeast-2` | `koreacentral` | `asia-northeast3` |
| `mumbai` | `ap-south-1` | `centralindia` | `asia-south1` |
| `hong-kong` | `ap-east-1` | `eastasia` | `asia-east2` |

### Aliases

Common aliases are supported for convenience:

- `us-east` → `virginia`
- `us-west` → `oregon`
- `eu-west` → `dublin`
- `eu-central` → `frankfurt`
- `asia-southeast` → `singapore`
- `asia-northeast` → `tokyo`

## 🛠️ Development

```bash
# Clone the repository
git clone https://github.com/prassanna-ravishankar/cloudregion.git
cd cloudregion

# Install development dependencies
uv sync --dev

# Run tests
uv run pytest

# Run type checking
uv run mypy cloudregion/

# Run linting
uv run ruff check .

# Format code
uv run ruff format .
```

## 📋 Requirements

- Python 3.9+
- No external dependencies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. See our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Roadmap

- **Terraform/Pulumi integration**: Generate provider-specific variables
- **Compliance zones**: EU, US-Gov, China region mappings
- **Latency data**: Distance and performance metrics between regions
- **Service availability**: Which services are available in each region
- **Cost data**: Regional pricing information integration

## 🙏 Acknowledgments

- Inspired by the need for simpler multi-cloud development
- Built with modern Python tooling (uv, ruff, mypy)
- Tested across Python 3.9-3.13

---

**Made with ❤️ for multi-cloud developers**
