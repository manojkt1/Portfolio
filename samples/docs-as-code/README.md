# Docs-as-Code Quality Pipeline

This sample demonstrates a documentation workflow with Markdown source in Git, pull-request review, internal-link validation, a strict MkDocs build, and publishing only after checks and review pass.

## Local commands

```bash
python -m pip install -r requirements.txt
python scripts/check_internal_links.py docs
mkdocs build --strict
```

## Review roles

- **Author:** writes and self-tests the change.
- **Technical reviewer:** verifies product behavior, commands, values, and examples.
- **Editorial reviewer:** checks clarity, structure, terminology, and accessibility.
- **Release owner:** confirms that documentation is ready with the product change.

The workflow intentionally does not use an LLM as an accuracy authority. AI-assisted edits require the same technical and editorial checks as human-authored changes.
