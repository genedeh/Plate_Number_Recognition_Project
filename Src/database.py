import sqlite3

connection = sqlite3.connect('nigeria_plate_number_code.db')

cursor = connection.cursor()

# cursor.execute("""CREATE TABLE nigeria_plate_number_code (
#                         code text
# )""")

# cursor.execute("""INSERT INTO nigeria_plate_number_code VALUES("JJJ"), ("AAA"), ("LSR"), ("FKJ"), ("FST"), ("APP"),
# ("AGL"), ("EPE"), ("LND"), ("MUS"), ("KRE"), ("FNN"), ("SGB"), ("LES"), ("EDE"), ("GBN"), ("BAT"), ("CRC"), ("BDW"),
# ("DDM"), ("BKR"), ("DMS"), ("NGW"), ("JBY"), ("KFY"), ("BRE"), ("DJA"), ("MLF"), ("KTN"), ("DTS"), ("BDJ"), ("GBR"),
# ("SEY"), ("LUY"), ("AME"), ("MAP"), ("NRK"), ("BJE"), ("KAM"), ("ANA"), ("CAL"), ("KMM"), ("BRA"), ("DUK"), ("GEP"),
# ("BNS"), ("EFE"), ("GGJ"), ("CKK"), ("TGD"), ("UDU"), ("BKS"), ("GWL"), ("NSR"), ("UGG"), ("KMC"), ("TRN"), ("DTF"),
# ("DAL"), ("KER"), ("EFY"), ("ADK"), ("EMR"), ("AMK"), ("KLE"), ("TUN"), ("WEN"), ("KEK"), ("AKR"), ("KTP"), ("FFN"),
# ("REE"), ("SUA"), ("JTA"), ("NND"), ("ABU"), ("AHD"), ("KNM"), ("ABM"), ("NDN"), ("BGM"), ("BNY"), ("DEG"), ("NCH"),
# ("MHA"), ("KHE"), ("KPR"), ("SKP"), ("BRR"), ("RUM"), ("RGM"), ("GGU"), ("KPK"), ("BER"), ("PBT")""")

cursor.execute("""SELECT * FROM nigeria_plate_number_code""")
print(cursor.fetchall())
connection.commit()

connection.close()
