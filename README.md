# Portfolio

## What this is

A static-content portfolio site built with Flask. LinkedIn-style layout with
four pages: Home, Experience, Projects, and Contact. Server-side rendering
only; all content lives in one Python file.

## Edit your content

All editable content is in `content.py` — nothing else needs changing:

- `PROFILE`: `name`, `headline`, `location`, `about`, `email`,
  `linkedin_url`, `github_url`, and the three page intros
  (`experience_intro`, `projects_intro`, `contact_intro`).
- `EXPERIENCE`, `EDUCATION`, `SKILLS`, `PROJECTS`: lists of dicts/strings.

Rules:

- `email` is a bare address (`you@example.com`). Do not add a `mailto:`
  prefix; templates add it themselves.
- Any value still starting with `TODO` is not real content: URLs and email
  addresses starting with `TODO` are hidden (no link is rendered), the
  Contact page hides a `TODO` location (`show_location`), and other
  text is shown literally as a placeholder until you replace it.
- An empty list (`EXPERIENCE = []`) renders an empty-state message rather
  than breaking the page.

## Add your images and CV

Place files at exactly these paths:

- `static/img/avatar.jpg` — your photo
- `static/img/banner.jpg` — wide banner behind the profile header
- `static/files/cv.pdf` — linked by the "Download CV" button

The site works without them: a missing avatar falls back to your initials,
a missing banner falls back to a gradient, and a missing CV hides the CV
button. No code changes are needed either way.

## Run locally

On Debian/Ubuntu, install the `python3-venv` package first.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/flask --app app run --debug
```

Open `http://127.0.0.1:5000`.

## Deploy to a Freestyle VM

1. Create a Freestyle VM (https://freestyle.sh) with
   `idleTimeoutSeconds: -1` (-1 removes the idle timeout that would otherwise
   pause the VM), and an outbound allow rule so `pip` can reach PyPI.
2. SSH into the VM. You are the default `ubuntu` user with passwordless
   sudo, and every privileged step below is prefixed with `sudo` for that
   reason.
3. Install dependencies: `sudo apt update && sudo apt install -y python3-venv git`.
4. Create the dedicated system user: `sudo useradd -r -M -d /srv/portfolio -s /usr/sbin/nologin portfolio`.
5. Create the directory itself and copy the repo into it:
   `sudo install -d -o portfolio -g portfolio /srv/portfolio`, then
   `sudo runuser -u portfolio -- git clone <your-repo-url> /srv/portfolio`
   (replace `<your-repo-url>` with your repo URL; `/srv/portfolio` is now an
   empty directory — cloning into an existing empty directory is supported
   by git). If the repo is not in git, `rsync` instead as `portfolio` too:
   `sudo runuser -u portfolio -- rsync …` (same reason: `/srv/portfolio` is
   owned by `portfolio`, so `ubuntu` cannot write there directly), or run
   `sudo chown -R portfolio:portfolio /srv/portfolio` afterwards, and
   exclude `.venv` and `__pycache__` (a copied dev `.venv` has absolute
   shebangs pointing at the dev machine).
6. Create the venv and install as `portfolio` (via `runuser`, since
   step 4 passes `-s /usr/sbin/nologin` and the account cannot log in
   directly; `runuser -u portfolio -- <command>` still works because it
   execs the command directly without invoking a shell):
   `sudo runuser -u portfolio -- /usr/bin/python3 -m venv /srv/portfolio/.venv`
   then
   `sudo runuser -u portfolio -- /srv/portfolio/.venv/bin/pip install -r /srv/portfolio/requirements.txt`.
   Intended ownership: code and venv are owned by `portfolio`.
   Verify with `ls -ld /srv/portfolio /srv/portfolio/.venv`.
7. Copy `/srv/portfolio/deploy/portfolio.service` to `/etc/systemd/system/portfolio.service`:
   `sudo cp /srv/portfolio/deploy/portfolio.service /etc/systemd/system/portfolio.service`.
8. Reload and start: `sudo systemctl daemon-reload` then
   `sudo systemctl enable --now portfolio`.
9. Check `sudo systemctl status portfolio` and `curl 127.0.0.1:8000`.
10. Expose it publicly with a Freestyle TLS/port rule: add a TLS rule for
    `<name>.style.dev` (or your custom domain) that forwards to the VM's
    port 8000. The service listens on `0.0.0.0:8000` because the TLS rule
    terminates outside the guest and reaches the VM from outside; do not add
    a public inbound firewall rule for 8000 — only the TLS rule needs it,
    keeping exposure limited.

## Updating the site

Pull (or re-copy) the latest code into `/srv/portfolio` — e.g.
`sudo runuser -u portfolio -- git -C /srv/portfolio pull` — then:

```sh
sudo runuser -u portfolio -- /srv/portfolio/.venv/bin/pip install -r /srv/portfolio/requirements.txt  # when requirements.txt changed
sudo cp /srv/portfolio/deploy/portfolio.service /etc/systemd/system/portfolio.service  # when the unit changed — copy first, then reload below
sudo systemctl daemon-reload  # after copying the updated unit
sudo systemctl restart portfolio
```

If it fails, check `journalctl -u portfolio -n 50 --no-pager` and
`curl -sS 127.0.0.1:8000/ -o /dev/null -w '%{http_code}'`.

## Project layout

```text
app.py                  Flask app: routes, template filters, shared context
content.py              All editable site content (single source of truth)
requirements.txt        Flask + gunicorn version ranges
deploy/portfolio.service  systemd unit for the VM
templates/base.html     Shared layout, nav, footer
templates/index.html    Home page
templates/experience.html  Work history, education, skills
templates/projects.html    Project grid
templates/contact.html  Contact details
static/css/style.css    All styles (no frameworks)
```

## Notes

No database. No JavaScript. No tracking, no cookies. Server-side rendering
only; gunicorn serves the Flask app and Freestyle's TLS rule terminates
TLS at the edge (no proxy is run on the VM).

No favicon is shipped, so `/favicon.ico` returns 404; add
`static/favicon.ico` later if wanted.
