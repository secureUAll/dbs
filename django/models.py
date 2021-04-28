from django.contrib.postgres.fields import ArrayField
from django.db import models

class User_Type(models.Model):
    cod=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=10)

    def _str_(self):
        return self.name

class User(models.Model):
    cod=models.BigAutoField(primary_key=True)
    email=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    user_type=models.ForeignKey(User_Type, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class Machine(models.Model):
    ip=models.CharField(max_length=15, primary_key=True)
    os=models.CharField(max_length=20)
    risk=models.IntegerField()
    scanLevel=models.IntegerField()
    location=models.CharField(max_length=30)

    def _str_(self):
        return self.ip

class Worker(models.Model):
    cod=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=12)
    status=models.CharField(max_length=12)
    failures=models.IntegerField()

    def _str_(self):
        return self.name

class Scan(models.Model):
    cod=models.BigAutoField(primary_key=True)
    machine=models.ForeignKey(Machine, on_delete=models.CASCADE)
    worker=models.ForeignKey(Worker, on_delete=models.CASCADE)
    date=models.DateField() # auto_now=True
    status=models.CharField(max_length=15)

class Worker_Scan_Comment(models.Model):
    cod=models.BigAutoField(primary_key=True)
    scan=models.ForeignKey(Scan, on_delete=models.CASCADE)
    comment=models.CharField(max_length=256)
    user_cod=models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.comment

class Machine_User(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True) # not sure about that
    machine=models.ForeignKey(Machine, on_delete=models.CASCADE, primary_key=True)
    user_type=models.ForeignKey(User_Type, on_delete=models.CASCADE)

class Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    machine=models.ForeignKey(Machine, on_delete=models.CASCADE)
    notification_email=models.CharField(max_length=50)
    description=models.CharField(max_length=256)

    def _str_(self):
        return self.description

class Machine_Dns(models.Model):
    machine=models.ForeignKey(Machine, on_delete=models.CASCADE)
    dns=models.CharField(max_length=100, primary_key=True)

    def _str_(self):
        return self.dns

class Machine_Port(models.Model):
    machine=models.ForeignKey(Machine, on_delete=models.CASCADE, primary_key=True)
    port=models.IntegerField(primary_key=True)
    service=models.ForeignKey(Machine_Service, on_delete=models.CASCADE)

    def _str_(self):
        return self.service + " (" + str(self.port) + ")"

class Machine_Service(models.Model):
    service=models.CharField(max_length=24, primary_key=True)
    version=models.CharField(max_length=12, primary_key=True)

    def _str_(self):
        return self.service + " (" + str(self.version) + ")"

class Vulnerability(models.Model):
    cod=models.BigAutoField(primary_key=True)
    risk=models.IntegerField()
    type=models.CharField(max_length=12)
    description=models.CharField(max_length=256)
    location=models.CharField(max_length=30)
    status=models.CharField(max_length=12)
    machine=models.ForeignKey(Machine, on_delete=models.CASCADE)

    def _str_(self):
        return "(" + self.risk + ") " + self.description

class Vulnerability_Comment(models.Model):
    cod=models.BigAutoField(primary_key=True)
    vulnerability=models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.CharField(max_length=256)

    def _str_(self):
        return self.comment

class Log(models.Model):
    cod=models.BigAutoField(primary_key=True)
    date=models.DateField() # auto_now=True
    machine=models.ForeignKey(Machine, on_delete=models.CASCADE)
    worker=models.ForeignKey(Worker, on_delete=models.CASCADE)
    path=models.CharField(max_length=256) #caminho para o ficheiro de logs
    

