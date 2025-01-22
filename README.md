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

Import documents with this command:

```sh
python manage.py import
```

To use a Python environment, run:

```sh
python manage.py shell
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

We recommend creating a shell alias that runs `docker compose run -it --remove-orphans web coverage run --source='.' manage.py test --pattern '*_test.py'`. We use `dt` to indicate `"docker...test"`. With that, for example, `dt feature_tests` would run the full command to run just feature tests.
