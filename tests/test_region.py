"""
Tests for cloudregion library.
"""

import pytest

from cloudregion import CloudRegionError, Region, UnknownRegionError, region


class TestRegion:
    """Test the Region class."""

    def test_region_creation_with_canonical_name(self):
        """Test creating a region with canonical city name."""
        r = Region("virginia")
        assert r.canonical == "virginia"
        assert r.aws == "us-east-1"
        assert r.azure == "eastus"
        assert r.gcp == "us-east1"

    def test_region_creation_with_alias(self):
        """Test creating a region with alias name."""
        r = Region("us-east")
        assert r.canonical == "virginia"
        assert r.aws == "us-east-1"

    def test_region_case_insensitive(self):
        """Test that region names are case-insensitive."""
        r1 = Region("Virginia")
        r2 = Region("VIRGINIA")
        r3 = Region("virginia")

        assert r1.canonical == r2.canonical == r3.canonical == "virginia"

    def test_region_whitespace_handling(self):
        """Test that whitespace is handled correctly."""
        r = Region("  virginia  ")
        assert r.canonical == "virginia"

    def test_unknown_region_raises_error(self):
        """Test that unknown regions raise UnknownRegionError."""
        with pytest.raises(UnknownRegionError) as exc_info:
            Region("unknown-region")

        assert "Unknown region" in str(exc_info.value)
        assert "Available regions:" in str(exc_info.value)

    def test_region_equality(self):
        """Test region equality comparison."""
        r1 = Region("virginia")
        r2 = Region("virginia")
        r3 = Region("us-east")  # alias for virginia
        r4 = Region("oregon")

        assert r1 == r2
        assert r1 == r3  # alias should be equal
        assert r1 != r4
        assert r1 != "virginia"  # different type

    def test_region_hash(self):
        """Test that regions can be hashed and used in sets."""
        r1 = Region("virginia")
        r2 = Region("virginia")
        r3 = Region("oregon")

        region_set = {r1, r2, r3}
        assert len(region_set) == 2  # r1 and r2 should be deduplicated

    def test_region_string_representations(self):
        """Test string representations of regions."""
        r = Region("virginia")

        assert str(r) == "Region('virginia')"
        assert "virginia" in repr(r)
        assert "us-east-1" in repr(r)
        assert "eastus" in repr(r)


class TestRegionFunction:
    """Test the main region() function."""

    def test_region_function_returns_region_object(self):
        """Test that region() function returns Region object."""
        r = region("virginia")
        assert isinstance(r, Region)
        assert r.canonical == "virginia"

    def test_region_function_with_alias(self):
        """Test region() function with alias."""
        r = region("us-east")
        assert r.canonical == "virginia"

    def test_region_function_unknown_region(self):
        """Test region() function with unknown region."""
        with pytest.raises(UnknownRegionError):
            region("unknown-region")


class TestRegionMappings:
    """Test specific region mappings."""

    def test_major_regions_have_all_providers(self):
        """Test that major regions have mappings for all providers."""
        major_regions = ["virginia", "oregon", "dublin", "frankfurt", "tokyo", "singapore"]

        for region_name in major_regions:
            r = region(region_name)
            assert r.aws is not None, f"{region_name} missing AWS mapping"
            assert r.azure is not None, f"{region_name} missing Azure mapping"
            assert r.gcp is not None, f"{region_name} missing GCP mapping"

    def test_specific_region_mappings(self):
        """Test specific known region mappings."""
        test_cases = [
            ("virginia", "us-east-1", "eastus", "us-east1"),
            ("oregon", "us-west-2", "westus2", "us-west1"),
            ("dublin", "eu-west-1", "northeurope", "europe-west1"),
            ("tokyo", "ap-northeast-1", "japaneast", "asia-northeast1"),
        ]

        for canonical, aws_expected, azure_expected, gcp_expected in test_cases:
            r = region(canonical)
            assert r.aws == aws_expected
            assert r.azure == azure_expected
            assert r.gcp == gcp_expected

    def test_aliases_resolve_correctly(self):
        """Test that aliases resolve to correct canonical regions."""
        alias_tests = [
            ("us-east", "virginia"),
            ("us-west", "oregon"),
            ("eu-west", "dublin"),
            ("asia-southeast", "singapore"),
        ]

        for alias, expected_canonical in alias_tests:
            r = region(alias)
            assert r.canonical == expected_canonical


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_none_region_mapping(self):
        """Test handling of regions that don't exist in some providers."""
        # This would test a region that exists in some providers but not others
        # For now, all our regions have mappings for all providers
        pass

    def test_error_inheritance(self):
        """Test that custom exceptions inherit correctly."""
        assert issubclass(UnknownRegionError, CloudRegionError)
        assert issubclass(CloudRegionError, Exception)


if __name__ == "__main__":
    pytest.main([__file__])
