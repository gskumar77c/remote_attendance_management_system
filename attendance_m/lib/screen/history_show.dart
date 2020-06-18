import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import '../main.dart';
import 'details.dart';
import '../component/jason_prac.dart';
import '../component/general_classes.dart';
import '../model/historyModel.dart';

class HistoryScreen extends StatefulWidget {
  @override
  _LandingScreenState createState() => _LandingScreenState();
}

class _LandingScreenState extends State<HistoryScreen> {
  @override
  void initState() {
    super.initState();
  }

  _LandingScreenState() {
    subjectList = new List<Subject>();
    for (var item in TeacherDetails.subjectDetailList) {
      subjectList.add(new Subject(item.subjectId, item.subjectName));
    }
  }

  Future<void> showMessage(BuildContext context) {
    return showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text("Alert"),
            content: SingleChildScrollView(
              child: ListBody(
                children: <Widget>[
                  Text("Message:" + "$message"),
                ],
              ),
            ),
          );
        });
  }

  Future<void> showClassHistory(String subjectId) {
    return showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text("Alert"),
            content: SingleChildScrollView(
              child: ListBody(
                children: <Widget>[
                  Text("Message: Showing Class history"),
                ],
              ),
            ),
          );
        });
  }

  Future<void> showStudentHistory(String subjectId) {
    studentList = new List<StudentClass>();
    print(subjectId);
    for (var item in TeacherDetails.subjectDetailList) {
      if (item.subjectId == subjectId)
        for (var entry in item.studentsList)
          studentList
              .add(new StudentClass(entry.studentId, entry.studentName));
    }

    return showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text("Alert"),
            content: SingleChildScrollView(
              child: ListBody(
                children: <Widget>[
                  Text("Choose Student of course_id ABC"),
                  new DropdownButton<String>(
                    hint: studentId == ""
                        ? Text("Student_id + Name")
                        : Text(studentId),
                    items: studentList.map((StudentClass value) {
                      return new DropdownMenuItem<String>(
                        value: value.studentId,
                        child: new Text(
                            value.studentId + "-" + value.studentName,
                            style: TextStyle(color: Colors.blue)),
                      );
                    }).toList(),
                    onChanged: (String val) {
                      setState(() {
                        studentId = val;
                      });
                      Fluttertoast.showToast(
                          msg: ("$studentId is Selected ,Go BAak!"),
                          toastLength: Toast.LENGTH_SHORT,
                          gravity: ToastGravity.TOP,
                          timeInSecForIos: 1,
                          backgroundColor: Colors.yellow[200],
                          textColor: Colors.blue[700],
                          fontSize: 20.0);
                      // refer to new page
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) =>
                                DetailScreen1(subjectId, studentId)),
                      );
                      print(studentId);
                    },
                  ),
                ],
              ),
            ),
          );
        });
  }

  Widget historySymbol() {
    return Icon(
      Icons.history,
      color: Colors.white,
      size: 40.0,
      semanticLabel: 'History-Section',
    );
  }

  Widget filter() {
    return Column(
      children: <Widget>[
        Padding(
          padding: EdgeInsets.all(20.0),
          child: Row(
            //  mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
            children: [
              Icon(
                Icons.filter_list,
                color: Colors.blue,
                size: 30.0,
                semanticLabel: 'Filter_Section',
              ),
              Text('Apply_Filter',
                  style: TextStyle(fontSize: 15, color: Colors.blue)),
            ],
          ),
        ),
        Padding(
            padding: EdgeInsets.all(2.0),
            child: Container(
              height: 150.0,
              child: Column(
                children: nList
                    .map((data) => RadioListTile(
                          title: Text("${data.type}" + " History"),
                          groupValue: groupId,
                          value: data.index,
                          onChanged: (val) {
                            setState(() {
                              Dates.startDate = null;
                              Dates.endDate = null;
                              radioItemHolder = data.type;
                              groupId = data.index;
                            });
                          },
                          activeColor: Colors.lightBlue,
                        ))
                    .toList(),
              ),
            )),
        Padding(
          padding: EdgeInsets.fromLTRB(25.0, 10.0, 10.0, 2.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Column(
                children: <Widget>[
                  Text("From (Date)", style: TextStyle(fontSize: 15)),
                  SizedBox(
                      width: 170,
                      child: RaisedButton(
                        child: Text(Dates.startDate == null
                            ? "Start-Date"
                            : (Dates.startDate.day).toString() +
                                "/" +
                                (Dates.startDate.month).toString() +
                                "/" +
                                (Dates.startDate.year).toString()),
                        onPressed: () {
                          if (groupId == 2) {
                            showDatePicker(
                                    context: context,
                                    initialDate: DateTime.now(),
                                    firstDate: DateTime(2001),
                                    lastDate: DateTime(2050))
                                .then((date) {
                              setState(() {
                                Dates.startDate = date;
                              });
                            });
                          } else {
                            Fluttertoast.showToast(
                                msg: "Only for limited history",
                                toastLength: Toast.LENGTH_SHORT,
                                gravity: ToastGravity.BOTTOM,
                                timeInSecForIos: 1,
                                backgroundColor: Colors.white,
                                textColor: (Colors.red[700]),
                                fontSize: 18.0);
                          }
                        },
                      ))
                ],
              ),
              Column(
                children: <Widget>[
                  Text("To (Date)"),
                  SizedBox(
                      width: 150,
                      child: RaisedButton(
                        child: Text(Dates.endDate == null
                            ? "End-Date"
                            : (Dates.endDate.day).toString() +
                                "/" +
                                (Dates.endDate.month).toString() +
                                "/" +
                                (Dates.endDate.year).toString()),
                        onPressed: () {
                          if (groupId == 2 && Dates.startDate != null) {
                            showDatePicker(
                                    context: context,
                                    initialDate: Dates.startDate,
                                    firstDate: Dates.startDate,
                                    lastDate: DateTime(2050))
                                .then((date) {
                              setState(() {
                                Dates.endDate = date;
                              });
                            });
                          } else {
                            if (Dates.startDate == null) {
                              message = "First, choose Start Date !";
                            } else {
                              message = "Only for limited History !";
                            }
                            Fluttertoast.showToast(
                                msg: "$message",
                                toastLength: Toast.LENGTH_SHORT,
                                gravity: ToastGravity.BOTTOM,
                                timeInSecForIos: 1,
                                backgroundColor: Colors.white,
                                textColor: (Colors.red[700]),
                                fontSize: 18.0);
                          }
                        },
                      ))
                ],
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget selectSubject() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
      child: Column(children: <Widget>[
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            new Text("Select Subject", style: TextStyle(fontSize: 15)),
            new DropdownButton<String>(
              hint: subjectId == "" ? Text("Subjects") : Text(subjectId),
              items: subjectList.map((Subject sub) {
                return new DropdownMenuItem<String>(
                  value: sub.subId,
                  child: new Text(sub.subName + " (" + sub.subId + ") ",
                      style: TextStyle(color: Colors.blue)),
                );
              }).toList(),
              // items: subject_list ,
              onChanged: (String val) {
                subjectId = val;
                this.setState(() {
                  subjectId = val;
                });
                print(subjectId);
              },
            ),
          ],
        ),
      ]),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Class History'),
        actions: <Widget>[
          historySymbol(),
          FlatButton(
            onPressed: () {
              Navigator.of(context).pushAndRemoveUntil(
                  MaterialPageRoute(
                      builder: (BuildContext context) => MainPage()),
                  (Route<dynamic> route) => false);
            },
            // child: Text("<1>Main", style: TextStyle(color: Colors.white, fontSize: 20),),
            child: Icon(
              Icons.person_pin,
              color: Colors.yellowAccent,
              size: 50.0,
              semanticLabel: 'Profile',
            ),
          ),
        ],
      ),
      body: Container(
        child: Column(
          children: <Widget>[
            Padding(
              // left,top,right,bottom
              padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
              child: selectSubject(),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
              child: filter(),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  RaisedButton(
                    onPressed: () {
                      if (validateEntry())
                        showStudentHistory(subjectId);
                      else
                        showMessage(context);
                    },
                    child: Row(
                      children: [
                        Text("Students-History"),
                        Icon(
                          Icons.person,
                          color: Colors.blue,
                          size: 30.0,
                          semanticLabel: 'History - Section',
                        ),
                      ],
                    ),
                  ),
                  RaisedButton(
                    onPressed: () {
                      if (validateEntry() == false)
                        // show_class_history(subject_id);
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => DetailScreen2(subjectId)),
                        );
                      else
                        showMessage(context);
                    },
                    child: Row(
                      children: [
                        Text("Class-History"),
                        Icon(
                          Icons.group,
                          color: Colors.blue,
                          size: 30.0,
                          semanticLabel: 'History - Section',
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

//  Widget makeRadioTiles() {
//     List<Widget> list = new List<Widget>();

//     for (int i = 0; i < _group.length; i++) {
//       list.add(new RadioListTile(
//         value: _group[i].index,
//         groupValue: _value2,
//         selected: _group[i].selected,
//         onChanged: (val) {
//           setState(() {
//             for (int i = 0; i < _group.length; i++) {
//               _group[i].selected = false;
//             }
//             _value2 = val;
//             _group[i].selected = true;
//           });
//         },
//         activeColor: Colors.purple,
//         controlAffinity: ListTileControlAffinity.trailing,
//         title: new Text(
//           ' ${_group[i].text}',
//           style: TextStyle(
//               color: _group[i].selected ? Colors.black : Colors.grey,
//               fontWeight:
//                   _group[i].selected ? FontWeight.bold : FontWeight.normal),
//         ),
//       ));
//     }
