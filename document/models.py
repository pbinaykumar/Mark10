from django.db import models

class All_Format(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=8,unique=True)

    def __str__(self):
        return self.name+'('+str(self.id)+')'
class File_Type(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=15)
    def __str__(self):
        return self.name+'('+str(self.id)+')'

class Available_Format(models.Model):
    id = models.AutoField(primary_key=True)
    input=models.ForeignKey(All_Format,on_delete=models.CASCADE)
    type=models.ForeignKey(File_Type,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.input)

class Output_Format(models.Model):
    id = models.AutoField(primary_key=True)
    available_format=models.ForeignKey(Available_Format,on_delete=models.CASCADE,null=True,blank=True)
    output = models.ForeignKey(All_Format, on_delete=models.CASCADE,null=True,blank=True)



class Document(models.Model):
    id=models.CharField(max_length=15,primary_key=True)
    output_format=models.CharField(max_length=6,blank=True,null=True)
    document=models.FileField(upload_to='input')
    output_document=models.FileField(upload_to='media/output',blank=True,null=True)



