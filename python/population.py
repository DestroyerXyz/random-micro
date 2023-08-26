final = 0
initial = int(input("Enter initial population: "))
rate = float(input("Enter birth rate: "))
years = int(input("Enter years: "))

for i in range(0, years):
      final = ((initial*rate)+(initial*100))/100
      print(i+1, '. ', "{:e}".format(int(initial)),
            " - ", "{:e}".format(int(final)))
      initial = final
