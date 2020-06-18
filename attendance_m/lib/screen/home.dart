// import 'dart:html';
import 'history_show.dart';
import 'file:///D:/Software_Engineering/attendance_m/lib/screen/profile.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'punch_att.dart';
import '../model/actionsBeforeApiCall.dart';

// ignore: must_be_immutable, camel_case_types
class homePage extends StatefulWidget {
  SharedPreferences sharedPreferences;

  homePage(this.sharedPreferences);

  @override
  _homePageState createState() => _homePageState(sharedPreferences);
}

// ignore: camel_case_types
class _homePageState extends State<homePage> {
  SharedPreferences sharedPreferences;

  _homePageState(this.sharedPreferences) {
    getTeacherDetails(sharedPreferences);
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

  // ignore: non_constant_identifier_names
  Widget history_symbol() {
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
                  Text(
                    'Punch Attendance',
                    style: new TextStyle(fontSize: 20.0, color: Colors.white),
                  )
                ],
              ),
              onPressed: () {
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
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                history_symbol(),
                new Text('History',
                    style: new TextStyle(fontSize: 20.0, color: Colors.white)),
              ],
            ),
            onPressed: () {
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
        appBar: new AppBar(
          automaticallyImplyLeading: false,
          title: Text("Home Page: FaceScan",
              style: TextStyle(
                color: Colors.white,
              )),
          centerTitle: true,
          actions: <Widget>[
            FlatButton(
              onPressed: () {
                Navigator.of(context).pushAndRemoveUntil(
                    MaterialPageRoute(
                        builder: (BuildContext context) => ProfilePage()),
                    (Route<dynamic> route) => false);
              },
              child: Icon(
                Icons.person_pin,
                color: Colors.yellowAccent,
                size: 50.0,
                semanticLabel: 'Profile',
              ),
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
