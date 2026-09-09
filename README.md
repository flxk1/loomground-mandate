<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-mandate

**Did this run serve the purpose it was given?**

Compares an observed trajectory with its declared mandate.

## Install

```
pip install loomground-mandate
```

## Usage

```python
from loomground_mandate import Mandate, TrajectoryStep, detect, fold_divergences
mandate = Mandate(EvidenceRef("engagement-letter", 120, 180), frozenset({"review"}))
steps = [TrajectoryStep("step-1", EvidenceRef("log", 0, 10), serves=frozenset({"review"}))]
fold_divergences(detect(mandate, steps, evidence=provider)).overall
```

## Interface

- inputs: `Mandate(evidence: EvidenceRef, purposes)` · `TrajectoryStep(ref, evidence, serves, defeats)` · `evidence: EvidenceProvider`
- output: `Divergence(kind, ref, why)`; `KINDS`: `ungrounded` · `defeats-purpose` · `out-of-mandate` · `unserved`
- `fold_divergences(divergences) → IssueAggregate`
- from solver: `cross_subsumption.Verdict` · `interop.EvidenceRef` · `ports.EvidenceProvider`

## Family

Diagnostic operator; consumes `loomground-solver` 0.5; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-mandate`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.1.0 · 22 tests · Python >=3.10 · solver 0.5

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`
