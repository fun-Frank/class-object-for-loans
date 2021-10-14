# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:06:08 2021

@author: 16617
"""

class finance(object):
    ''' financial stats of instance '''
    
    def __init__(self, name):

        self._name = name
        print('name: {}'.format(self._name))
        
    def who(self):
        ''' docstring to show name associated with instance '''
        print(self._name)
        
    def setIncome(self, income):
        self._income = income
        print('income: {}'.format(income))
        
    def setHausPmt(self, pmt):
        self._hausPmt = pmt
        print('house pmt: {}'.format(pmt))
        
    def setTaxRate(self, taxRate):
        ''' tax rate in percent '''
        self._taxRate = taxRate/100
        print('{}%'.format(taxRate))
        print(self._taxRate)        
    
class loan(finance):
    ''' sub class of finance '''
    
    def __init__(self, name):
        super().__init__(name)
        
    def setPV(self, PV):
        ''' set pV.. must be dollars '''
        self._PV = PV
        print('present value = ', self._PV)
        
    def setRate(self, ratePct):
        ''' set interest rate, percent 
        must be in to interest, apr 
        '''
        self._ratePct = ratePct
        print('APR = ', self._ratePct,'%')
        
    def setMonths(self, months):
        ''' set months to repay, usually an integer '''
        self._months = months
        print(self._months, 'months')
        
    def computePmt(self):
        ''' formula: pmt = PV*(r*(1+r)**n)/((1+r)**months -1)'''
        r = self._ratePct/100/12 # convert % to a decimal/month
        self._Pmt = r*self._PV/(1-(1+r)**(-self._months))
        print('payment = $', round(self._Pmt,2))
        return self._Pmt
    
    def totalAmtPaid(self, ratePct, months, PV):
        pass 
    
