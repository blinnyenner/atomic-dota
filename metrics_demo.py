"""Small helper script for simple engagement metrics."""

from __future__ import annotations


def engagement_rate(likes: int, comments: int, shares: int, impressions: int) -> float:
    if impressions <= 0:
        return 0.0
    return round(((likes + comments + shares) / impressions) * 100, 2)


if __name__ == "__main__":
    print("Sample engagement rate:", engagement_rate(120, 45, 10, 5000), "%")
