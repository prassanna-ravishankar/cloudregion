"""
SDK integration helpers for cloud region mapping.

Provides wrapper functions for popular cloud SDKs that automatically
resolve canonical region names to provider-specific identifiers.
"""

from typing import Any

from .region import CloudRegionError, Region, UnknownRegionError


class IntegrationError(CloudRegionError):
    """Base exception for SDK integration errors."""

    def __init__(self, region_name: str, provider: str):
        """Initialize the exception for a region not available in a provider."""
        message = f"Region '{region_name}' is not available for {provider.upper()}"
        super().__init__(message)


def resolve_region_parameter(region_param: str, provider: str) -> str:
    """
    Resolve a region parameter to provider-specific format.

    Args:
        region_param: Region name (canonical or provider-specific)
        provider: Cloud provider ('aws', 'azure', 'gcp')

    Returns:
        Provider-specific region identifier

    Raises:
        IntegrationError: If region cannot be resolved
    """
    try:
        region_obj = Region(region_param)
    except UnknownRegionError:
        # If Region creation fails, assume it's already a provider-specific name
        return region_param

    provider_region = getattr(region_obj, provider)
    if provider_region is None:
        raise IntegrationError(region_param, provider)

    return str(provider_region)


# AWS Integrations
def boto3_session_kwargs(region: str, **kwargs: Any) -> dict[str, Any]:
    """
    Generate boto3 Session kwargs with resolved region.

    Args:
        region: Canonical region name or AWS region
        **kwargs: Additional Session parameters

    Returns:
        Dictionary of Session parameters with resolved region_name

    Example:
        >>> session_kwargs = boto3_session_kwargs('virginia', profile_name='dev')
        >>> session = boto3.Session(**session_kwargs)
    """
    resolved_region = resolve_region_parameter(region, "aws")
    return {"region_name": resolved_region, **kwargs}


def boto3_client_kwargs(service: str, region: str, **kwargs: Any) -> dict[str, Any]:
    """
    Generate boto3 client kwargs with resolved region.

    Args:
        service: AWS service name (e.g., 'ec2', 's3')
        region: Canonical region name or AWS region
        **kwargs: Additional client parameters

    Returns:
        Dictionary of client parameters with resolved region_name

    Example:
        >>> client_kwargs = boto3_client_kwargs('ec2', 'virginia')
        >>> client = boto3.client(**client_kwargs)
    """
    resolved_region = resolve_region_parameter(region, "aws")
    return {"service_name": service, "region_name": resolved_region, **kwargs}


# Azure Integrations
def azure_credential_kwargs(region: str, **kwargs: Any) -> dict[str, Any]:
    """
    Generate Azure credential kwargs with resolved region.

    Args:
        region: Canonical region name or Azure region
        **kwargs: Additional credential parameters

    Returns:
        Dictionary with resolved location parameter

    Example:
        >>> cred_kwargs = azure_credential_kwargs('virginia')
        >>> # Use with Azure SDK clients
    """
    resolved_region = resolve_region_parameter(region, "azure")
    return {"location": resolved_region, **kwargs}


# GCP Integrations
def gcp_client_kwargs(region: str, **kwargs: Any) -> dict[str, Any]:
    """
    Generate GCP client kwargs with resolved region.

    Args:
        region: Canonical region name or GCP region
        **kwargs: Additional client parameters

    Returns:
        Dictionary with resolved region parameter

    Example:
        >>> client_kwargs = gcp_client_kwargs('virginia')
        >>> # Use with Google Cloud client libraries
    """
    resolved_region = resolve_region_parameter(region, "gcp")
    return {"region": resolved_region, **kwargs}
