from mongoengine import *
import datetime

class Message(Document):
    msg         =   StringField()

    def decrypt(self, pubkey=None, privkey=None):
        if not privkey:
            if not pubkey:
                raise Exception, "Need either pubkey or privkey"
            else:
                return self.msg + " decrypted with pubkey(" + pubkey + ")"
        else:
                return self.msg + " decrypted with privkey(" + privkey + ")"

    def encrypt(self, pubkey=None, privkey=None):
        if not privkey:
            if not pubkey:
                raise Exception, "Need either pubkey or privkey"
            else:
                return self.msg + " ecnrypted with pubkey(" + pubkey + ")"
        else:
                return self.msg + " encrypted with privkey(" + privkey + ")"



class User(Document):
    name        =   StringField()
    publickey   =   StringField(unique=True)

    verified    =   DateTimeField()

    def verify(self, privkey_encrypted_pubkey=None):
        if not privkey_encrypted_pubkey:
            raise Exception, "Need a privkey_encrypted_pubkey to verify"

        if not self.publickey:
            raise Exception, "Need to set self.publickey!"

        print "Should decrypt privkey_encrypted_pubkey(%s) with self.publickey(%s)" % (privkey_encrypted_pubkey, self.publickey)
        m = Message(msg='pubkey')
        pep = m.encrypt(privkey='my_priv_key')
        print "Pep = " + pep
        print m.decrypt(pubkey=self.publickey)


        self.verified = datetime.datetime.now()








