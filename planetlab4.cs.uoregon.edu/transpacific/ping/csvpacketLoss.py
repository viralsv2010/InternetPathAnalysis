import csv

txt_file = r"packetLoss.txt"
csv_file = r"packetLoss.csv"

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
in_txt = csv.reader(open(txt_file, "r"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'w'))
out_csv.writerow(["","Percentage of Package Loss "])
out_csv.writerows(in_txt)