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

These commands assume the five destination names do not already exist. Restart Codex if necessary, then explicitly invoke a skill, for example `$grant-proposal`. Keep this checkout in place: the links point to its evaluated skill files, whose relative references must remain accessible.

This follows the [documented Codex skill discovery locations](https://learn.chatgpt.com/docs/build-skills). The controlled Sol evaluation used Codex; this installation path has been structurally checked but has not yet had a native end-to-end acceptance run.

## Platform testing

All five skills were explicitly invoked in Claude Desktop/Cowork on Sonnet 5 Medium and in ChatGPT Work on the web on GPT-6 Astra Medium. These were compatibility checks on fictional cases, separate from the published evaluation; they do not establish that every output passed its quality criteria.

This repository contains one canonical set of skills and shared references. Standalone ChatGPT Work upload packages are not distributed here.

Models can make mistakes. Review facts, calculations, permissions, and sensitive information before sharing outputs.
