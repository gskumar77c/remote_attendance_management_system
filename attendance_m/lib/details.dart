import 'dart:convert';
import 'package:flutter/cupertino.dart';
import 'package:shared_preferences/shared_preferences.dart';


class DetailScreen1 extends StatefulWidget {
  String student_id="";
  String subject_id="";
  DetailScreen1(this.subject_id,this.student_id);
  @override
  StudentDetailPage createState() => StudentDetailPage( subject_id,student_id);  
}

class DetailScreen2 extends StatefulWidget {
  @override
  ClassDetailPage createState() => ClassDetailPage();  
}
///////////////////////////
class StudentDetailPage extends State<DetailScreen1> {
    String student_id="";     
    String subject_id="";     
    SharedPreferences sharedPreferences;   
    StudentDetailPage( this.subject_id,this.student_id)
    {
      // _getStudentDetails(this.subject_id,this.student_id);
    }

  //   _getStudentDetails(String student_id)async{
  //     String url_data = 'http://192.168.43.178:8080/teacher_profile/' ;
  //     var credentials ={ 'Authorization': ('Token '+ sharedPreferences.getString('token')), };
  //     var response2 = await http.post(url_data , headers: credentials);
  //     var jsonResponse;
  //     if(response2.statusCode == 200) { 
  //         jsonResponse = json.decode(response2.body);
  //         if(jsonResponse != null) {  
  //             print(jsonResponse[0]["message"]);
  //             teacher_details.name= jsonResponse[1]["name"];
  //             teacher_details.id= jsonResponse[2]["id"];              
  //             List<subject_wise_detail> subj_detail_list = new List<subject_wise_detail>() ;
  //             var subj_list= jsonResponse[3]["detail"];
              
  //             for (var item in subj_list ) {
  //                   List<student_class>  stud_list = new List<student_class> ();
  //                   for (var entry in item["students_list"]) {
  //                         stud_list.add( student_class( entry["student_name"],entry["student_id"] ) );
  //                   }
  //                   subj_detail_list.add( subject_wise_detail(item["subject_name"],item["subject_id"], stud_list) );
  //             }
              
  //             teacher_details.subject_detail_list = subj_detail_list;
  //         }
  //     }
  //     else { 
  //       print(response2.body);
  //     }
  // }

  @override 
  Widget build(BuildContext context) {
     
    throw UnimplementedError();
  }
}


/////////////////////////

class ClassDetailPage extends State<DetailScreen2> {
  @override
 
 
 
  Widget build(BuildContext context) {
   
    throw UnimplementedError();
  }
}