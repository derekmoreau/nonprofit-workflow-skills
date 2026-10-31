# Install the skills

## Claude Code

From the repository root:

```sh
claude --plugin-dir ./plugin
```

## Codex

For repository-scoped use, preserve both the skills and shared references. From this repository root on macOS or Linux:

```sh
mkdir -p .agents/skills
for skill in plugin/skills/*; do
  ln -s "../../$skill" ".agents/skills/$(basename "$skill")"
done
```

These commands assume the five destination names do not already exist. Restart Codex if necessary, then explicitly invoke a skill, for example `$grant-proposal`. Keep this checkout in place: the links point to its skill files, whose relative references must remain accessible.

This follows the [documented Codex skill discovery locations](https://learn.chatgpt.com/docs/build-skills). The controlled Sol evaluations used Codex. This installation path has had structural checks, but no native end-to-end acceptance run for the current instructions.

## Version and platform testing

V2 preserves the public version’s checks and adds selected later fixes. This prepared update has not had model evaluation or native Claude validation. The five workflows and installation paths remain unchanged. See [what changed in V2](../README.md#what-changed-in-v2).

The following checks used the September version. They have not been repeated for the current instructions.

All five skills were explicitly invoked in Claude Desktop/Cowork on Sonnet 5 Medium and in ChatGPT Work on the web on GPT-6 Astra Medium. These were compatibility checks on fictional cases, separate from the published evaluation; they do not establish that every output passed its quality criteria.

This repository contains one canonical set of skills and shared references. Standalone ChatGPT Work upload packages are not distributed here.

Models can make mistakes. Review facts, calculations, permissions, and sensitive information before sharing outputs.
