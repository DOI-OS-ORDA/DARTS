# Architecture decision record 2: Python, Django, PostgreSQL

The tech stack we selected for replatforming DARTS

* :white_check_mark: _Status:_ Implemented [December 2024](https://github.com/DOI-OS-ORDA/DARTS/commit/1858055b77cc9f840480fb4f9ddfe0314e0992ec)
* :ticket: _Epic:_ [Document search](https://github.com/DOI-OS-ORDA/DARTS/milestone/1)
* :busts_in_silhouette: _Meetings:_
    * [John & Deanna, 21 August 2024](https://docs.google.com/document/d/1hiQZG-PVklW5Y-Dk03r9kYafTTdw-Ol9wAq7H5Q2ni0/edit?tab=t.0#heading=h.o4jgj8cu2r4u)
    * [John & Matt, 27 November 2024](https://docs.google.com/document/d/1aI9Ef5yS-mzrNaTyvhhPe3E4PrWliudMGoEw9AWmwtM/)
    * [ORDA & 18F, 3 December 2024](https://docs.google.com/document/d/1hiQZG-PVklW5Y-Dk03r9kYafTTdw-Ol9wAq7H5Q2ni0/edit?tab=t.0#heading=h.wy6rvv8yun23)

## Context

18F's [Strategy Development final report](https://docs.google.com/document/d/1Rjov9MW8LuXyoqMj9ZXNThSpbCJx4F1BE7Siluc6obg/) concluded that ORDA should incrementally replace DARTS. The question arises of what tech stack to use in building the replacement. In particular, a programming language, framework, and database had to be selected to begin developing a document search system, which ORDA and 18F agreed was a good "first slice" of replatforming work.

ORDA, 18F, and USGS TWSC together considered the tech stack to use at a series of meetings in late 2024.

## Decision

We will replatform DARTS on this tech stack:
* Language: Python
* Web application framework: Django
* Primary database: PostgreSQL

## Consequences

The choice of a platform outside of .NET and the Microsoft ecosystem may be a challenge for ORDA and TWSC because it is less familiar. We hope that, in the long run, this choice will reduce vendor lock-in and promote maintainability of the codebase.

## Alternatives Considered

During the prior phase of the project, we considered building upon the .NET platform used by the DARTS legacy system. This would have the advantage of being familiar to ORDA and TWSC. We rejected this because there is no clear path to upgrade ASP.NET Web Forms beyond the version currently in use.

We considered Ruby on Rails because it is familiar to 18F and suited to the project. We decided in favor of Python because TWSC has Python expertise and supports existing Python code. We considered Python Flask as a starting point, but we thought we would run into Flask's limits quickly.

For a database, we considered Microsoft SQL Server because it is the legacy database used by DARTS and because TWSC has expertise in it. For document search, we considered Elasticsearch and Solr. Because PostgreSQL could serve these two purposes &mdash; both a database and, via full text search, a document search engine &mdash; we decided it was the more advantageous tool.

We have favored technologies that are open-source, widespread, and expected to be maintained over those that are closed, proprietary, uncommon, or approaching end-of-life.
