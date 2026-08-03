# Auctra Novel Skills

A public, project-owned skill collection for Auctra and Chinese long-form novel production.

This repository keeps Auctra runtime guidance, novel-writing workflows, character modeling, and Auctra-specific visual handoff skills separate from the general Yeisme agent skill collection.

## Modules

- `auctra-runtime/`: Auctra CLI/runtime, project bootstrap, workspace routing, market research, review orchestration, optimization, and screenplay-pattern research.
- `novel-writing/`: Chinese novel briefing, outlining, scene cards, chapter writing, review, continuity, revision, reader retention, and serial operations.
- `character-modeling/`: Character cognition, motivation, identity, relationships, embodiment, social knowledge, group organization, and dramatic stress modeling.
- `auctra-visual/`: Auctra-specific Eikona visual routing and handoff guidance.

Every skill follows the standard shape:

```text
<module>/<skill-name>/
  SKILL.md
  agents/openai.yaml
```

## Installation as a Yeisme source module

The main `yeisme-agent` workspace mounts this repository as a source module under `.skills/yeisme/auctra-novel/`. The existing profile names remain stable, so generated `.agents/skills` and `.claude/skills` consumers do not need to rename their skill references.

For a standalone checkout, read the relevant `SKILL.md` directly or integrate the repository as a project-owned source module in a skills profile.

## Scope boundary

This repository does not contain the Auctra CLI implementation, novel manuscripts, project canon, or runtime state. Those live in their owning repositories:

- Auctra CLI: `https://github.com/yeisme/auctra`
- Novel project: `https://github.com/yeisme/chichao-beian`

## License

The skills are released under the MIT License. See [LICENSE](LICENSE).
