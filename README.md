# GitHub Automation Python Tools

Complete suite of Python applications for automating GitHub operations.

## Overview

4 independent applications:

| Tool | Purpose |
|------|---------|
| **github_pusher.py** | Automated push |
| **github_manager.py** | Interactive menu |
| **docs_pusher.py** | Build LaTeX & push |
| **github_monitor.py** | Status monitoring |

## Quick Start

```bash
python setup.py
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
python github_monitor.py
```

## Requirements

- Python 3.7+
- Git 2.x+
- GitHub personal access token

## Getting Token

1. https://github.com/settings/tokens
2. Generate new token (classic)
3. Select "repo" scope
4. Copy token

## Applications

### github_pusher.py
Automated GitHub push with single command.

```bash
python github_pusher.py
```

Features:
- Auto file staging
- Pattern matching
- Custom messages

### github_manager.py
Interactive menu-driven management.

```bash
python github_manager.py
```

Features:
- 11 menu options
- Real-time status
- Branch management

### docs_pusher.py
Build LaTeX to PDF and push.

```bash
python docs_pusher.py
```

Requires: pdflatex
- Ubuntu: `sudo apt-get install texlive-latex-base`
- macOS: `brew install --cask mactex`

### github_monitor.py
Repository status monitoring.

```bash
python github_monitor.py
```

Features:
- Status summary
- Commit history
- JSON/text export

## Configuration

Edit .env file (created by setup.py):

```env
GITHUB_USERNAME=your_username
GITHUB_TOKEN=your_token
GITHUB_REPO=your_repo
LOCAL_REPO_PATH=./repo_path
COMMIT_MESSAGE=Update
```

## Security

- ❌ Never commit .env
- ✅ Included in .gitignore
- ✅ Token rotation quarterly

## Troubleshooting

**Module not found**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Missing .env**
```bash
python setup.py
```

**pdflatex not found**
Install TeX Live or MiKTeX

## Support

See README.md for detailed guides
