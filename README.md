# platform-bootstrap-api

A privacy-safe FastAPI service that plans repository bootstrap actions.

This project models a common platform engineering pattern:
exposing baseline repository standards (ownership, CI, and branch protection)
through an API instead of relying on manual setup or tribal knowledge.

Default behavior is **dry-run**, ensuring no external writes occur unless explicitly implemented.

---

## Why this exists

Platform teams often standardize:

- Repository hygiene
- CODEOWNERS enforcement
- CI defaults
- Security documentation
- Branch protection policies

Rather than configuring each repository manually, this service demonstrates
how those guardrails can be encoded into an internal platform API.

The focus is repeatability, safety, and clarity.

---

## Features

- Health check endpoint (`/healthz`)
- Bootstrap planning endpoint (`/bootstrap`)
- Dry-run by default for privacy and safety
- Clear separation between API layer and bootstrap logic

---

## Local development

Install dependencies:

```bash
python -m pip install -e .[dev]
```

Run the API:

```bash
uvicorn platform_bootstrap_api.main:app --reload --port 8000
```

---

## API usage

Health check:

```bash
curl http://localhost:8000/healthz
```

Bootstrap (dry-run default):

```bash
curl -X POST http://localhost:8000/bootstrap \
  -H "Content-Type: application/json" \
  -d '{"owner":"acme","repo":"demo-repo"}'
```

Example response:

```json
{
  "ok": true,
  "dry_run": true,
  "actions": [
    "ensure repo exists: acme/demo-repo",
    "upsert CODEOWNERS -> @my-org/platform",
    "upsert SECURITY.md",
    "upsert CONTRIBUTING.md",
    "upsert .github/workflows/ci.yml",
    "set branch protection on main"
  ]
}
```

---

## Architecture

```
Client → FastAPI → Bootstrap Planner → (future) GitHub API client
```

- FastAPI handles request validation
- Bootstrap planner defines platform policy
- GitHub client abstraction enables future real execution

---

## Roadmap

- Integrate with `platform-bootstrap` package for real execution
- Add optional authentication header
- Support policy packs and organization-wide defaults
- Containerized deployment example
