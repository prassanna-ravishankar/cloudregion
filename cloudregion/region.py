"""
Core Region class for cloud provider region mapping.
"""

from typing import Optional

from .region_data import REGION_ALIASES, REGION_MAPPINGS


class CloudRegionError(Exception):
    """Base exception for cloud region errors."""

    pass


class UnknownRegionError(CloudRegionError):
    """Raised when a region name is not recognized."""

    def __init__(self, region_name: str, available_regions: list[str]):
        """Initialize the exception with the unknown region and available options."""
        message = f"Unknown region '{region_name}'. Available regions: {', '.join(available_regions)}"
        super().__init__(message)


class Region:
    """
    Represents a canonical cloud region with provider-specific mappings.

    A Region object provides access to provider-specific region identifiers
    through properties (.aws, .azure, .gcp) based on a canonical city name.

    Example:
        >>> r = Region('virginia')
        >>> r.aws
        'us-east-1'
        >>> r.azure
        'eastus'
        >>> r.gcp
        'us-east1'
    """

    def __init__(self, canonical_name: str) -> None:
        """
        Initialize a Region with a canonical city-based name.

        Args:
            canonical_name: City-based region name (e.g., 'virginia', 'tokyo')

        Raises:
            UnknownRegionError: If the canonical name is not recognized
        """
        # Normalize name to lowercase for lookup
        normalized_name = canonical_name.lower().strip()

        # Check if it's an alias first
        if normalized_name in REGION_ALIASES:
            normalized_name = REGION_ALIASES[normalized_name]

        # Verify the canonical name exists
        if normalized_name not in REGION_MAPPINGS:
            available_regions = sorted(list(REGION_MAPPINGS.keys()) + list(REGION_ALIASES.keys()))
            raise UnknownRegionError(canonical_name, available_regions)

        self._canonical_name = normalized_name
        self._mappings = REGION_MAPPINGS[normalized_name]

    @property
    def canonical(self) -> str:
        """Return the canonical city-based region name."""
        return self._canonical_name

    @property
    def aws(self) -> Optional[str]:
        """Return the AWS region identifier."""
        return self._mappings.get("aws")

    @property
    def azure(self) -> Optional[str]:
        """Return the Azure region identifier."""
        return self._mappings.get("azure")

    @property
    def gcp(self) -> Optional[str]:
        """Return the Google Cloud Platform region identifier."""
        return self._mappings.get("gcp")

    def __str__(self) -> str:
        """Return string representation of the region."""
        return f"Region('{self._canonical_name}')"

    def __repr__(self) -> str:
        """Return detailed string representation of the region."""
        return f"Region('{self._canonical_name}': aws='{self.aws}', azure='{self.azure}', gcp='{self.gcp}')"

    def __eq__(self, other: object) -> bool:
        """Test equality with another Region object."""
        if not isinstance(other, Region):
            return NotImplemented
        return self._canonical_name == other._canonical_name

    def __hash__(self) -> int:
        """Return hash for use in sets and as dictionary keys."""
        return hash(self._canonical_name)
