# Category Checklist - Web App / SaaS

Use when the target is a browser-delivered product (SaaS, dashboard, collaborative tool, marketing site with an app behind it). Work these axes while drafting docs 02, 03, 04, 06.

## Surface inventory

- Marketing site vs app vs docs vs status page - list URLs actually fetched
- Public API docs: endpoints, auth scheme, rate limits
- Public changelog / release notes cadence
- Export/data-portability pages (GDPR deletion, export buttons) - usually documented, rarely tested

## Auth and tenancy (public evidence only)

- SSO/SAML/OAuth providers named on pricing or docs pages
- Workspace/team model: seats, roles, guests - as *described*, not tested
- Public sign-up flow (does it require email verify? trial length?)

## Core object model

Infer primary objects from marketing nouns, docs, and API resources (e.g., "workspace → project → task → comment"). Label INFERRED. Missing fields → UNKNOWN, not guessed.

## Collaboration and sync

- Real-time co-editing claims (usually marketing → NOT TESTED)
- Offline behavior, conflict resolution - rarely public → open question
- Sharing model: public links, domain-restricted, password-protected

## Pricing and limits

- Tier table: seats, storage, API calls, automation runs
- What breaks at the limit (hard block vs overage billing)

## Integrations

- Named integrations from marketing or docs
- Webhook / API availability per tier
- Import from competitors (migration tools)

## Security / compliance signals

- SOC2 / ISO / GDPR badges (claims → NOT TESTED unless auditor report fetched)
- Subprocessors page if public

## Test-plan seeds (docs/10)

- Auth: unauthenticated access to core routes → expected redirect/401
- Sharing: public link exposes only intended object, not siblings
- Limits: create over-quota resource → expected refusal message
- Export: data export contains the objects docs claim

## Clean-room note

SaaS specs fail when they repackage marketing language as requirements. Keep "claimed vs tested" visible in 02; a rebuild should win on clarity, not on copying slogans.
