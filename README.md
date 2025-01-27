# ORDA DARTS

## Installation

Clone this repository and navigate into it.

To use Docker to start all services, run

```sh
docker compose up
```

Then visit <http://localhost:8000> to see the site.

To reach a shell within the Docker container, run

```sh
docker compose run -it --remove-orphans web sh
```

Migrate the database for the search app

```sh
bin/manage migrate search
```

Import documents with this command:

```sh
bin/manage import
```

To use a Python environment, run:

```sh
bin/manage shell
```

## Testing

Run tests with the following commands:

```sh
# Run all tests
bin/testall

# Run all Cucumber / behave features
bin/features

# Run all feature tests (this is different than the last one, believe it or not)
bin/feature_test

# Run all unit tests (with code coverage analysis)
bin/test

# Run a scoped-down set of unit tests, in this case search/tests/operations/*.py
bin/test search.tests.operations

# Get a test coverage report
bin/coverage
```
