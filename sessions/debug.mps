*SENSE:Minimize
NAME          test_invalid_var_names
ROWS
 N  obj
 L  c1
 G  c2
 E  c3
 G  c4
COLUMNS
    End       c2         1.000000000000e+00
    End       c3         1.000000000000e+00
    End       obj        9.000000000000e+00
    a         c1         1.000000000000e+00
    a         c2         1.000000000000e+00
    a         obj        1.000000000000e+00
    b         c4         1.000000000000e+00
    g         c1         1.000000000000e+00
    g         c3        -1.000000000000e+00
    g         obj        4.000000000000e+00
RHS
    RHS       c1         5.000000000000e+00
    RHS       c2         1.000000000000e+01
    RHS       c3         7.000000000000e+00
    RHS       c4         0.000000000000e+00
BOUNDS
 FR BND       End     
 FR BND       a       
 FR BND       b       
 LO BND       g         -1.000000000000e+00
 UP BND       g          1.000000000000e+00
ENDATA
