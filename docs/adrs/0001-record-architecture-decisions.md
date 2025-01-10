# Architecture Decision Record 1: Establish Format for ADRs

Document technical and software architecture decisions in records like this one.

:white_check_mark: _Status:_ Implemented January 2024
:ticket: [Decide whether to use ADRs](https://github.com/DOI-OS-ORDA/DARTS/issues/13)
:busts_in_silhouette: [Our meeting about ADRs](https://docs.google.com/document/d/1hiQZG-PVklW5Y-Dk03r9kYafTTdw-Ol9wAq7H5Q2ni0/edit?tab=t.0#heading=h.vgkb99dm1sxm)

## Context

ORDA and 18F are modernizing DARTS. As we started to make technical decisions, we felt we should write down our reasoning for later reference.

## Decision

We will record our tech decisions in Architecture Decision Record (ADRs). We will keep the ADRs in source control of the relevant codebase. When ADRs relate to a GitHub issue, we will tag the ticket as ADR-related and we will link to it from the ADR.

**Format:** ADRs will be based upon [a template](./xxxx-template.md).

**Subject matter:** ADRs are *only* for technical decisions. ADRs are *not* product, design, or business-level decisions. *This* ADR is about technical documentation, which counts and is encouraged.

**Immutability:** ADRs are loosely immutable. When a decision is superseded, a new one should be issued to replace it. We will add a note to the old ADR's text (and maybe the filename) saying "overwritten" or "superseded."

## Consequences

Our hope is that ADRs will forestall speculation, arguments, and confusion about past decisions by illuminating the reasoning used at the time.

Our ADRs will be subject to code review by the team. Like anything in shared source control, they will be collaborative documents. Only people with GitHub access will be able to easily participate.

## Alternatives Considered

We considered using only GitHub issues / ticketing system to store ADRs, with no folder and no markdown files. The proposal was that descriptions or comments in the issue would detail our decisions. The issues would be tagged as ADRs; one would find the complete list of ADRs by sorting for this label. We decided not to do this, but we did keep the idea of tagging issues as ADR-related.

We considered avoiding the jargon "ADR" by calling this folder `decisions` instead of `adrs`. But, we thought that a more-general name might invite non-engineering decisions. We wanted only decisions closely connected to the codebase to be stored here in source control.
