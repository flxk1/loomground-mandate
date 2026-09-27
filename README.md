<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-mandate

**Did this run serve the purpose it was given?**

Compares an observed trajectory with its declared mandate.

## Problem

A run finishes; nobody checks it did what it was told. Compares the trajectory to the mandate and names each divergence.

## Install

```
pip install git+https://github.com/flxk1/loomground-mandate
```

## Usage

```python
from loomground_mandate import Mandate, TrajectoryStep, detect, fold_divergences
mandate = Mandate(EvidenceRef("engagement-letter", span_start=120, span_end=180), frozenset({"review"}))
steps = [TrajectoryStep("step-1", EvidenceRef("log", span_start=0, span_end=10), serves=frozenset({"review"})),
         TrajectoryStep("step-2", EvidenceRef("log", span_start=10, span_end=20), serves=frozenset({"billing"}))]
divs = detect(mandate, steps, evidence=provider)
divs, fold_divergences(divs).overall
```

## Example

```
in : the Usage snippet; provider verifies engagement-letter and log
out: Divergence(kind='out-of-mandate', ref='step-2', why='serves no purpose the mandate declares')
     Verdict.NOT_SATISFIED
```

## Interface

- inputs: `Mandate(evidence: EvidenceRef, purposes)` · `TrajectoryStep(ref, evidence, serves, defeats)` · `evidence: EvidenceProvider`
- output: `Divergence(kind, ref, why)`; `KINDS`: `ungrounded` · `defeats-purpose` · `out-of-mandate` · `unserved`
- `fold_divergences(divergences) → IssueAggregate`
- from solver: `cross_subsumption.Verdict` · `interop.EvidenceRef` · `ports.EvidenceProvider`

## Family

Diagnostic operator; consumes `loomground-solver` 0.6.0; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-mandate`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.2.0 · 22 tests · Python >=3.10 · solver 0.6.0

## How this is made

The code and documentation are written with Loomground agents running on Claude (Anthropic). The maintainer reads and corrects all of it.

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`
