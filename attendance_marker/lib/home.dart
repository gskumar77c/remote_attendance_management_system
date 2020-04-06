// import 'dart:html';

import 'package:attendance_marker/history_show.dart';
import 'package:attendance_marker/main.dart';
import 'package:flutter/material.dart';
import 'punch_att.dart';

class Homepage extends StatefulWidget {
  @override
  _HomepageState createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {

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

  Widget showAttendanceButton() {
    return new Padding(
      padding: EdgeInsets.fromLTRB(30.0, 70.0, 30.0, 0.0),
      child: SizedBox(
        height: 40.0,
        child: new RaisedButton(
          elevation: 5.0,
          shape: new RoundedRectangleBorder(
              borderRadius: new BorderRadius.circular(30.0)),
          color: Colors.blue,
          child: new Text('Punch Attendance',
              style: new TextStyle(fontSize: 20.0, color: Colors.white)),
          onPressed: (){
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => LandingScreen()),
            );
          },
        ),  
    ));
  }

  Widget showHistoryButton() {
    return new Padding(
      padding: EdgeInsets.fromLTRB(30.0, 70.0, 30.0, 0.0),
      child: SizedBox(
        height: 40.0,
        child: new RaisedButton(
          elevation: 5.0,
          shape: new RoundedRectangleBorder(
              borderRadius: new BorderRadius.circular(30.0)),
          color: Colors.blue,
          child: new Text('History',
              style: new TextStyle(fontSize: 20.0, color: Colors.white)),
          onPressed: (){
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
          title: Text("MYNA APP", style: TextStyle(color: Colors.white)),
          centerTitle: true,

          actions: <Widget>[
            FlatButton(
              onPressed: () {              
                Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => MainPage()), (Route<dynamic> route) => false);
              },
              child: Text("<1> Main", style: TextStyle(color: Colors.white, fontSize: 20)),
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
