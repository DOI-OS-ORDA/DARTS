# Architecture decision record 3: Containerization

Brief description

* :white_check_mark: _Status:_ Implemented
* :busts_in_silhouette: _Meeting:_ [29 January 2025](https://docs.google.com/document/d/1hiQZG-PVklW5Y-Dk03r9kYafTTdw-Ol9wAq7H5Q2ni0/edit?tab=t.0#heading=h.8kq0024yofc5)

## Context

In our work replatforming DARTS, we face the question: will we run [our tech stack](./0002-python-django-postgres.md) from within a [container](https://en.wikipedia.org/wiki/Containerization_(computing))? Here are some of our considerations:
* The [18F engineering guide recommends](https://guides.18f.gov/engineering/tools/docker/) containerization with Docker Compose to control dependencies in different development environments.
* Cloud.gov [supports Docker images](https://cloud.gov/docs/deployment/docker/)
* Containerization adds a dependency and (at least at first) technical overhead.

## Decision

We will implement containerization with Docker and Docker Compose. We believe these tools' capability to hide complexity justifies their costs.

* :white_check_mark: We will maintain in our [`Dockerfile`](../../Dockerfile) and [`docker-compose.yml`](../../docker-compose.yml) current components and dependencies required for the code to run locally, via `docker compose up`.
* :white_check_mark: We will provide scripts in `bin/` that simplify commonly-used long Docker Compose commands.
* :x: We discourage including in the `Dockerfile` tools that aren't needed for running or testing the application, such as tools only needed for asset compilation.

## Consequences

* Developers can run the DARTS app from a Docker container. This is not required, but provided for consistency and convenience.
* Containerization will smooth over some complexity of setting up a local development environment.
* The development process is now dependent (at least loosely) on Docker, Docker Compose, and Docker Desktop, including its license agreement and cost.
* Running commands within the application (Python REPL, etc.) requires going through Docker. This incurs extra steps at the command line or the maintance of `bin/` scripts to simplify commands.

## Alternatives Considered

* We considered not employing containerization, instead requiring developers to install the codebase's dependencies directly. However, machine and platform differences can lead to inconsistencies. Given that we have system-level tools (xpdf, firefox-esr, geckodriver) as well as Python versions and packages to install, using containerization is simpler, cleaner, and more consistent.
* We considered including in the container tools that, while not needed at runtime, might be useful utilities for developers. For example, in order to more easily build USWDS CSS files with `nodejs` and `npm`, we experimented with including these in the `Dockerfile`. We [chose to undo this experiment](https://github.com/DOI-OS-ORDA/DARTS/commit/5a95943447921a9bc2db29b238bb763b8b1b2284) because their inclusion in the container did not add enough value to justify the increased build time and added dependency.
