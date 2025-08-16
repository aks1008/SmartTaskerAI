import sqlite3
import random
from datetime import datetime, timedelta

# Connect to a database (creates the file if it doesn't exist)
conn = sqlite3.connect('school.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS students')

# (Optional) Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        studentId TEXT PRIMARY KEY,
        name TEXT,
        dateOfBirth TEXT,
        className TEXT,
        totalMarks INTEGER,
        emergencyContact TEXT
    )
''')

students = [
  ("S0001","Aarav Patel","2008-03-12","8A",782,"+1-555-0101"),
  ("S0002","Maya Singh","2007-11-02","9B",812,"+1-555-0102"),
  ("S0003","Liam Johnson","2006-06-22","10C",765,"+1-555-0103"),
  ("S0004","Sofia Garcia","2009-01-15","7A",698,"+1-555-0104"),
  ("S0005","Noah Brown","2005-09-05","11B",845,"+1-555-0105"),
  ("S0006","Emma Davis","2010-12-19","6C",712,"+1-555-0106"),
  ("S0007","Oliver Wilson","2008-07-30","8B",730,"+1-555-0107"),
  ("S0008","Ava Martinez","2007-04-09","9A",790,"+1-555-0108"),
  ("S0009","Elijah Anderson","2006-02-27","10A",801,"+1-555-0109"),
  ("S0010","Isabella Thomas","2009-10-11","7B",677,"+1-555-0110"),
  ("S0011","Lucas Taylor","2005-05-03","11A",858,"+1-555-0111"),
  ("S0012","Mia Moore","2010-08-21","6A",705,"+1-555-0112"),
  ("S0013","Mason Jackson","2008-11-29","8C",744,"+1-555-0113"),
  ("S0014","Charlotte White","2007-03-18","9C",826,"+1-555-0114"),
  ("S0015","James Harris","2006-12-02","10B",778,"+1-555-0115"),
  ("S0016","Amelia Martin","2009-06-14","7C",693,"+1-555-0116"),
  ("S0017","Benjamin Thompson","2005-02-08","11C",838,"+1-555-0117"),
  ("S0018","Harper Garcia","2010-09-26","6B",721,"+1-555-0118"),
  ("S0019","Ethan Martinez","2008-05-07","8D",709,"+1-555-0119"),
  ("S0020","Evelyn Robinson","2007-01-30","9D",799,"+1-555-0120"),
  ("S0021", "Ankesh Patel", "2008-03-12", "8A", 782, "+1-555-0101"),
    ("S0022", "Maya Sharma", "2007-11-02", "9B", 812, "+1-555-0102"),
    ("S0023", "Vivaan Sharma", "2008-07-19", "8B", 765, "+1-555-0103"),
    ("S0024", "Diya Mehta", "2007-05-23", "9A", 798, "+1-555-0104"),
    ("S0025", "Krishna Iyer", "2008-01-30", "8C", 745, "+1-555-0105"),
    ("S0026", "Anaya Reddy", "2007-09-14", "9C", 820, "+1-555-0106"),
    ("S0027", "Rohan Desai", "2008-06-11", "8A", 790, "+1-555-0107"),
    ("S0028", "Ishita Kapoor", "2007-12-05", "9B", 805, "+1-555-0108"),
    ("S0029", "Aditya Joshi", "2008-04-17", "8B", 768, "+1-555-0109"),
    ("S0030", "Sneha Nair", "2007-08-29", "9A", 799, "+1-555-0110"),
    ("S0031", "Yash Verma", "2008-02-21", "8C", 752, "+1-555-0111"),
    ("S0032", "Tanya Gupta", "2007-10-10", "9C", 818, "+1-555-0112"),
    ("S0033", "Kunal Saxena", "2008-05-06", "8A", 784, "+1-555-0113"),
    ("S0034", "Meera Bhatt", "2007-11-25", "9B", 810, "+1-555-0114"),
    ("S0035", "Aryan Malhotra", "2008-07-03", "8B", 770, "+1-555-0115"),
    ("S0036", "Nisha Pillai", "2007-06-18", "9A", 795, "+1-555-0116"),
    ("S0037", "Kabir Chatterjee", "2008-01-09", "8C", 748, "+1-555-0117"),
    ("S0038", "Riya D'Souza", "2007-09-30", "9C", 822, "+1-555-0118"),
    ("S0039", "Dev Mishra", "2008-03-27", "8A", 787, "+1-555-0119"),
    ("S0040", "Simran Kaur", "2007-07-12", "9B", 803, "+1-555-0120"),
    ("S0041", "Ayaan Jain", "2008-06-25", "8B", 763, "+1-555-0121"),
    ("S0042", "Pooja Agarwal", "2007-05-15", "9A", 800, "+1-555-0122"),
    ("S0043", "Harsh Vora", "2008-02-02", "8C", 750, "+1-555-0123"),
    ("S0044", "Neha Kulkarni", "2007-10-20", "9C", 819, "+1-555-0124"),
    ("S0045", "Rajiv Menon", "2008-04-09", "8A", 781, "+1-555-0125"),
    ("S0046", "Priya Das", "2007-08-07", "9B", 807, "+1-555-0126"),
    ("S0047", "Siddharth Rao", "2008-05-28", "8B", 766, "+1-555-0127"),
    ("S0048", "Aishwarya Ghosh", "2007-06-03", "9A", 796, "+1-555-0128"),
    ("S0049", "Manav Bhatia", "2008-01-18", "8C", 747, "+1-555-0129"),
    ("S0050", "Juhi Sen", "2007-09-08", "9C", 823, "+1-555-0130"),
    ("S0051", "Rajat Kapoor", "2008-03-04", "8A", 786, "+1-555-0131"),
    ("S0052", "Kritika Raina", "2007-07-27", "9B", 804, "+1-555-0132"),
    ("S0053", "Nikhil Tripathi", "2008-06-14", "8B", 764, "+1-555-0133"),
    ("S0054", "Shruti Mohan", "2007-05-01", "9A", 801, "+1-555-0134"),
    ("S0055", "Varun Shetty", "2008-02-13", "8C", 751, "+1-555-0135"),
    ("S0056", "Anjali Roy", "2007-10-01", "9C", 817, "+1-555-0136"),
    ("S0057", "Raghav Kulkarni", "2008-04-22", "8A", 783, "+1-555-0137"),
    ("S0058", "Bhavya Sinha", "2007-08-15", "9B", 806, "+1-555-0138"),
    ("S0059", "Omkar Pandey", "2008-05-10", "8B", 769, "+1-555-0139"),
    ("S0060", "Lavanya Joshi", "2007-06-25", "9A", 794, "+1-555-0140"),
    ("S0061", "Tanmay Rathi", "2008-01-05", "8C", 746, "+1-555-0141"),
    ("S0062", "Sana Khan", "2007-09-18", "9C", 821, "+1-555-0142"),
    ("S0063", "Arjun Bhargava", "2008-03-15", "8A", 788, "+1-555-0143"),
    ("S0064", "Rekha Pillai", "2007-07-05", "9B", 802, "+1-555-0144"),
    ("S0065", "Dhruv Nair", "2008-06-01", "8B", 767, "+1-555-0145"),
    ("S0066", "Ira Deshmukh", "2007-05-20", "9A", 797, "+1-555-0146"),
    ("S0067", "Karan Chopra", "2008-02-25", "8C", 753, "+1-555-0147"),
    ("S0068", "Nandini Rao", "2007-10-12", "9C", 816, "+1-555-0148"),
    ("S0069", "Amitabh Das", "2008-04-01", "8A", 785, "+1-555-0149"),
    ("S0070", "Shreya Gopal", "2007-08-22", "9B", 808, "+1-555-0150"),
]

cursor.executemany('INSERT INTO students (studentId, name, dateOfBirth, className, totalMarks, emergencyContact) VALUES (?, ?, ?, ?, ?, ?)', students)

# Commit changes and close the connection
conn.commit()
conn.close()