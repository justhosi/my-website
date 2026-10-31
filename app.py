"""Flask application: routes and shared template context."""

import os

from flask import Flask, render_template

from content import PROFILE

app = Flask(__name__)

# (label, endpoint) pairs used by base.html to render the nav.
NAV_ITEMS = [
    ("Home", "home"),
    ("Experience", "experience"),
    ("Projects", "projects"),
    ("Contact", "contact"),
]


def _initials(name):
    """Return initials (first + last word) for the brand mark."""
    parts = (name or "").split()
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0][:1].upper()
    return (parts[0][:1] + parts[-1][:1]).upper()


def _asset_exists(relative_path):
    """True if a file exists under the static folder; never raises."""
    try:
        if not relative_path:
            return False
        return os.path.exists(os.path.join(app.static_folder, relative_path))
    except (TypeError, ValueError):
        return False


@app.context_processor
def inject_globals():
    """Share profile, nav, and asset flags with every template."""
    return {
        "profile": PROFILE,
        "nav_items": NAV_ITEMS,
        "initials": _initials(PROFILE.get("name", "")),
        "has_avatar": _asset_exists(PROFILE.get("avatar")),
        "has_banner": _asset_exists(PROFILE.get("banner")),
        "has_cv": _asset_exists(PROFILE.get("cv")),
    }


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/experience")
def experience():
    return render_template("experience.html")


@app.get("/projects")
def projects():
    return render_template("projects.html")


@app.get("/contact")
def contact():
    return render_template("contact.html")
