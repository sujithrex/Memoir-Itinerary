from datetime import datetime
from django.shortcuts import render, redirect
from .forms import RecordCreateForm, RecordUpdateForm
from .models import Record
from django.contrib.auth.decorators import login_required

@login_required
def homePageView(request):
    today = str(datetime.today())
    title = 'Welcome: This is the Home Page'
    # print(today)
    # searchresult=Record.objects.raw ("SELECT id,date,eventname,adobe,record,hero,source,note FROM record_record WHERE date = '"+ today +"'")
    tdate = datetime.now().strftime('%d' )
    
    month = str(datetime.today().month)
    # print("t"+tdate, "s"+ month)
        # searchresult=Record.objects.raw ("SELECT * FROM record_record WHERE date <= '"+ today +"'")
    print(str(month))
    print(str(tdate))
    
    # searchresult=Record.objects.raw ("select id,date,eventname,adobe,record,hero,source,note from record_record where month(date) ="+ str(month) +"and DAY([date]) = "+ str(tdate)+"")
    # searchresult=Record.objects.raw ("SELECT * FROM record_record WHERE date(d) = "+ str(tdate) +" AND date(m) = "+ str(month) +"")

    searchresult=Record.objects.raw ("select * from record_record where month(record_record.date) = month(CURDATE()) and day(record_record.date) = day(CURDATE())")





    # searchresult=Record.objects.raw ("SELECT id,date,eventname,adobe,record,hero,source,note  FROM record_record WHERE DAY([date]) = "+ str(month) +" AND MONTH([date]) =  "+ str(tdate)+"")
    context = {
    "title": title,
    "records": searchresult
    }
    return render(request, "pages/home.html",context)

@login_required
def recordView(request):
    record_list = Record.objects.all()
    return render(request, "pages/allrecords.html",{"records": record_list})

@login_required
def add_Record(request):
    form = RecordCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        if form.is_valid():
            form.save()
        return redirect('/allrecords')
    context = {
        "form": form,
        "title": "Add Record",
    }
    return render(request, "pages/add_new.html", context)


@login_required
def dateRangeView(request):
    if request.method =="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=Record.objects.raw ('select id,date,eventname,adobe,record,hero,source,note from record_record where date between"' +fromdate+ '"and"' +todate+'"')

        return  render(request,'pages/datefilter.html',{"records": searchresult})
    else:
       displaydata= Record.objects.all()
       return render(request,'pages/datefilter.html',{"records": displaydata})


@login_required
def update_items(request, pk):
    queryset = Record.objects.get(id=pk)
    form = RecordUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = RecordUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/allrecords')

    context = {
        'form':form
    }
    return render(request, 'pages/add_new.html', context)

@login_required
def delete_items(request, pk):
    queryset = Record.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/allrecords')
    return render(request, 'pages/delete_record.html')
@login_required
def view_items(request, pk):
    queryset = Record.objects.get(id=pk)
    form = RecordUpdateForm(instance=queryset)
    context = {
        'form':form
        
    }
    return render(request, 'pages/indicard.html', context )


def ideaPageView(request):
	title = 'Where this idea came from!!'
	context = {
	"title": title,
	}
	return render(request, "pages/idea.html",context)