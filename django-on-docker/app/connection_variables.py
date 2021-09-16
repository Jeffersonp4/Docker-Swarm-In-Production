

class EncapsulatedConnection:
    def __init__(self,ip,user,pw,puerto,dbType,active):
        self._ip = ip
        self._user = user
        self._pw = pw
        self._puerto = puerto
        self._dbType = dbType
        self._active = active

        @property
        def ip(self):
            return self._ip

        @ip.setter
        def ip(self,ip):
            self._ip = ip

        @property
        def user(self):
            return self._user

        @user.setter
        def user(self, user):
            self._user = user

        @property
        def pw(self):
            return self._pw

        @pw.setter
        def pw(self, pw):
            self._pw = pw

        @property
        def puerto(self):
            return self._puerto

        @puerto.setter
        def puerto(self, puerto):
            self._puerto = puerto

        @property
        def dbType(self):
            return self._dbType

        @dbType.setter
        def dbType(self, dbType):
            self._dbType = dbType

        @property
        def active(self):
            return self._active

        @active.setter
        def active(self, active):
            self._active = active