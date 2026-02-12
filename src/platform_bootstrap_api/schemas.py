from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class BootstrapRequest(BaseModel):
    owner: str = Field(..., description="Repository owner or organization.")
    repo: str = Field(..., description="Repository name.")
    default_branch: str = Field("main", description="Default branch name.")
    codeowners: str = Field(
        "@my-org/platform",
        description="CODEOWNERS entry for the repository.",
    )
    dry_run: bool = Field(True, description="If true, no external writes occur.")


class BootstrapResponse(BaseModel):
    ok: bool
    dry_run: bool
    actions: List[str]
