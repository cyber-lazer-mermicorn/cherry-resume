"""Tests for Cherry Master Resume — validates content, structure, and job tracker."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_readme_exists():
    readme = ROOT / "README.md"
    assert readme.exists(), "README.md missing"
    content = readme.read_text()
    assert len(content) > 50, "README.md too short"
    print("PASS: test_readme_exists")


def test_readme_has_required_sections():
    readme = ROOT / "README.md"
    content = readme.read_text()
    for section in ["What this project does", "Who it is for", "What exists today"]:
        assert section in content, f"Missing section: {section}"
    print("PASS: test_readme_has_required_sections")


def test_resume_exists():
    resume = ROOT / "RESUME.md"
    assert resume.exists(), "RESUME.md missing"
    content = resume.read_text()
    assert len(content) > 500, "RESUME.md too short"
    print("PASS: test_resume_exists")


def test_resume_has_name():
    resume = ROOT / "RESUME.md"
    content = resume.read_text()
    assert "Cherry" in content, "Missing name in resume"
    print("PASS: test_resume_has_name")


def test_resume_has_skills():
    resume = ROOT / "RESUME.md"
    content = resume.read_text()
    for skill in ["Python", "AI", "API"]:
        assert skill in content, f"Missing skill: {skill}"
    print("PASS: test_resume_has_skills")


def test_resume_has_projects():
    resume = ROOT / "RESUME.md"
    content = resume.read_text()
    assert "Mermicorn" in content, "Missing main project"
    print("PASS: test_resume_has_projects")


def test_resume_has_contact():
    resume = ROOT / "RESUME.md"
    content = resume.read_text()
    assert "@" in content or "email" in content.lower(), "Missing contact info"
    print("PASS: test_resume_has_contact")


def test_job_tracker_exists():
    tracker = ROOT / "JOB-APPLICATION-TRACKER.md"
    assert tracker.exists(), "JOB-APPLICATION-TRACKER.md missing"
    content = tracker.read_text()
    assert len(content) > 100, "Job tracker too short"
    print("PASS: test_job_tracker_exists")


def test_job_tracker_has_entries():
    tracker = ROOT / "JOB-APPLICATION-TRACKER.md"
    content = tracker.read_text()
    assert "Vercel" in content, "Missing job entry"
    assert "Applied" in content, "Missing status"
    print("PASS: test_job_tracker_has_entries")


def test_job_tracker_has_target_companies():
    tracker = ROOT / "JOB-APPLICATION-TRACKER.md"
    content = tracker.read_text()
    assert "Target Companies" in content, "Missing target companies section"
    print("PASS: test_job_tracker_has_target_companies")


def test_linkedin_exists():
    linkedin = ROOT / "LINKEDIN.md"
    assert linkedin.exists(), "LINKEDIN.md missing"
    content = linkedin.read_text()
    assert len(content) > 50, "LinkedIn doc too short"
    print("PASS: test_linkedin_exists")


def test_cover_letter_template_exists():
    template = ROOT / "COVER-LETTER-TEMPLATE.md"
    assert template.exists(), "COVER-LETTER-TEMPLATE.md missing"
    content = template.read_text()
    assert len(content) > 100, "Cover letter template too short"
    print("PASS: test_cover_letter_template_exists")


def test_powerflex_profile_exists():
    profile = ROOT / "POWERFLEX-PROFILE.md"
    assert profile.exists(), "POWERFLEX-PROFILE.md missing"
    print("PASS: test_powerflex_profile_exists")


def test_no_secrets_in_files():
    secret_patterns = [
        r"ghp_[A-Za-z0-9]{36}",
        r"github_pat_[A-Za-z0-9_]{82}",
        r"sk-[A-Za-z0-9]{48}",
        r"API_KEY\s*=\s*['\"][^'\"]+['\"]",
    ]
    for md_file in ROOT.glob("*.md"):
        content = md_file.read_text()
        for pattern in secret_patterns:
            assert not re.search(pattern, content), f"Secret found in {md_file.name}"
    print("PASS: test_no_secrets_in_files")


def test_robots_and_robots():
    """Test that LICENSE and RIGHTS exist."""
    assert (ROOT / "LICENSE").exists(), "LICENSE missing"
    assert (ROOT / "RIGHTS.md").exists(), "RIGHTS.md missing"
    print("PASS: test_robots_and_robots")


def run_all():
    tests = [
        test_readme_exists,
        test_readme_has_required_sections,
        test_resume_exists,
        test_resume_has_name,
        test_resume_has_skills,
        test_resume_has_projects,
        test_resume_has_contact,
        test_job_tracker_exists,
        test_job_tracker_has_entries,
        test_job_tracker_has_target_companies,
        test_linkedin_exists,
        test_cover_letter_template_exists,
        test_powerflex_profile_exists,
        test_no_secrets_in_files,
        test_robots_and_robots,
    ]
    passed = failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"FAIL: {test.__name__}: {e}")
            failed += 1
    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    return failed == 0


if __name__ == "__main__":
    import sys
    sys.exit(0 if run_all() else 1)
