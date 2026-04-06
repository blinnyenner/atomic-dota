"""Simple proof-of-concept moderation logic for Atomic Dota.

This is a lightweight demonstration module intended for portfolio use.
It scores input text against a small risk vocabulary and returns an action.
"""

from __future__ import annotations

from dataclasses import dataclass


HIGH_RISK_TERMS = {"kill", "hate", "abuse", "threat", "self-harm"}
MEDIUM_RISK_TERMS = {"stupid", "idiot", "loser", "ugly"}


@dataclass
class ModerationResult:
    score: int
    label: str
    action: str



def moderate_text(text: str) -> ModerationResult:
    lowered = text.lower()
    score = 0

    for term in HIGH_RISK_TERMS:
        if term in lowered:
            score += 3

    for term in MEDIUM_RISK_TERMS:
        if term in lowered:
            score += 1

    if score >= 4:
        return ModerationResult(score=score, label="high-risk", action="block_and_review")
    if score >= 1:
        return ModerationResult(score=score, label="warning", action="allow_with_flag")
    return ModerationResult(score=score, label="clean", action="allow")


if __name__ == "__main__":
    sample = "I hate you and this is a threat"
    result = moderate_text(sample)
    print(result)
