#Exception Handling
import sys
class srinu:
    def __init__(self):
            print("constructor")
    def welcome(self):
            print("Welcome")
    def __del__(self):
            print("destructor")
 #Exception
    def members(self):
        try:
            members=['srinu','vamsi','vasu']
            print(members[3])
       # except IndexError:
        #    errorInfo=sys.exc_info()
         #   print(errorInfo[0],errorInfo[1])
            #print("Exception Occured")
        except IOError:
            print("Excute")
        except ImportError:
            print('import error')
        except:
            print('final except')
        else:
            print('All Good')
        finally:
            print('Every time i will call')
s1=srinu()
s1.welcome()
s1.members()