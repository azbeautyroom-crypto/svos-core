# SVOS Compiler Contract

## Input authority

`inputs/sessionvue/` is hand-authored canonical company input.

## Generated authority

`generated/sessionvue-os/` is disposable compiler output. Never edit it manually.

## Compile sequence

1. Load `compiler/contracts/sessionvue.compile.json`.
2. Validate required input directories.
3. Remove the prior generated output when configured.
4. Copy canonical Company Brain, Projects, and Jobs.
5. Compile each `inputs/sessionvue/systems/*.system.json` definition.
6. Generate Business System files, Jobs, Metrics, Automations, and registries.
7. Generate build metadata and validation reports.
8. Fail the release gate when required sources are absent.

## Correction rule

When generated output is wrong, update the source input, template, or compiler and compile again.
