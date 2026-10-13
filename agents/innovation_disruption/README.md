# Innovation and Disruption Agent

Read [records/agent_record.md](records/agent_record.md) for the complete record, [specialist_instructions.md](specialist_instructions.md) for classification criteria, and [records/test_record.md](records/test_record.md) for results. Inputs are in `cases/`, saved model JSON outputs in `responses/`, and generated packets in root `work/`.

This uses the course interactive ChatGPT runtime, not a Python-based LLM or an API service. From the repository root:

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/innovation_disruption --case agents/innovation_disruption/cases/primary.json
```

Paste the generated packet into ChatGPT and save the JSON response, then run:

```bash
python tools/validate_response.py agents/innovation_disruption/responses/primary_response.json
```

Repeat for `contrast_1` and `contrast_2`. Do not alter frozen schemas or tools. New runs may differ; preserve new responses and review the reasoning. The saved outputs are demonstrations, not guaranteed results of rerunning a model.
