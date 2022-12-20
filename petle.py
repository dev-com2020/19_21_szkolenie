# znaPythona = 0
#
# if znaPythona:
#     print("Gratulacje!")
# else:
#     print("Musisz się nauczyć!")
#
# print("...Kolejne instrukcje programu...")

znaPythona = input("Czy znasz język?(Wprowadź 't' lub 'n')")

if znaPythona == 'tak' or znaPythona == 'Tak' or znaPythona == 't':
    print("Gratulacje!")
elif znaPythona == 'nie':
    print("Musisz się nauczyć!")
else:
    print("Nie ma takiego wyboru!")

print("...Kolejne instrukcje programu...")