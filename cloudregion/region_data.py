"""
Region mapping data for cloud providers.

This module contains the core mapping data between canonical city-based
region names and provider-specific region identifiers.
"""

from typing import Optional

# City-based canonical regions mapped to provider regions
REGION_MAPPINGS: dict[str, dict[str, Optional[str]]] = {
    # North America - US East
    "virginia": {
        "aws": "us-east-1",
        "azure": "eastus",
        "gcp": "us-east1",
    },
    "ohio": {
        "aws": "us-east-2",
        "azure": "eastus2",
        "gcp": "us-east4",
    },
    # North America - US West
    "oregon": {
        "aws": "us-west-2",
        "azure": "westus2",
        "gcp": "us-west1",
    },
    "california": {
        "aws": "us-west-1",
        "azure": "westus",
        "gcp": "us-west2",
    },
    # North America - Canada
    "toronto": {
        "aws": "ca-central-1",
        "azure": "canadacentral",
        "gcp": "northamerica-northeast1",
    },
    # Europe
    "dublin": {
        "aws": "eu-west-1",
        "azure": "northeurope",
        "gcp": "europe-west1",
    },
    "london": {
        "aws": "eu-west-2",
        "azure": "uksouth",
        "gcp": "europe-west2",
    },
    "paris": {
        "aws": "eu-west-3",
        "azure": "francecentral",
        "gcp": "europe-west9",
    },
    "frankfurt": {
        "aws": "eu-central-1",
        "azure": "germanywestcentral",
        "gcp": "europe-west3",
    },
    "stockholm": {
        "aws": "eu-north-1",
        "azure": "swedencentral",
        "gcp": "europe-north1",
    },
    # Asia Pacific
    "singapore": {
        "aws": "ap-southeast-1",
        "azure": "southeastasia",
        "gcp": "asia-southeast1",
    },
    "sydney": {
        "aws": "ap-southeast-2",
        "azure": "australiaeast",
        "gcp": "australia-southeast1",
    },
    "tokyo": {
        "aws": "ap-northeast-1",
        "azure": "japaneast",
        "gcp": "asia-northeast1",
    },
    "seoul": {
        "aws": "ap-northeast-2",
        "azure": "koreacentral",
        "gcp": "asia-northeast3",
    },
    "mumbai": {
        "aws": "ap-south-1",
        "azure": "centralindia",
        "gcp": "asia-south1",
    },
    "hong-kong": {
        "aws": "ap-east-1",
        "azure": "eastasia",
        "gcp": "asia-east2",
    },
}

# Common aliases for region names
REGION_ALIASES: dict[str, str] = {
    # US variations
    "us-east": "virginia",
    "us-east-1": "virginia",
    "us-east-2": "ohio",
    "us-west": "oregon",
    "us-west-1": "california",
    "us-west-2": "oregon",
    "n-virginia": "virginia",
    "north-virginia": "virginia",
    # Europe variations
    "eu-west": "dublin",
    "eu-central": "frankfurt",
    "europe-west": "dublin",
    "uk": "london",
    "france": "paris",
    "germany": "frankfurt",
    # Asia variations
    "asia-southeast": "singapore",
    "asia-northeast": "tokyo",
    "japan": "tokyo",
    "korea": "seoul",
    "australia": "sydney",
    "india": "mumbai",
}
