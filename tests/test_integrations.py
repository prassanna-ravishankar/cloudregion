"""
Tests for SDK integration helpers.
"""

import pytest

from cloudregion.integrations import (
    azure_credential_kwargs,
    boto3_client_kwargs,
    boto3_session_kwargs,
    gcp_client_kwargs,
    resolve_region_parameter,
)


class TestResolveRegionParameter:
    """Test the resolve_region_parameter helper function."""

    def test_resolve_canonical_region(self):
        """Test resolving canonical region names."""
        assert resolve_region_parameter("virginia", "aws") == "us-east-1"
        assert resolve_region_parameter("virginia", "azure") == "eastus"
        assert resolve_region_parameter("virginia", "gcp") == "us-east1"

    def test_resolve_alias_region(self):
        """Test resolving alias region names."""
        assert resolve_region_parameter("us-east", "aws") == "us-east-1"
        assert resolve_region_parameter("eu-west", "azure") == "northeurope"

    def test_resolve_provider_specific_region(self):
        """Test that provider-specific regions pass through unchanged."""
        assert resolve_region_parameter("us-east-1", "aws") == "us-east-1"
        assert resolve_region_parameter("eastus", "azure") == "eastus"
        assert resolve_region_parameter("us-east1", "gcp") == "us-east1"

    def test_resolve_invalid_region_for_provider(self):
        """Test error handling for regions not available in provider."""
        # This would test a scenario where a region doesn't exist for a provider
        # For now, all our regions support all providers
        pass


class TestBoto3Integration:
    """Test boto3 integration helpers."""

    def test_boto3_session_kwargs(self):
        """Test boto3 session kwargs generation."""
        kwargs = boto3_session_kwargs("virginia")
        assert kwargs == {"region_name": "us-east-1"}

    def test_boto3_session_kwargs_with_additional_params(self):
        """Test boto3 session kwargs with additional parameters."""
        kwargs = boto3_session_kwargs("virginia", profile_name="dev", aws_access_key_id="test")
        expected = {"region_name": "us-east-1", "profile_name": "dev", "aws_access_key_id": "test"}
        assert kwargs == expected

    def test_boto3_client_kwargs(self):
        """Test boto3 client kwargs generation."""
        kwargs = boto3_client_kwargs("ec2", "virginia")
        expected = {"service_name": "ec2", "region_name": "us-east-1"}
        assert kwargs == expected

    def test_boto3_client_kwargs_with_additional_params(self):
        """Test boto3 client kwargs with additional parameters."""
        kwargs = boto3_client_kwargs("s3", "oregon", aws_access_key_id="test")
        expected = {"service_name": "s3", "region_name": "us-west-2", "aws_access_key_id": "test"}
        assert kwargs == expected


class TestAzureIntegration:
    """Test Azure integration helpers."""

    def test_azure_credential_kwargs(self):
        """Test Azure credential kwargs generation."""
        kwargs = azure_credential_kwargs("virginia")
        assert kwargs == {"location": "eastus"}

    def test_azure_credential_kwargs_with_additional_params(self):
        """Test Azure credential kwargs with additional parameters."""
        kwargs = azure_credential_kwargs("frankfurt", subscription_id="test-sub")
        expected = {"location": "germanywestcentral", "subscription_id": "test-sub"}
        assert kwargs == expected


class TestGCPIntegration:
    """Test GCP integration helpers."""

    def test_gcp_client_kwargs(self):
        """Test GCP client kwargs generation."""
        kwargs = gcp_client_kwargs("virginia")
        assert kwargs == {"region": "us-east1"}

    def test_gcp_client_kwargs_with_additional_params(self):
        """Test GCP client kwargs with additional parameters."""
        kwargs = gcp_client_kwargs("tokyo", project="test-project")
        expected = {"region": "asia-northeast1", "project": "test-project"}
        assert kwargs == expected


class TestIntegrationWithAliases:
    """Test integration helpers work with aliases."""

    def test_boto3_with_alias(self):
        """Test boto3 helpers work with region aliases."""
        kwargs = boto3_session_kwargs("us-east")
        assert kwargs == {"region_name": "us-east-1"}

    def test_azure_with_alias(self):
        """Test Azure helpers work with region aliases."""
        kwargs = azure_credential_kwargs("eu-west")
        assert kwargs == {"location": "northeurope"}

    def test_gcp_with_alias(self):
        """Test GCP helpers work with region aliases."""
        kwargs = gcp_client_kwargs("asia-southeast")
        assert kwargs == {"region": "asia-southeast1"}


if __name__ == "__main__":
    pytest.main([__file__])
