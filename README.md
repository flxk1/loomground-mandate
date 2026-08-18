<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-mandate

**Did this run serve the purpose it was given?**

A mandate, a trajectory, and the comparison between them. Both terms grounded in evidence through the solver's port; the judgement that a step serves or defeats a purpose supplied by whoever can be held to it.

## Scope

One problem. This package answers the question above and nothing adjacent to it.
If a change here would also need a second question answered, it belongs in a
different repository.

## Where it sits

```
grammar ──▶ versum ──▶ solver ──▶ loomground-mandate
```

Above the reasoning kernel, never beside it. It uses `loomground-solver`'s shared
three-valued verdict, its OPEN-dominant strict-AND fold, and its injected ports —
and reaches into no solver internals. Nothing in the kernel imports this package,
and nothing here imports governance, a corpus, or a domain.

## Contract

The package **reports**; it resolves nothing and decides nothing. Judgements
arrive already made, from whoever can be held to them, and are compared rather
than derived. Where a term is absent it escalates rather than passing: an
unmeasured input is not the same as a satisfied one, and the two never collapse
into a single value.

## Install

```
pip install loomground-mandate
```

## Licence

Apache-2.0 for the code; CC-BY-4.0 for the prose in this README. See `NOTICE`.
