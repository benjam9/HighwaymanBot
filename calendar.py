import month
class Calendar:
  def __init__(self, nMonths, monthArr):
    self.nMonths = nMonths
    self.monthArr = monthArr


months = [month.Month(31, "January", 1), month.Month(28, "February", 2), month.Month(31, "March", 3), month.Month(30, "April", 4), month.Month(31, "May", 5), month.Month(30, "June", 6), month.Month(31, "July", 7), month.Month(31, "August", 8), month.Month(30, "September", 9), month.Month(31, "October", 10), month.Month(30, "November", 11), month.Month(31, "December", 12)]
c1 = calendar.Calendar(12, months)

print(c1.nMonths)
print(c1.monthArr[0].name)
