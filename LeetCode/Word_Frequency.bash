awk 'BEGIN { 
    PROCINFO["sorted_in"] = "@val_num_desc"   
} { 
    for (i=1;i<=NF;i++) {   
        a[$i]++             
    }
} END {
    for (i in a) {          
        print i,a[i]
    }
}' words.txt
