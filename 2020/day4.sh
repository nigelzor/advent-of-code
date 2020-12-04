#!/bin/bash
tr ' ' "\n" < day4_input.txt | grep -v ^cid | awk -f <(
cat << 'EOF'
  /:/ { c += 1 }
  /^$/ { if (c == 7) { t++ }; c = 0 }
  END { if (c == 7) { t++ }; print t }
EOF
)
tr ' ' "\n" < day4_input.txt | awk -F : -f <(
cat << 'EOF'
  /^byr:/ { if ($2 >= 1920 && $2 <= 2002) { c++ } }
  /^iyr:/ { if ($2 >= 2010 && $2 <= 2020) { c++ } }
  /^eyr:/ { if ($2 >= 2020 && $2 <= 2030) { c++ } }
  /^hgt:..in/ { c++ }
  /^hgt:1..cm/ { c++ }
  /^hcl:#[0-9a-z]{6}$/ { c++ }
  /^ecl:(amb|blu|brn|gry|grn|hzl|oth)$/ { c++ }
  /^pid:[0-9]{9}$/ { c++ }
  /^$/ { if (c == 7) { t++ }; c = 0 }
  END { if (c == 7) { t++ }; print t }
EOF
)
