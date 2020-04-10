from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import json  
from django.views.generic.edit import FormView 
from django import forms 

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class getImage(APIView):
    permission_classes = (IsAuthenticated,)   

    # print("image")
    # form_class = FileFieldForm
    # template_name = 'upload.html'  # Replace with your template.
    # success_url = '...'  # Replace with your URL or reverse().
    
    parser_classes = (FileUploadParser, )
    def post(self, request):
        # form_class = self.get_form_class()
        # form = self.get_form(form_class)
        # files = request.FILES.getlist('file_field')
        # if form.is_valid():
        #     for f in files:
        #         print("got new file")
        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)
        try:
            up_file = request.FILES['image_file1']
            destination = open("D:/Development_Engineering_Prj/farmers_mate_mate/lib/" + up_file.name, 'wb+')
            for chunk in up_file.chunks():
                destination.write(chunk)
            destination.close()  # 
        except Exception as e:
            print (e ) 

        return Response(status =204)
        #     return Response(status, 
        #                    status.HTTP_500_INTERNAL_SERVER_ERROR)
        # return Response(status, status.HTTP_200_OK) 



class TeacherView(APIView):
    permission_classes = (IsAuthenticated,)   
    
    def post(self, request): 

        # use these commands if request data info is needed
       
        print (request.META.get('HTTP_AUTHORIZATION') )  ;
        print (json.loads(request.body.decode())['message'])  ; 
        print (request.user.username)

        content = [
                    {'message': 'Teacher_profile'},
                    {'name': 'Radheshyam'},
                    {'id': '2021521215'}, 
                    {  "detail": [
                                     {
                                        "subject_name" : "math",
                                        "subject_id" : "ma101",
                                        "students_list" : [
                                                                {
                                                                    "student_name": "sibbi",
                                                                    "student_id": "1",
                                                                },
                                                                {
                                                                    "student_name": "garima",
                                                                    "student_id": "2",
                                                                }, 
                                                          ],
                                    },
                                    {
                                        "subject_name" : "astronomy",
                                        "subject_id" : "as101",
                                        "students_list" : [
                                                                {
                                                                    "student_name": "mayank",
                                                                    "student_id": "3",
                                                                },
                                                                {
                                                                    "student_name": "garima",
                                                                    "student_id": "2",
                                                                },
                                                             ],
                                    },  
                                ], 
                        },
 
                 ]

        return Response(content)
 
      
 

class ClassHistory(APIView):
    permission_classes = (IsAuthenticated,)  
    
    def post(self, request): 

        print (json.loads(request.body.decode())['message'])  ; 
        print (json.loads(request.body.decode())['subject_id'])  ;  
        print (request.user.username);

        content = [
                    {'message': 'Teacher_profile'},
                    {'subject_id': 'ma101'},
                    { "list_date_wise" : [
                                        {
                                            "date": "27.2.2020",
                                            "present" : "50",
                                            "total"   : "64",
                                        },
                                        {
                                            "date": "27.2.2020",
                                            "present" : "45",
                                            "total"   : "64",
                                        }, 
                                        {
                                            "date": "27.2.2020",
                                            "present" : "25",
                                            "total"   : "64",
                                        },
                                        {
                                            "date": "27.2.2020",
                                            "present" : "60",
                                            "total"   : "64",
                                        },
                                    ] ,
                          },
                  ]
        return Response(content)
 
      
 
# class getImage(APIView):
#     permission_classes = (IsAuthenticated,)   
#     # def post(self, request):  
#     def handle_uploaded_file(f):
#             with open('some/file/name.txt', 'wb+') as destination:
#                 for chunk in f.chunks():
#                     destination.write(chunk)

#     def upload_file(self, request):
#             if request.method == 'POST':
#                 form = UploadFileForm(request.POST, request.FILES)
#                 if form.is_valid():
#                     handle_uploaded_file(request.FILES['file'])
#                     return HttpResponseRedirect('/success/url/')
#             else:
#                 form = UploadFileForm()
#             return render(request, 'upload.html', {'form': form})
#                   ]
#             # return Response(content)
 
      
 

class StudentHistory(APIView):
    permission_classes = (IsAuthenticated,)    

    def post(self, request): 

        print (json.loads(request.body.decode())['message'])  ; 
        print (json.loads(request.body.decode())['subject_id'])  ;  
        print (json.loads(request.body.decode())['student_id'])  ;  
        print (request.user.username);
        
        content = [
                    {'message': 'Student_History'},
                    {      "subject_id" : "as101"  , 
                            "student_id": "1",
 
                            "list" : [
                                        {
                                            "date": "27.2.2020",
                                            "class_position" : "1",
                                            "Attendance" : "P"
                                        },
                                        {
                                            "date": "26.2.2020",
                                            "class_position" : "1",
                                            "Attendance" : "A"
                                        } ,
                                        {
                                            "date": "29.2.2020",
                                            "class_position" : "1",
                                            "Attendance" : "A"
                                        },
                                        {
                                            "date": "24.2.2020",
                                            "class_position" : "1",
                                            "Attendance" : "A"
                                        } ,
                                  ] ,
                     },
                ],   

        return Response(content) 