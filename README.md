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
bin/run app sh
```

Migrate the database for the search app:

```sh
bin/manage migrate search
```

Set up fixture data with this command:

```sh
bin/manage loaddata regions users persons cases
```

Import documents with this command:

```sh
bin/manage import
```

To use a Python environment shell, run:

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

### Inline `<script>` and `<style>` security

The system's Content-Security-Policy header prevents `<script>` and `<style>`
tags from working without further configuration. Use `<%%= javascript_tag
nonce: true %>` for inline javascript.

See the [CSP compliant script tag helpers](./doc/adr/0004-rails-csp-compliant-script-tag-helpers.md) ADR for
more information on setting these up successfully.

### Running tests

* Tests: `bin/pipenv run darts/manage.py test`
* Python linter: `bin/pipenv run black`
* Dynamic security scan: `bin/run owasp`
* Static security scan: `bin/pipenv run bandit -r .`
* Python dependency checks: `bin/pipenv check`

### Automatic linting

To enable automatic Python linting on every `git commit` follow the instructions
at the top of `.githooks/pre-commit`

## CI/CD

### Deployment

Each environment has dependencies on a PostgreSQL RDS instance managed by cloud.gov.
See [cloud.gov docs](https://cloud.gov/docs/services/relational-database/) for information on RDS.

#### Deploying to development

TBD


### Configuring ENV variables in cloud.gov

All configuration that needs to be added to the deployed application's ENV should be added to
the `env:` block in `manifest.yml`

Items that are both **public** and **consistent** across staging and production can be set directly there.

Otherwise, they are set as a `((variable))` within `manifest.yml` and the variable is defined depending on sensitivity:

#### Credentials and other Secrets

#### Non-secrets

Configuration that changes from staging to production, but is public, should be added to `config/deployment/staging.yml` and `config/deployment/production.yml`

## Documentation

### Architectural Decision Records

Architectural Decision Records (ADR) are stored in `doc/adr`
To create a new ADR, first install [ADR-tools](https://github.com/npryce/adr-tools) if you don't
already have it installed.
* `brew bundle` or `brew install adr-tools`

Then create the ADR:
*  `adr new Title Of Architectural Decision`

This will create a new, numbered ADR in the `doc/adr` directory.

Compliance diagrams are stored in `doc/compliance`. See the README there for more information on
generating diagram updates.

## Contributing

*This will continue to evolve as the project moves forward.*

* Pull down the most recent main before checking out a branch
* Write your code
* If a big architectural decision was made, add an ADR
* Submit a PR
  * If you added functionality, please add tests.
  * All tests must pass!
* Ping the other engineers for a review.
* At least one approving review is required for merge.
* Rebase against main before merge to ensure your code is up-to-date!
* Merge after review.
  * Squash commits into meaningful chunks of work and ensure that your commit messages convey meaning.

## Story Acceptance

TBD
