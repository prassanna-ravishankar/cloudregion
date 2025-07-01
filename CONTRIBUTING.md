# Contributing to `cloudregion`

First off, thank you for considering contributing to `cloudregion`. It's people like you that make open source such a great community! Your contributions are welcome, and they are greatly appreciated.

## 🚀 How to Contribute

There are many ways to contribute to the project. Here are a few ideas:

### 🗺️ Adding New Regions or Aliases

The core of `cloudregion` is its mapping data. If you find a region that's missing or has an alias that could be added, this is a great way to contribute.

1.  **Edit the data files**: All region data is stored in `cloudregion/region_data.py`.
    *   To add a new region, add an entry to the `REGION_MAPPINGS` dictionary. Please ensure you add the region for all providers (AWS, Azure, GCP).
    *   To add a new alias, add an entry to the `REGION_ALIASES` dictionary.

2.  **Add tests**: We aim for 100% test coverage. Please add a test case to `tests/test_region.py` that verifies your new region or alias works as expected.

3.  **Update documentation**: If you've added a new region, please update the "Supported Regions" table in `README.md`.

### ⚙️ Adding New SDK Integrations

We want to make `cloudregion` as useful as possible, and that includes integrating with popular SDKs.

1.  **Add an integration function**: New integration helpers should be added to `cloudregion/integrations.py`. Follow the existing patterns for `boto3`, `azure`, and `gcp`.

2.  **Add tests**: Create a new test file in the `tests/` directory (e.g., `tests/test_integrations.py`) and add test cases for your new integration.

3.  **Update documentation**: Add a section to the `README.md` demonstrating how to use your new integration.

### 🐛 Reporting Bugs or Proposing Features

-   **Report bugs**: If you find a bug, please open an issue and provide detailed steps to reproduce it.
-   **Propose features**: If you have an idea for a new feature, open an issue to start a discussion. We're particularly interested in ideas related to the project [Roadmap](https://github.com/prassanna-ravishankar/cloudregion#%-roadmap) outlined in the `README.md`.

## 🛠️ Development Setup

Ready to contribute? Here's how to set up `cloudregion` for local development.

1.  **Fork and Clone**: Fork the repository on GitHub and clone it locally.

    ```bash
    git clone git@github.com:YOUR_USERNAME/cloudregion.git
    cd cloudregion
    ```

2.  **Install Environment**: This project uses `uv` for environment management.

    ```bash
    uv sync --dev
    ```

3.  **Install Pre-commit Hooks**: We use `pre-commit` to run linters and formatters.

    ```bash
    uv run pre-commit install
    ```

4.  **Create a Branch**:

    ```bash
    git checkout -b your-feature-or-bugfix-branch
    ```

5.  **Run Checks**: Before submitting, please run the checks to ensure everything is in order.

    ```bash
    make check  # Runs formatting and linting
    make test   # Runs the test suite
    ```

6.  **Submit a Pull Request**: Push your changes to your fork and open a pull request. Please provide a clear description of your changes.

Thank you for your contribution!
