BEGIN { sum = 0; }
$3 > 0 { printf("%s %5d %3d %6d\n", $1, $2, $3, $2*$3);
         sum += $2*$3; }
END { printf("total %20d\n", sum); }
