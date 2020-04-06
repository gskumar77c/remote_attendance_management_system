import 'dart:convert';

class jason_data{

  static   Map<String, dynamic> class_his= { 
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
    
String jasonStringLogin = json.encode(class_his); 


  
  
  
// static   Map<String, dynamic>students_his= {
// 	"subject_id" : "nihil"	, 
// 	"student_name": "2017csb1091"

// 	"list" : [
// 		{
// 			"date": "27.2.2020"
// 			"Attendance" : "P"
// 		}
// 		{
// 			"date": "26.2.2020",
// 			"Attendance" : "A"
// 		} 
// 	] 
// }

  
}
