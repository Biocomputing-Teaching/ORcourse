\* test_invalid_var_names *\
Minimize
obj: 9 End + a + 4 g
Subject To
c1: a + g <= 5
c2: End + a >= 10
c3: End - g = 7
c4: b >= 0
Bounds
 End free
 a free
 b free
 -1 <= g <= 1
End
