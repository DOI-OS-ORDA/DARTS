# Architecture decision record 3: Containerization

Brief description

* :eyes: _Status:_ Proposed
* :ticket: _Issue:_ Link to github issue
* :busts_in_silhouette: _Meeting:_ Link to meeting notes

## Context

In our work replatforming DARTS, we face the question: will we run [our tech stack](./0002-python-django-postgres.md) from within a [container](https://en.wikipedia.org/wiki/Containerization_(computing))? Here are some of our considerations:
* The [18F engineering guide recommends](https://guides.18f.gov/engineering/tools/docker/) containerization with Docker Compose to control dependencies in different development environments.
* Cloud.gov [supports Docker images](https://cloud.gov/docs/deployment/docker/)
* Containerization adds a dependency and (at least at first) technical overhead.

## Decision

We will implement containerization with Docker and Docker Compose. We believe these tools' capability to hide complexity justifies their costs.

* :white_check_mark: We will maintain in our [`Dockerfile`](../../Dockerfile) a current list of dependencies required for the code to run locally, on a developer's laptop, in a Docker container.
* :white_check_mark: We will maintain in our [`docker-compose.yml`](../../docker-compose.yml) all of the components needed to run the entire application system locally, via `docker compose up`.
* :x: We discourage including in the `Dockerfile` tools that aren't needed for running or testing the application, such as tools only needed for asset compilation.

## Consequences

* Developers can run the DARTS app from a Docker container. This is not required, but provided for consistency and convenience.
* Containerization will smooth over some complexity of setting up a local development environment.
* The development process is now dependent (at least loosely) on Docker, Docker Compose, and Docker Desktop, including its license agreement and cost.
* Running commands within the application (Python REPL, etc.) requires going through Docker, though we have partially mitigated this complexity by providing `bin/` scripts that simplify commonly-used long Docker Compose commands.

## Alternatives Considered

* We considered not employing containerization, instead requiring developers to install the codebase's dependencies directly. However, machine and platform differences can lead to inconsistencies. Given that we have system-level tools (xpdf, firefox-esr, geckodriver) as well as Python versions and packages to install, using containerization is simpler, cleaner, and more consistent.
* We considered including in the container tools that, while not needed at runtime, might be useful utilities for developers. For example, in order to more easily build USWDS CSS files with `nodejs` and `npm`, we experimented with including these in the `Dockerfile`. We [chose to undo this experiment](https://github.com/DOI-OS-ORDA/DARTS/commit/5a95943447921a9bc2db29b238bb763b8b1b2284) because their inclusion in the container did not add enough value to justify the increased build time and added dependency.
