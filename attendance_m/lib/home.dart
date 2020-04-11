// import 'dart:html';

import 'dart:convert';

import 'package:attendance_marker/history_show.dart';
import 'package:attendance_marker/profile.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart'; 
import 'package:http/http.dart' as http;
import 'punch_att.dart';
import 'jason_prac.dart';


class Homepage extends StatefulWidget {
   SharedPreferences sharedPreferences;   
  Homepage(this.sharedPreferences);
  @override
  _HomepageState createState() => _HomepageState(sharedPreferences);
}

class _HomepageState extends State<Homepage> {
 
   SharedPreferences sharedPreferences;   
  _HomepageState(this.sharedPreferences)
  {
    _getTeacherDetails();
  }

  _getTeacherDetails()async{
      String url_data = 'http://192.168.43.178:8080/teacher_profile/' ;
      var credentials ={ 'Authorization': ('Token '+ sharedPreferences.getString('token')), };

      var data ={ 'message': 'hello'};
      var body_data= json.encode(data); 
      var response2 = await http.post(url_data , headers: credentials, body: body_data);
      var jsonResponse;

      if(response2.statusCode == 200) { 
          jsonResponse = json.decode(response2.body);
          if(jsonResponse != null) {  
              print(jsonResponse[0]["message"]);
              teacher_details.name= jsonResponse[1]["name"];
              teacher_details.id= jsonResponse[2]["id"];              
              List<subject_wise_detail> subj_detail_list = new List<subject_wise_detail>() ;
              var subj_list= jsonResponse[3]["detail"];
              
              for (var item in subj_list ) {
                    List<student_class>  stud_list = new List<student_class> ();
                    for (var entry in item["students_list"]) {
                          stud_list.add( student_class( entry["student_name"],entry["student_id"] ) );
                    }
                    subj_detail_list.add( subject_wise_detail(item["subject_name"],item["subject_id"], stud_list) );
              }

              teacher_details.subject_detail_list = subj_detail_list;
          }
      }
      else { 
        print(response2.body);
      }
  }


  Widget showLogo() {
    return new Hero(
      tag: 'hero',
      child: Padding(
        padding: EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 0.0),
        child: CircleAvatar(
          backgroundColor: Colors.cyanAccent,
          radius: 200.0,
          child: Image.asset('assets/iitrpr_logo.jpeg'),
        ),
      ),
    );
  }

  
  Widget history_symbol(){ 
    return Icon(
    Icons.history,
      color: Colors.white,
      size: 40.0,
      semanticLabel: 'History-Section',
    ); 
  }  
// attach_file

  Widget showAttendanceButton() {
    return new Padding(
      padding: EdgeInsets.fromLTRB(20.0, 30.0, 20.0, 10.0),
      child: SizedBox(
        height: 40.0,
        child: new RaisedButton(
          elevation: 5.0,
          shape: new RoundedRectangleBorder(
              borderRadius: new BorderRadius.circular(30.0)),
          color: Colors.blue,
          child: Row(
            children: <Widget>[
              Icon(
                Icons.attachment,
                  color: Colors.white,
                  size: 40.0,
                  semanticLabel: 'History-Section',
                 ), 
              Text('Punch Attendance',
              style: new TextStyle(fontSize: 20.0, color: Colors.white),)
               ],),
          onPressed: (){
                      // _getTeacherDetails();
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => LandingScreen()),
                        );
                    },
            
    )));
  }

  Widget showHistoryButton() {
    return new Padding(
      padding: EdgeInsets.fromLTRB(20.0, 30.0, 20.0, 10.0),
      child: SizedBox(
        height: 40.0,
        child: new RaisedButton(
          elevation: 5.0,
          shape: new RoundedRectangleBorder(
              borderRadius: new BorderRadius.circular(30.0)),
          color: Colors.blue,
          child:  Row(
             mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
            children: <Widget>[
                history_symbol(),
                new Text('History',
                    style: new TextStyle(fontSize: 20.0, color: Colors.white)),],),
          onPressed: (){
            //  _getTeacherDetails();
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => HistoryScreen()),
            );
          },
        ),  
    ));
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
        appBar:new AppBar(
          automaticallyImplyLeading: false,   
          title: Text("Home Page: FaceScan", style: TextStyle(color: Colors.white ,)),
          centerTitle: true,

          actions: <Widget>[
            FlatButton(
              onPressed: () {              
                Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => ProfilePage()), (Route<dynamic> route) => false);
              },
               child: Icon( Icons.person_pin,  color: Colors.yellowAccent, size: 50.0, semanticLabel: 'Profile', ),
            ),
          ],
        ),


        body: Stack(
          children: <Widget>[
            _showForm(),
          ],
        ));
  }

  Widget _showForm() {
    return new Container(
        padding: EdgeInsets.all(16.0),
        child: new Form(
          child: new ListView(
            shrinkWrap: true,
            children: <Widget>[
              showLogo(),
              showAttendanceButton(),
              showHistoryButton(),
            ],
          ),
        ));
  }

}
