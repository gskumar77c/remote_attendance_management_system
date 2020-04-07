import 'dart:convert';



  //  1

class server_login_response{
  static String token;
  static List<subject_wise_details> detail_list;  
}
 
class subject_wise_details
{
  String subject_name;
  String subject_id;
  List<student_class>    students_list;

  subject_wise_details(this.subject_name, this.subject_id , this. students_list);
}


class student_class
{
   String student_name ;
   String student_id ;

   student_class(this.student_name, this.student_id);
}



///2
  class class_hist_date_wise {
     static List<date_attendance> attendence_list;
  }
  class date_attendance {
    String date;
    String present;
    String total; 

    date_attendance(this.date, this.present, this.total);
  }

  // 3
  class student_hist {
    static String  course_id;
    static String  course_name;
    static String  student_id;
    static String  student_name;
    static List <student_daily_entry> attendence_list; 
  }

  class student_daily_entry {
    DateTime date;
    bool attendance;

    student_daily_entry(this.date, this.attendance);
  }


  class jason_data{
    static   Map<String, dynamic> class_hist= { 
          "subject_name" : "math",
          "subject_id" : "5552165",
          "list_date_wise" : [
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
      };
      
    String jasonString_class_histn = json.encode(class_hist);   
    
    static   Map<String, dynamic>students_hist= {
      "subject_id"  : "5552165"	, 
      "subject_name" : "math"	, 
      "student_id"  : "2017csb1091",
      "student_name": "Nikhil", 
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
    };

    String jasonString_students_hist = json.encode(students_hist); 

      
    static  Map<String, dynamic>login_response =
    {
      "token": "A1A2A2A3D1",
      "subjects_wise_details" : [
          {
            "subject_name" : "math",
            "subject_id" : "5552165",
            "students_list" : [
                  {
                      "student_name": "sibbi",
                      "student_id": "6565656",
                  },
                  {
                      "student_name": "garima",
                      "student_id": "632565",
                  },
                  // ....... so on
                ],
          },
        {
            "subject_name" : "astronomy",
            "subject_id" : "65626",
            "students_list" : [
                  {
                      "student_name": "sibbi",
                      "student_id": "6565656",
                  },
                  {
                      "student_name": "garima",
                      "student_id": "632565",
                  },
                  // ....... so on
                ],
          }, 
          // ........so on
        ],
  
    };

    
  }
