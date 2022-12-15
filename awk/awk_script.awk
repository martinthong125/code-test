# Run the command below
# awk -f awk_script.awk /etc/passwd 
BEGIN { 
    print "Start of script" 
    } 
/root/ { 
    print $0 
    } 
END { 
    print "End of script" 
    }