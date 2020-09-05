from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np 
from zipfile import ZipFile
import os
import io

from .forms import FileUpload

def upload(request):
	if request.method == 'POST':
		upload_form = FileUpload(request.POST,request.FILES)
		if upload_form.is_valid():
			f = request.FILES['upload_file']
			filename = str(f)
			with open('upload_files/'+filename,'wb+') as out:
				for data in f:
					out.write(data)
			response = HttpResponse("Upload Success")		
			return	response	
	else:	
		upload_form = FileUpload()
	return render(request,'upload.html',{'form':upload_form})	

def subset(request,filename):
	df = pd.read_excel('upload_files/'+filename+'.xlsx')

	pc_df = df[(df['Accepted Compound ID'].str.endswith('PC',na=False)) & (df['Accepted Compound ID'].str[-3]!='L')]
	pc_df.to_csv('PC.csv',index=False)

	lpc_df = df[df['Accepted Compound ID'].str.endswith('LPC',na=False)]
	lpc_df.to_csv('LPC.csv',index=False)

	plasgn_df = df[df['Accepted Compound ID'].str.endswith('plasmalogen',na=False)]
	plasgn_df.to_csv('Plasmalogen.csv',index=False)

	zip_file_list = ['PC.csv','LPC.csv','Plasmalogen.csv']
	
	download_file = io.BytesIO()
	with ZipFile(download_file,'w') as zip_file:
		for csv_file in zip_file_list:
			zip_file.write(csv_file)
			os.remove(csv_file) 

	response = HttpResponse(download_file.getvalue(),content_type='application/octet-stream')		
	response['Content-Disposition'] = 'attachment; filename="task_1_output.zip"'
			
	return response

def rounded_time(row):
	time = row['Retention time (min)'] 
	if time>1:
		return round(time)
	else:
		return 1	

def grouping(request, filename):
  df = pd.read_excel('upload_files/'+filename+'.xlsx')
	
  rounded_retention_time = df.apply(lambda row : rounded_time(row),axis=1)
  df.insert(2,'Retention Time Roundoff (in mins)',rounded_retention_time)
  
  df.to_csv('task2.csv',index=False)

  del df['m/z']
  del df['Retention time (min)']

  dfsorted=df.sort_values('Retention Time Roundoff (in mins)')
  avg = dfsorted.groupby('Retention Time Roundoff (in mins)').mean().reset_index()
  avg['avg']=avg.mean(axis=1)
  avg.to_csv("task3.csv",index=True)

  zip_file_list = ['task2.csv', 'task3.csv']

  download_file = io.BytesIO()

  with ZipFile(download_file,'w') as zip_file:
	  for csv_file in zip_file_list:
		  zip_file.write(csv_file)
		  os.remove(csv_file)


  response = HttpResponse(download_file.getvalue(),content_type='application/octet-stream')		
  response['Content-Disposition'] = 'attachment; filename="task_2_3_output.zip"'

  return response













