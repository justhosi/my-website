"""Flask application: routes and shared template context."""

import os
import re

from flask import Flask, render_template

from content import EDUCATION, EXPERIENCE, PROFILE, PROJECTS, SKILLS

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


@app.template_filter("public_url")
def public_url(value):
    """Return "" for missing or TODO placeholder values, else the value.

    Templates use this to decide whether a URL (or contact value) is real
    before rendering it as a link, so placeholder copy never becomes a link.
    """
    if value is None:
        return ""
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped or stripped.lower().startswith("todo"):
            return ""
        lowered = stripped.lower()
        if not (
            lowered.startswith("http://")
            or lowered.startswith("https://")
            or lowered.startswith("mailto:")
        ):
            return ""
        return value
    return value


@app.template_filter("public_email")
def public_email(value):
    """Return the bare address (no mailto:) or "" if missing/placeholder/invalid.

    Templates prefix ``mailto:`` themselves, so returning the bare address
    keeps exactly one ``mailto:`` in the rendered ``href``.
    """
    if not isinstance(value, str):
        return ""
    stripped = value.strip()
    if not stripped or stripped.lower().startswith("todo"):
        return ""
    bare = stripped
    if bare.lower().startswith("mailto:"):
        bare = bare[len("mailto:"):].strip()
    if "<" in bare or ">" in bare:
        return ""
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", bare):
        return ""
    return bare


@app.template_filter("pretty_url")
def pretty_url(value):
    """Return host/path display text for an http(s) URL, else ""."""
    if not isinstance(value, str):
        return ""
    stripped = value.strip()
    lowered = stripped.lower()
    if not (lowered.startswith("http://") or lowered.startswith("https://")):
        return ""
    rest = stripped.split("://", 1)[1]
    rest = rest.split("?", 1)[0].split("#", 1)[0]
    if rest.lower().startswith("www."):
        rest = rest[len("www."):]
    return rest.rstrip("/")


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
    return render_template(
        "index.html", EXPERIENCE=EXPERIENCE, PROJECTS=PROJECTS, SKILLS=SKILLS
    )


@app.get("/experience")
def experience():
    return render_template(
        "experience.html", EXPERIENCE=EXPERIENCE, EDUCATION=EDUCATION, SKILLS=SKILLS
    )


@app.get("/projects")
def projects():
    return render_template("projects.html", PROJECTS=PROJECTS)


@app.get("/contact")
def contact():
    return render_template("contact.html")
