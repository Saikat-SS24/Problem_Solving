cat file.txt | head -n1 | awk '{print NF}' | xargs seq 1 \
  | xargs -I {} sh -c \
  "cat file.txt | awk '{print \${}}' | tr '\n' ' '  | sed -E 's/\ +$//g' && echo"
