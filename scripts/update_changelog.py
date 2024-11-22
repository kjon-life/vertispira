#!/usr/bin/env python3
# update_changelog.py

import sys
import re
from datetime import datetime
from typing import List, Dict

def parse_pull_requests(since_tag: str) -> List[Dict]:
    """
    Parse merged PRs since the last release.
    Implement using GitHub API client here.
    """
    # TODO: Implement using GitHub API
    return []

def categorize_changes(prs: List[Dict]) -> Dict[str, List[str]]:
    """Categorize changes based on PR labels"""
    categories = {
        "Added": [],
        "Changed": [],
        "Fixed": [],
        "Security": [],
        "Performance": [],
        "Documentation": [],
    }
    
    for pr in prs:
        # Logic to categorize based on labels
        pass
    
    return categories

def update_changelog(version: str, changes: Dict[str, List[str]]) -> str:
    today = datetime.now().strftime("%Y-%M-%d")
    entry = f"\n## [{version}] - {today}\n"
    
    for category, items in changes.items():
        if items:
            entry += f"\n### {category}\n"
            for item in items:
                entry += f"- {item}\n"
    
    return entry

def insert_changelog_entry(content: str, new_entry: str) -> str:
    """Insert new entry after Unreleased section"""
    unreleased_pattern = r"## \[Unreleased\].*?\n(?=## \[|\Z)"
    return re.sub(unreleased_pattern, f"## [Unreleased]\n\n{new_entry}\n", 
                 content, flags=re.DOTALL)

def update_version_links(content: str, version: str, repo_url: str) -> str:
    """Update version comparison links"""
    links_section = "\n## Version Links\n"
    links_section += f"[Unreleased]: {repo_url}/compare/v{version}...HEAD\n"
    links_section += f"[{version}]: {repo_url}/releases/tag/v{version}\n"
    
    if "## Version Links" in content:
        return re.sub(r"## Version Links.*", links_section, content, 
                     flags=re.DOTALL)
    return content + links_section

def main(version: str, repo_url: str):
    # Read current CHANGELOG.md
    with open("CHANGELOG.md", "r") as f:
        content = f.read()
    
    # Get PRs since last release
    prs = parse_pull_requests(f"v{version}")
    
    # Categorize changes
    changes = categorize_changes(prs)
    
    # Create new entry
    new_entry = update_changelog(version, changes)
    
    # Update content
    content = insert_changelog_entry(content, new_entry)
    content = update_version_links(content, version, repo_url)
    
    # Write updated CHANGELOG.md
    with open("CHANGELOG.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: update_changelog.py VERSION REPO_URL")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])