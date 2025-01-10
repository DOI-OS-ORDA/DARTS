# Architecture Decision Record 1: Establish Format for ADRs

We document technical and software architecture decisions in records like this one.

* :white_check_mark: _Status:_ Implemented January 2024
* :ticket: _Issue:_ [Decide whether to use ADRs](https://github.com/DOI-OS-ORDA/DARTS/issues/13)
* :busts_in_silhouette: _Meeting:_ [About ADRs](https://docs.google.com/document/d/1hiQZG-PVklW5Y-Dk03r9kYafTTdw-Ol9wAq7H5Q2ni0/edit?tab=t.0#heading=h.vgkb99dm1sxm)

## Context

ORDA and 18F are modernizing DARTS. As we started to make technical decisions, we felt we should write down our reasoning for later reference. We had a [joint team meeting](https://docs.google.com/document/d/1hiQZG-PVklW5Y-Dk03r9kYafTTdw-Ol9wAq7H5Q2ni0/edit?tab=t.0#heading=h.vgkb99dm1sxm) on 7 January 2025 on which we outlined the following.

## Decision

We will record our tech decisions in Architecture Decision Record (ADRs). We will keep the ADRs in the source control repo of the relevant codebase. When an ADR relates to a GitHub issue ticket, we will tag the issue as ADR-related and we will link to it from the ADR.

**Format:** ADRs will be based upon [this template](./xxxx-template.md).

**Subject matter:** ADRs are *only* for technical decisions. ADRs are *not* product, design, or business-level decisions. Good subjects for ADRs: the selection of a library, a design pattern, a development practice, or (like the current ADR) a technical documentation practice.

**Immutability:** ADRs are loosely immutable. When a decision is superseded, a new ADR should be issued to replace the old. We will add a note to the old ADR's text (and maybe the filename) saying "overwritten" or "superseded."

## Consequences

Our hope is that ADRs will forestall speculation, arguments, and confusion about past decisions by illuminating the reasoning used at the time.

Our ADRs will be subject to code review by the team. Like anything in shared source control, they will be collaborative documents. Only people with GitHub access will be able to easily participate.

Because they are stored in a public repo, ADRs will expose our reasoning and technical choices to the public. ADRs with security implications will need to be accepted by the OCIO.

## Alternatives Considered

We considered using only GitHub issues to store ADRs – no folder, no markdown files. Our decisions would be recorded in the text or comments of the issues. An "ADR" issue tag would make it possible to find them all. We decided not to do this because it did not seem robust enough. But, we did keep the idea of tagging issues as ADR-related.

We considered avoiding the jargon "ADR" by calling this folder `decisions` instead of `adrs`. But, we thought that a more-general name might invite non-engineering decisions. We wanted only decisions closely connected to the codebase to be stored here in source control.

We considered recording technical decisions in the same place as product or design decisions. Because product decisions are typically recorded in a roadmap and design decisions in user stories, we decided to restrict ADRs to technical decisions only.
