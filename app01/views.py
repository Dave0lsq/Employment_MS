from django.shortcuts import render, redirect
from django import forms
from app01 import models

def depart_list(request):
    '''Department List'''
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'queryset': queryset})

def depart_add(request):
    '''Add Department'''
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    title = request.POST.get('title')

    models.Department.objects.create(title=title)

    return redirect('/department/list/')

def depart_delete(request):
    '''Delete Department'''
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()

    return redirect('/department/list/')

def depart_edit(request, nid):
    '''Edit Department'''
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_object': row_object})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)

    return redirect('/department/list/')

def user_list(request):
    '''User List'''
    queryset = models.UserInfo.objects.all()

    '''
    for obj in queryset:
        #print(obj.id, obj.name, obj.gender, obj.get_gender_display(), obj.account, obj.create_time.strftime('%Y-%m-%d'))
        print(obj.name, obj.depart_id)
        obj.depart_id
        obj.depart.title
    '''

    return render(request, 'user_list.html', {'queryset':queryset})


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'gender', 'balance', 'depart', 'create_time']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}

def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})

    # Data Authentication
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # models.UserInfo.objects.create()
        form.save()
        return redirect('/user/list/')

    else:
        print(form.errors)

def user_delete(request):
    '''Delete User'''
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()

    return redirect('/user/list/')

def user_edit(request, nid):
    '''Edit User'''
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')

    return render(request, 'user_edit.html', {'form': form})