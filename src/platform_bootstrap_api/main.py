from __future__ import annotations

from fastapi import FastAPI

from platform_bootstrap_api.schemas import BootstrapRequest, BootstrapResponse

app = FastAPI(title="platform-bootstrap-api")


@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True}


@app.post("/bootstrap", response_model=BootstrapResponse)
def bootstrap(request: BootstrapRequest) -> BootstrapResponse:
    actions = [
        f"ensure repo exists: {request.owner}/{request.repo}",
        f"upsert CODEOWNERS -> {request.codeowners}",
        "upsert SECURITY.md",
        "upsert CONTRIBUTING.md",
        "upsert .github/workflows/ci.yml",
        f"set branch protection on {request.default_branch}",
    ]
    return BootstrapResponse(ok=True, dry_run=request.dry_run, actions=actions)
