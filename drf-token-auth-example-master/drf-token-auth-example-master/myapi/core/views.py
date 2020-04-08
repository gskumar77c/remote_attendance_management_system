from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TeacherView(APIView):
    permission_classes = (IsAuthenticated,) 

    def post(self, request):
        content = [
                    {'message': 'Teacher_profile'},
                    { "subjects_list" : [
                                            {
                                                "subject_name": "math",
                                                "subject_id": "ma101",
                                            },
                                            {
                                                "subject_name": "astronomy",
                                                "subject_id": "as101",
                                            }, 
                                          ],
                    },
                    {  "details": [
                                     {
                                        "subject_name" : "math",
                                        "subject_id" : "ma101",
                                        "students_list" : [
                                                                {
                                                                    "subject_name": "sibbi",
                                                                    "subject_id": "1",
                                                                },
                                                                {
                                                                    "subject_name": "garima",
                                                                    "subject_id": "2",
                                                                }, 
                                                          ],
                                    },
                                    {
                                        "subject_name" : "astronomy",
                                        "subject_id" : "as101",
                                        "students_list" : [
                                                                {
                                                                    "subject_name": "mayank",
                                                                    "subject_id": "3",
                                                                },
                                                                {
                                                                    "subject_name": "garima",
                                                                    "subject_id": "2",
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
 
      
 

class StudentHistory(APIView):
    permission_classes = (IsAuthenticated,) 

    def post(self, request):
        content = [
                    {'message': 'Student_History'},
                    {      "subject_id" : "as101"  , 
                            "student_id": "1",
 
                            "list" : [
                                        {
                                            "date": "27.2.2020",
                                            "Attendance" : "P"
                                        },
                                        {
                                            "date": "26.2.2020",
                                            "Attendance" : "A"
                                        } ,
                                        {
                                            "date": "29.2.2020",
                                            "Attendance" : "A"
                                        },
                                        {
                                            "date": "24.2.2020",
                                            "Attendance" : "A"
                                        } ,
                                  ] ,
                     },
                ],   

        return Response(content)
 
      
 