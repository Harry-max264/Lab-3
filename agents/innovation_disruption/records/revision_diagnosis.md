# Observed weakness and revision

The initial ChatGPT/Codex response in `responses/primary_v0.1.json` was generated in this session after reading `work/v0_primary_prompt.txt`. It correctly separated the undeployed proposal from the general technology and gave Low business-model exposure. It was not a fabricated failure or a separate API execution.

The useful weakness was incomplete decision support: the disruption explanation did not systematically map channels, costs and defensive capabilities; the trigger only said to wait for pilot results, without identifying what result would change the classification. The v0 instructions also had no operational severity rubric and no explicit insufficient-information gate, risking inconsistent labels in the agency and ambiguous cases.

Revision v1.0 adds an implementation gate, named baselines, severity conditions, a create/displace/retain map, a strongest counter-case with discriminating evidence, decision-linked monitoring, and an explicit abstention rule. It preserves the frozen output contract. The same primary input is retained for the re-run; the contrast inputs were not changed to manufacture a pass.

This is a single-session development demonstration. The same model constructed, answered and reviewed the cases; it is not independent validation or evidence of repeat-run reliability.
