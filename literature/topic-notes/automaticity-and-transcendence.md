# Automaticity, frequencies, Cobham, and transcendental slopes

## Three distinct facts

1. **Finite-state periodic residue data.** A sequence periodic modulo a fixed integer is automatic. This is elementary.
2. **Rational-frequency lemma.** If a symbol frequency exists in a `k`-automatic sequence, then it is rational. KTHM-0005 proves this from the rational transition matrix of a DFAO.
3. **Cobham's theorem.** A set recognizable in two multiplicatively independent bases is ultimately periodic. [@Cobham1969; @AlloucheShallit2003]

These are not interchangeable.

## Application to `CLAUDE/T-0003`

The repository's desired schedule has a frequency given by a rational expression in `log_64 81`. KTHM-0006 proves that `log_64 81` is transcendental by Gelfond–Schneider; hence the displayed nonconstant rational expression is transcendental when defined.

If the schedule is a finite-alphabet `k`-automatic word and the asserted letter frequency exists, KTHM-0005 already gives a contradiction. Cobham is unnecessary for this step.

Cobham would become relevant only after exhibiting the **same** set or sequence as recognizable in two multiplicatively independent integer bases. An automatic arithmetic supply stream and a separate nonautomatic schedule are not, by themselves, an instance of Cobham.

## Sturmian and Ostrowski language

A mechanical/Sturmian word of irrational slope is a natural way to realize two gap lengths with an irrational frequency. Ostrowski numeration can make such words computable. That observation identifies a candidate complexity class; it does not prove that the resulting carry demands close or that every nonautomatic schedule is Sturmian.
