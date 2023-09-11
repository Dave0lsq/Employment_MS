from django.shortcuts import render, redirect
from django import forms
from app01 import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'index.html')

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

    # Use Bootstrap Style
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loop and find all widgets, add class = 'form-control'
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


def school_list(request):
    '''School List'''
    # Initialize Search Box
    data_dict = {}

    # Obtain user's search value
    search_data = request.GET.get('q', "")

    # If user input a search content, output the target
    if search_data:
        # Find the target
        data_dict["name__contains"] = search_data

    # If user doesn't input, list all
    queryset = models.SchoolInfo.objects.filter(**data_dict).order_by('id')

    paginator = Paginator(queryset, 10) # Initialize a paging object, displayed per page 10
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    # is_paginated = True if paginator.num_pages > 1 else False  # 如果页数小于1不使用分页
    # context = {'page_obj': page_obj, 'is_paginated': is_paginated}

    return render(request, 'school_list.html', locals())


class SchoolModelForm(forms.ModelForm):
    class Meta:
        model = models.SchoolInfo
        fields = ['name', 'district', 'status']

    # Use Bootstrap Style
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loop and find all widgets, add class = 'form-control'
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}

def school_add(request):
    '''Add School'''
    if request.method == 'GET':
        form = SchoolModelForm()
        return render(request, 'school_add.html', {'form':form})

    form = SchoolModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/school/list/')
    else:
        print(form.errors)


def school_edit(request, nid):
    '''Edit School'''
    row_object = models.SchoolInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = SchoolModelForm(instance=row_object)
        return render(request, 'school_edit.html', {'form': form})

    form = SchoolModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/school/list/')

    return render(request, 'school_edit.html', {'form': form})

