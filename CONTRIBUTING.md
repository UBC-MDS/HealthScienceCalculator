# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `healthsciencecalculator` for local development.

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/UBC-MDS/HealthScienceCalculator.git
   cd healthsciencecalculator
   ```
3. Install `healthsciencecalculator` using `poetry`:

    ```console
    $ poetry install
    ```

4. Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

4. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

5. Commit your changes and open a pull request.

### Documentation

We welcome:

- Fixed typos
- Improved explanations
- New examples
- Better organization
- Translations

## Style Guidelines

- Code: Follow PEP 8 and project-specific conventions and NumPy-style docstrings
- Commit messages: Follow conventional commits format
- Documentation: Clear, concise, and complete
- Tests: Unit tests for new features, regression tests for bugs

## Development Process

1. Make your changes in your feature branch
2. Write or update tests as needed
3. Update documentation to reflect any changes
4. Run the test suite:
   ```bash
   poetry run pytest
   poetry run pytest --cov=healthsciencecalculator
   ```
5. Run the linting checks:
   ```bash
   poetry run flake8
   poetry run black .
   poetry run mypy .
   ```

## Pull Request Process

1. Update the README.md with details of significant changes
2. Ensure all tests pass and code meets quality standards
3. Update the documentation if needed. 

  Example of good Numpy docstring:
  ```python
  def get_bmi(
    weight: float,
    height: float,
) -> BMIResult:
    """Calculate Body Mass Index (BMI) and return detailed classification information.

    BMI is calculated as weight (kg) divided by height (m) squared.

    Parameters
    ----------
    weight : float
        Weight in kilograms
    height : float
        Height in meters

    Returns
    -------
    BMIResult
        A dataclass containing:
        - bmi (float): The calculated BMI value
        - category (str): BMI category, one of:
            - 'underweight' (BMI < 18.5)
            - 'healthy' (BMI 18.5-24.9)
            - 'overweight' (BMI 25-29.9)
            - 'class 1 obesity' (BMI 30-34.9)
            - 'class 2 obesity' (BMI 35-39.9)
            - 'class 3 obesity' (BMI >= 40)
        - risk_level (str): Associated health risk level
    """

  ```

4. Link any relevant issues in the PR description
5. Request review from maintainers

### PR Checklist
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] Code follows project style guidelines
- [ ] Commits are properly formatted and descriptive
- [ ] Changes are described in CHANGELOG.md



## Code of Conduct

Please note that the `healthsciencecalculator` project is released with a
Code of Conduct. By contributing to this project you agree to abide by its terms.
