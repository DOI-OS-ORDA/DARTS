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
python manage.py import "test_docs/*"
```

From there, to use a Python environment, run:

```sh
python manage.py shell
```

Run tests with the following commands:

```sh
# Run all tests
docker compose run -it --remove-orphans web coverage run --source='.' manage.py test --pattern '*_test.py'

# Run only feature tests
docker compose run -it --remove-orphans web coverage run --source='.' manage.py test --pattern '*_test.py' feature_tests

# Run a scoped-down set of unit tests, in this case search/tests/operations/*.py
docker compose run -it --remove-orphans web coverage run --source='.' manage.py test --pattern '*_test.py' search.tests.operations

# Get a test coverage report
docker compose run -it --remove-orphans web coverage report
```

We recommend creating a shell alias that runs `docker compose run -it --remove-orphans web coverage run --source='.' manage.py test --pattern '*_test.py'`. We use `dt` to indicate `"docker...test"`. With that, for example, `dt feature_tests` would run the full command to run just feature tests.


## OUR ESSENCE

The Office of Restoration and Damage Assessment (ORDA) at the Department of Interior (Interior) plays a crucial role within the Interior's Natural Resource Damage Assessment and Restoration (NRDAR) Program. It's responsible for coordinating efforts to assess damage to natural resources and determine the necessary restoration actions following environmental incidents, such as hazardous substance releases. The ORDA works closely with state, tribal, and federal trustee agencies to conduct damage assessments as the initial step toward restoring affected resources.  The ORDA's activities are geared towards ensuring that public natural resources injured or destroyed due to hazardous substance releases are restored, replaced, or that their equivalents are acquired.

The Damage Assessment and Restoration Tracking System (DARTS) is a significant tool developed by the ORDA to support the NRDAR Program.
DARTS serves as an interactive platform designed to track cases involving the assessment of damages and restoration of natural resources injured by oil spills or hazardous substances released into the environment. It is a web-based tool that provides details on each case from initial damage assessment through claims resolution, restoration, monitoring, and case closures. The system is used by a wide audience, which includes the ORDA, those affected by spills and releases, and the general public with research interests in this area.


## Mission

The mission of DOI ORDA (Office of Restoration and Damage Assessment) is to restore natural resources that have been injured due to oil spills or the release of hazardous substances into the environment.

This effort is part of their broader Natural Resource Damage Assessment and Restoration (NRDA) program.


## Project

A team from 18F, in collaboration with our partners at the Office of Restoration and Damage Assessment (ORDA), dedicated twelve weeks to understanding the Damage Assessment and Restoration Tracking System (DARTS) and its users.

**Problem Statement:** We are building a modern and simplified case information management and tracking system that will alleviate many of the current user challenges with navigating and queries.
The new DARTS will reduce manual processes and improve the functionality for users.

**Vision Statement:** ORDA’s Vision is to create an intuitive, user-friendly, streamlined system that DARTS users can trust to deliver accurate NRDAR information,reduce the need for constant maintenance and support,and empower users to work more
efficiently.

**Phase 1:** The objective was to provide recommendations for enhancing the user experience of case managers and other users involved in the various NRDAR processes within the system, as well as to outline a roadmap for future development. ***Completed October 2024***
[DARTS Final  Presentation](https://docs.google.com/presentation/d/16QfQCxpfH1_BZDkp-cuHFb0dvJPaU2l29IMI0F_XLPU/edit#slide=id.g30d737a98d2_0_274)

**Phase 2: December 2024 In-Process**
