CONJECTUREPANEL Quiz
PROOF "T→Q2, T, Q1, Q2→(¬B∧¬S∧¬P), Q1→(B∨Q2∨S∨P)∧(¬B∨¬Q2∨¬S)∧(¬B∨¬Q2∨¬P)∧(¬B∨¬P∨¬S) ⊢ (Q2∧¬B∧¬S∧¬P)"
INFER T→Q2,
     T,
     Q1,
     Q2→(¬B∧¬S∧¬P),
     Q1→(B∨Q2∨S∨P)∧(¬B∨¬Q2∨¬S)∧(¬B∨¬Q2∨¬P)∧(¬B∨¬P∨¬S)
     ⊢ (Q2∧¬B∧¬S∧¬P)
FORMULAE
0 Q2∧¬B∧¬S∧¬P,
1 ¬P,
2 Q2∧¬B∧¬S,
3 ¬B∧¬S∧¬P,
4 ¬B∧¬S,
5 ¬S,
6 Q2∧¬B,
7 ¬B,
8 Q2,
9 Q2→¬B∧¬S∧¬P,
10 T,
11 T→Q2,
12 Q1,
13 Q1→(B∨Q2∨S∨P)∧(¬B∨¬Q2∨¬S)∧(¬B∨¬Q2∨¬P)∧(¬B∨¬P∨¬S),
14 Q2→(¬B∧¬S∧¬P)
IS
SEQ (cut[B,C\8,0]) ("→ elim"[A,B\10,8]) (hyp[A\11]) (hyp[A\10]) (cut[B,C\3,0]) ("→ elim"[A,B\8,3]) (hyp[A\9]) (hyp[A\8]) (cut[B,C\4,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\4,1]) (hyp[A\3])) (cut[B,C\5,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\7,5]) (hyp[A\4])) (cut[B,C\7,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\7,5]) (hyp[A\4])) (cut[B,C\6,0]) ("∧ intro"[A,B\8,7]) (hyp[A\8]) (hyp[A\7]) (cut[B,C\2,0]) ("∧ intro"[A,B\6,5]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\1,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\4,1]) (hyp[A\3])) (cut[B,C\0,0]) ("∧ intro"[A,B\2,1]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "¬¬P ⊢ P"
INFER ¬¬P 
     ⊢ P 
FORMULAE
0 ⊥,
1 ¬¬P,
2 ¬P,
3 P 
IS
SEQ ("contra (classical)"[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q ⊢ ¬Q→¬P"
INFER P→Q 
     ⊢ ¬Q→¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q,
5 ¬P 
IS
SEQ ("→ intro"[A,B\1,5]) ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Quiz
PROOF "(B∨S∨Q), ¬S, Q→S ⊢ B"
INFER (B∨S∨Q),
     ¬S,
     Q→S 
     ⊢ B 
FORMULAE
0 ⊥,
1 B,
2 ¬S,
3 S,
4 Q,
5 Q→S,
6 B∨S,
7 B∨S∨Q 
IS
SEQ ("∨ elim"[A,B,C\6,4,1]) (hyp[A\7]) ("∨ elim"[A,B,C\1,3,1]) (hyp[A\6]) (hyp[A\1]) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0]) (cut[B,C\3,1]) ("→ elim"[A,B\4,3]) (hyp[A\5]) (hyp[A\4]) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q, ¬Q ⊢ ¬P"
INFER P→Q,
     ¬Q 
     ⊢ ¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q 
IS
SEQ ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P∨¬P"
INFER P∨¬P 
FORMULAE
0 ⊥,
1 ¬(P∨¬P),
2 P∨¬P,
3 P,
4 ¬P,
5 ¬(P∨¬P)
IS
SEQ ("contra (classical)"[A\2]) (cut[B,C\3,0]) ("contra (classical)"[A\3]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\3,4]) (hyp[A\4])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\4,3]) (hyp[A\3])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P ⊢ ¬¬P"
INFER P 
     ⊢ ¬¬P 
FORMULAE
0 ⊥,
1 ¬P,
2 P 
IS
SEQ ("¬ intro"[A\1]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
