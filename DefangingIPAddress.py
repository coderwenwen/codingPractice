import unittest
class DefangingIPAddress(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")





