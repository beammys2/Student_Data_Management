from django import forms 

class Stud(forms.Form):
    reg=forms.IntegerField()
    name=forms.CharField(max_length=30)
    clas=forms.IntegerField()
    section=forms.CharField(max_length=30)
    rollno=forms.IntegerField()
    percentage=forms.CharField(max_length=30) 
    gender=forms.CharField(max_length=30) 
    phone=forms.IntegerField()
    address=forms.CharField(max_length=30)
    

class Delete(forms.Form):
    reg=forms.IntegerField()
    
class Update(forms.Form):
    reg=forms.IntegerField()
    name=forms.CharField(max_length=30)
    clas=forms.IntegerField()
    section=forms.CharField(max_length=30)
    rollno=forms.IntegerField()
    percentage=forms.CharField(max_length=30) 
    gender=forms.CharField(max_length=30) 
    phone=forms.IntegerField()
    address=forms.CharField(max_length=30)

class Search(forms.Form):
    name=forms.CharField(max_length=30)