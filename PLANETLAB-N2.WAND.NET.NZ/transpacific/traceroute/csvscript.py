import csv
txt_file = r"data.txt"
csv_file = r"data.csv"

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
in_txt = csv.reader(open(txt_file, "r"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'w'))
out_csv.writerow(["Node name", "1st Packet ms","2nd Packet ms", "3rd Packet ms"])
out_csv.writerows(in_txt)