SMT-LIB v2 Guide for CVC5
SMT-LIB v2 is a standard format for specifying Satisfiability Modulo Theories (SMT) problems. CVC5 supports SMT-LIB v2 scripts with the following features:

Logics: QF_LIA (Quantifier-Free Linear Integer Arithmetic), QF_LRA, etc.
Syntax:
(set-logic <logic>): Specify the logic.
(declare-fun <name> () <type>): Declare variables (e.g., Int, Real).
(assert <expression>): Add constraints.
(check-sat): Check satisfiability.


Example:(set-logic QF_LIA)
(declare-fun x () Int)
(declare-fun y () Int)
(assert (= (+ x y) 10))
(assert (= (- x y) 4))
(check-sat)



