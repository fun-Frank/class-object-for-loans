class loan(object):
    def __init__(self, name):
        self._name = name

    def who(self):
        print(self._name)

    def setPV(self, PV):
        self._PV = PV
        print('present value = ', self._PV)

    def setRate(self, ratePct):
        # set interest, apr
        self._ratePct = ratePct
        print('APR = ', self._ratePct, '%')

    def setMonths(self, months):
        self._months = months
        print(self._months, 'months')

    def computePmt(self):
        # formula: pmt = PV*(r*(1+r)**n)/((1+r)**months -1)
        r = self._ratePct / 100 / 12
        self._Pmt = self._PV * (r * (1 + r) ** self._months) / ((1 + r) ** self._months - 1)
        print('payment = $', round(self._Pmt, 2))
        return self._Pmt

    def setPmt(self, Pmt):
        self._Pmt = Pmt
        print("Set the payment to {}".format(round(self._Pmt, 2)))

    def computePV(self):
        r = self._ratePct / 100 / 12
        self._PV = self._Pmt / r * (1 - (1 - r) ** (-self._months))
        print("Max loan = ${}".format(-round(self._PV, 2)))


if __name__ == "__main__":
    loan1 = loan('Dr J')
    loan1.who()

    loan1.setPV(27150)  # mini cooper
    loan1.setRate(1.9)
    loan1.setMonths(42)
    payment = loan1.computePmt()

    loan2 = loan("Frank")
    loan2.who()
    loan2.setRate(4.4)
    loan2.setMonths(48)
    loan2.setPmt(399)
    loan2.computePV()
   
