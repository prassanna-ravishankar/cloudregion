"""
cloudregion - Simple Python library for cloud region mapping.

Converts between canonical city-based region names and provider-specific
region identifiers across AWS, Azure, and Google Cloud Platform.

Basic usage:
    >>> from cloudregion import region
    >>> r = region('virginia')
    >>> r.aws
    'us-east-1'
    >>> r.azure
    'eastus'
    >>> r.gcp
    'us-east1'
"""

from .region import CloudRegionError, Region, UnknownRegionError

__version__ = "0.0.1"
__all__ = ["CloudRegionError", "Region", "UnknownRegionError", "region"]


def region(canonical_name: str) -> Region:
    """
    Create a Region object from a canonical city-based region name.

    This is the main entry point for the library. It accepts city-based
    region names and returns a Region object with provider-specific
    region mappings accessible via properties.

    Args:
        canonical_name: City-based region name (e.g., 'virginia', 'tokyo', 'frankfurt')
                       Also accepts common aliases like 'us-east', 'eu-west'

    Returns:
        Region object with .aws, .azure, .gcp properties

    Raises:
        UnknownRegionError: If the region name is not recognized

    Examples:
        >>> r = region('virginia')
        >>> r.aws
        'us-east-1'

        >>> r = region('tokyo')
        >>> r.azure
        'japaneast'

        >>> # Using aliases
        >>> region('us-east').canonical
        'virginia'
    """
    return Region(canonical_name)
