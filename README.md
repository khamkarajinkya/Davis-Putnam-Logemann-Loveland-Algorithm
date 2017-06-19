# Davis-Putnam-Logemann-Loveland-Algorithm

A recursive search algorithm for evaluating satisfiability of sentences in CNF

It relies on two simple sub-algorithms:

1. Unit propagation
2. Pure literal elimination

Unit propagation

Clauses with only one literal are called unit clauses

Example The first clause in P 1 ∧ (¬P 1 ∨ P 2 ) ∧ (P 3 ∨ P 4 )

Literals in unit clauses must be set to true. P 1 = true is required
Unit propagation repeatedly satisfies unit clauses and eliminates the literals:

P 1 ∧ (¬P 1 ∨ P 2 ) ∧ (P 3 ∨ P 4 )
P 2 ∧ (P 3 ∨ P 4 ) (by setting P 1 = true)
(P 3 ∨ P 4 ) (by setting P 2 = true)

Pure literal elimination

Atomic sentences that only appear in positive literals or only appear in negative literals are called pure
Example P 1 is pure in (P 1 ∨P 2 )∧(P 1 ∨P 3 )∧(¬P 2 ∨¬P 3 )

Assignment of pure atomic sentences is trivial

(P 1 ∨ P 2 ) ∧ (P 1 ∨ P 3 ) ∧ (¬P 2 ∨ ¬P 3 )
(¬P 2 ∨ ¬P 3 )

The DPLL Algorithm
Input A sentence α in CNF
1. Return false if α contains an empty clause, trueif no clauses
2. UnitPropagation(α)
3. AssignPure(α)
4. Choose unassigned variable P
5. Return DPLL(Reduce(α,P)) or DPLL(Reduce(α,¬P))
