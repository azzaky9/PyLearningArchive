frmt = 'Hari ini aku makan {1},dan hari ini {0}, besok mau {2}'.format("Ayam", "Ikan", "Bebek")

frmt_without_index = '{}, {}, {}'.format("A", "B", "C")

frmt_short = "{2}, {0}, {1}".format(*'abc')

repeated = "{0}{1}{0}{0}{1}".format("abra", "cada")

print(repeated)

print(frmt_short)

print(frmt_without_index)

print(frmt)