import 'dart:convert';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:http/http.dart' as http;
import '../component/jason_prac.dart';
import '../model/actionsBeforeApiCall.dart';

class DetailScreen1 extends StatefulWidget {
  String student_id = "";
  String subject_id = "";

  DetailScreen1(this.subject_id, this.student_id);

  @override
  StudentDetailPage createState() => StudentDetailPage(subject_id, student_id);
}

class DetailScreen2 extends StatefulWidget {
  String subject_id = "";

  DetailScreen2(this.subject_id);

  @override
  ClassDetailPage createState() => ClassDetailPage(this.subject_id);
}

///////////////////////////
class StudentDetailPage extends State<DetailScreen1> {
  String _studentId = "";
  String _subjectId = "";
  bool _isLoading = false;
  SharedPreferences sharedPreferences;
  var _widgetList = List<Widget>();

  StudentDetailPage(this._subjectId, this._studentId) {
    getStudentDetails(this._subjectId, this._studentId);

    // for (var item in student_hist.attendence_list) {
    //     widget_list.add(Row(
    //       children: <Widget>[
    //         Text((item.date.day).toString()+"/"+(item.date.month).toString()+"/"+(item.date.year).toString()),
    //         Text(item.slot),
    //         Text(item.extra_class),
    //         Text(item.attendance),
    //       ],
    //     )
    //     );
    //   }
  }

  @override
  Widget build(BuildContext context) {
    // SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle.light.copyWith(statusBarColor: Colors.transparent));

    return new Scaffold(
      appBar: AppBar(
        title: Text("       FaceScan :    Students History",
            style: TextStyle(color: Colors.white)),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
              colors: [Colors.blue, Colors.teal],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter),
        ),
        child: _isLoading
            ? Center(child: CircularProgressIndicator())
            : ListView(
                children: <Widget>[
                  // Text(student_hist.student_id),
                  // Text(student_hist.student_name),
                  // Text(student_hist.course_id),
                  // Text(student_hist.course_name),
                  // Column(children: widget_list,),
                  // _showSludentList(),
                ],
              ),
      ),
    );
  }
}

/////////////////////////

class ClassDetailPage extends State<DetailScreen2> {
  String subject_id = "";
  bool _isLoading = false;
  SharedPreferences sharedPreferences;

  ClassDetailPage(this.subject_id) {
    getClassDetails(this.subject_id, sharedPreferences);
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: AppBar(
        title: Text("       FaceScan :    Class History",
            style: TextStyle(color: Colors.white)),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
              colors: [Colors.blue, Colors.teal],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter),
        ),
        child: _isLoading
            ? Center(child: CircularProgressIndicator())
            : ListView(
                children: <Widget>[
                  // _showclassList(),
                ],
              ),
      ),
    );
  }
}
