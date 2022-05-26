string = 'SOC 23 CTech 5 DSBS8 NWC 56 CINtel 20 5'
findnum = lambda st,lennum: sorted([i  for i in st.split() if (i.isdigit() and len(i)>=lennum) ])

s = findnum(string,2)
print(s)