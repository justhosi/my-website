# Site content in one place.
#
# HOW TO EDIT:
#   - PROFILE holds the owner's identity, bio, and contact links.
#   - "experience_intro", "projects_intro", and "contact_intro" are the
#     one-or-two-sentence intros shown at the top of those pages.
#   - "email" is a bare address (you@example.com, no "mailto:" prefix).
#   - EXPERIENCE / EDUCATION are lists shown in order; add or remove dicts.
#   - SKILLS is a plain list of short skill names.
#   - PROJECTS holds portfolio entries; leave "demo_url" as "" if none.
#   - "avatar", "banner", and "cv" are paths relative to the static/ folder.
#     If the files are missing, templates hide them gracefully (no crash).
#   - Empty strings ("") are hidden by the templates: use "" rather than a
#     fake URL when a company has no site or a project has no demo.

PROFILE = {
    "name": "Hossein Mohammadzadehmazinan",
    "headline": "Medical Interpreter (English ↔ Farsi) · VRI & OPI Specialist",
    "location": "Mersin, Türkiye",
    "about": (
        "I'm a Farsi–English medical interpreter with C2-level English, two years of "
        "professional video and over-the-phone interpreting, and fifteen years inside "
        "Iran's healthcare and medical-device market as a sales leader and board member. "
        "I've delivered more than 7,000 minutes of live clinical interpretation at GLOBO "
        "with no reported communication-related incidents.\n\n"
        "Native Farsi, practised in HIPAA-compliant handling of patient information, and "
        "equally at home in board meetings and exam rooms. I also build small tools — "
        "Python, Flask, some Rust — mostly the kind of thing that removes a repetitive "
        "task from an interpreter's day."
    ),
    "email": "mohamadzadeh@outlook.com",
    "experience_intro": (
        "Two years of clinical interpretation on top of fifteen years in healthcare sales "
        "and medical devices — the same conversations, seen from both sides."
    ),
    "projects_intro": (
        "Things I build when I'm not interpreting — mostly small tools that solve one "
        "specific, real annoyance."
    ),
    "contact_intro": (
        "Open to medical interpretation work — VRI, OPI and clinical accounts — and glad "
        "to talk about technical or localisation projects."
    ),
    "linkedin_url": "https://www.linkedin.com/in/hossein-mohammadzadehmazinan-483a6311a/",
    "github_url": "https://github.com/justhosi",
    "avatar": "img/avatar.jpg",
    "banner": "img/banner.jpg",
    "cv": "files/cv.pdf",
}

EXPERIENCE = [
    {
        "title": "Medical Interpreter",
        "company": "GLOBO",
        "company_url": "https://globohq.com/",
        "location": "Remote · United States healthcare clients",
        "start": "Jul 2025",
        "end": "Present",
        "bullets": [
            "Interpret real-time Farsi–English medical dialogue in high-stakes clinical "
            "encounters — 7,000+ minutes delivered so far.",
            "Hold a zero-incident accuracy record across specialty consults, intake and "
            "discharge instructions.",
            "Cover telehealth and video remote interpreting sessions for US patients with "
            "limited English proficiency.",
        ],
    },
    {
        "title": "Interpreter",
        "company": "Future Group Translation Services",
        "company_url": "",
        "location": "Remote · Egypt / MENA",
        "start": "Apr 2023",
        "end": "Jul 2025",
        "bullets": [
            "Delivered consecutive and simultaneous VRI and over-the-phone interpreting for "
            "healthcare, business and technical clients for more than two years.",
            "Mediated clinician–patient conversations in sensitive contexts, preserving both "
            "clarity and empathy.",
            "Earned repeat business on multilingual projects, known for precision under pressure.",
        ],
    },
    {
        "title": "Board Member",
        "company": "Akam Teb Tejarat",
        "company_url": "",
        "location": "",
        "start": "Apr 2019",
        "end": "Jul 2024",
        "bullets": [
            "Set strategic direction for a medical-solutions company over five years, "
            "aligning departments and healthcare partnerships.",
            "Served concurrently as Regional Sales Manager, using bilingual negotiation to "
            "secure cross-border medical-equipment partnerships.",
        ],
    },
    {
        "title": "Sales Manager",
        "company": "Pars Eltiam Kala",
        "company_url": "",
        "location": "",
        "start": "Feb 2013",
        "end": "Jul 2022",
        "bullets": [
            "Led a B2B and retail sales organisation serving hospitals, medical centres and "
            "a nationwide retailer network.",
            "Grew revenue 300%, sustained across a nine-year tenure.",
        ],
    },
    {
        "title": "Regional Sales Manager",
        "company": "Sazgan Gostar Co.",
        "company_url": "",
        "location": "",
        "start": "Nov 2011",
        "end": "Nov 2013",
        "bullets": [
            "Owned product and sales strategy for the blood-pump (haematology device) division.",
            "Raised market share 25% within a single focused year.",
        ],
    },
    {
        "title": "Author (part-time)",
        "company": "winphone.ir",
        "company_url": "",
        "location": "",
        "start": "May 2016",
        "end": "Apr 2019",
        "bullets": [
            "Published 1,000+ Persian-language articles on mobile technology, deepening my "
            "technical vocabulary and translation skill.",
        ],
    },
    {
        "title": "Salesman",
        "company": "Pars Eltiam Kala Co.",
        "company_url": "",
        "location": "",
        "start": "Mar 2007",
        "end": "Dec 2009",
        "bullets": [
            "Built foundational medical and industrial sales experience managing client "
            "relationships and closing deals.",
            "Promoted to Regional Sales Manager within two years.",
        ],
    },
]

EDUCATION = [
    {
        "school": "Nooretouba Virtual Institute of Higher Education",
        "degree": "B.A., Finance & Financial Management Services",
        "start": "2013",
        "end": "2018",
    },
    {
        "school": "Islamic Azad University",
        "degree": "B.A., Natural Resources Engineering",
        "start": "2006",
        "end": "2010",
    },
]

SKILLS = [
    "Medical interpretation",
    "VRI & OPI",
    "Consecutive & simultaneous",
    "HIPAA compliance",
    "Medical terminology",
    "PHI handling",
    "Telehealth interpreting",
    "Farsi (native)",
    "English (C2)",
    "B2B sales",
    "Key account management",
    "Team leadership",
    "Negotiation",
    "Python & Flask",
    "GitHub",
    "CAT tools",
]

PROJECTS = [
    {
        "name": "globo-mcp",
        "description": (
            "An unofficial MCP server for the GLOBO interpreter portal. Sign in with your "
            "own account and an AI assistant can read your call statistics, schedule, "
            "assignments, payouts and the interpreter knowledge base — no scraping."
        ),
        "tags": ["TypeScript", "MCP", "Node"],
        "github_url": "https://github.com/justhosi/globo-mcp",
        "demo_url": "",
    },
    {
        "name": "furus",
        "description": (
            "A from-scratch, still-in-progress reimplementation of Rufus in Rust for "
            "Linux: native FAT32 and exFAT formatting, MBR/GPT writers and an ISO9660 "
            "reader, with the end-to-end USB write path still to come. No Windows binaries."
        ),
        "tags": ["Rust", "Linux", "Filesystems"],
        "github_url": "https://github.com/justhosi/furus",
        "demo_url": "",
    },
    {
        "name": "v2ray-plugin",
        "description": (
            "An Omarchy bar plugin for v2ray/xray. Paste a vless, vmess, trojan or ss share "
            "link, click the shield, and a tunnel comes up — proxying only the apps you "
            "point at it, with no root and no password prompt."
        ),
        "tags": ["Shell", "Omarchy", "Networking"],
        "github_url": "https://github.com/justhosi/v2ray-plugin",
        "demo_url": "",
    },
    {
        "name": "Video download bot",
        "description": (
            "A small Telegram bot that takes a YouTube, Instagram or TikTok link and sends "
            "the video straight back into the chat. Built with python-telegram-bot and yt-dlp."
        ),
        "tags": ["Python", "Telegram", "yt-dlp"],
        "github_url": "https://github.com/justhosi/suckless_video_downloader_bot",
        "demo_url": "",
    },
    {
        "name": "ToDoList",
        "description": (
            "A one-window desktop to-do list in Python and Tkinter. Nothing to install "
            "beyond the standard library, and the list survives a restart through a plain "
            "JSON file."
        ),
        "tags": ["Python", "Tkinter", "Desktop"],
        "github_url": "https://github.com/justhosi/ToDoList",
        "demo_url": "",
    },
    {
        "name": "flaskblog",
        "description": (
            "A small Flask blog engine, written to teach myself server-side rendering and "
            "the request/response cycle."
        ),
        "tags": ["Python", "Flask", "Web"],
        "github_url": "https://github.com/justhosi/flaskblog",
        "demo_url": "https://resumeblog.onrender.com",
    },
]
