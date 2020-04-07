import 'package:flutter/material.dart';  
import 'package:fluttertoast/fluttertoast.dart';
import 'main.dart';
import 'details.dart';
import 'jason_prac.dart';

 

class HistoryScreen extends StatefulWidget {
  @override
  _LandingScreenState createState() => _LandingScreenState();
}

class _LandingScreenState extends State<HistoryScreen> {

  String  subject_id="";
  String  student_id="";
  String  message= ""; 
  var studentsList = new List<student_class>(); 

  @override
  void initState() {
    super.initState();
    studentsList.add(student_class("Raj","123456")); 
    studentsList.add(student_class("Raj2","123756")); 
    studentsList.add(student_class("Raj3","125456")); 
    studentsList.add(student_class("Raj4","12756")); 
    studentsList.add(student_class("Raj5","129456")); 
    studentsList.add(student_class("Raj6","128456")); 
  } 
 

  // Default Radio Button Selected Item.
  String radioItemHolder = 'All';
  // Group Value for Radio Button.
  int group_id = 1;

  List<NumberList> nList = [
    NumberList(
      index: 1,
      type: "All",
    ),
    NumberList(
      index: 2,
      type: "Limited",
    ), 
  ];


  Future<void> show_message(BuildContext context){
    return showDialog(context: context, builder:(BuildContext context){
      return AlertDialog(
        title: Text("Alert"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[ Text("Message:"+ "$message"), 
            ],
          ),
        ),
      );
    });
  }

  Widget history_symbol(){ 
      return Icon(
      Icons.history,
        color: Colors.white,
        size: 40.0,
        semanticLabel: 'History-Section',
      ); 
    }  

  Widget filter()
  {
      return Column(
        children: <Widget>[   

           Padding(
            padding : EdgeInsets.all(20.0),
            child:  Row(
              //  mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
                        children : [
                          Icon(
                              Icons.filter_list,
                              color: Colors.blue,
                              size: 30.0,
                              semanticLabel: 'Filter_Section',
                            ),
                          Text('Apply_Filter', style: TextStyle(fontSize: 15, color: Colors.blue)),
                        ],
                       ),   
              ),

           Padding(
            padding : EdgeInsets.all(2.0), 
            child: Container( 
            height: 150.0,
            child: Column(
              children: 
                nList.map((data) => RadioListTile ( 
                  title: Text("${data.type}" + " History"), 
                  groupValue: group_id,
                  value: data.index,
                  onChanged: (val) {
                    setState(() {
                      dates.start_date=null;
                      dates.end_date=null;
                      radioItemHolder = data.type ;
                      group_id = data.index;
                    });
                  },
                  activeColor: Colors.lightBlue,
                )).toList(),
            ),
          )),

          Padding(
            padding : EdgeInsets.fromLTRB(25.0, 10.0, 10.0, 2.0),

            child: Row(
                      mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
                      children :<Widget>[ 

                        Column(
                          children: <Widget>[
                                Text("From (Date)",style: TextStyle(fontSize: 15)),
                                 SizedBox(
                                  width: 170,  
                                  child: RaisedButton(
                                    child: Text( dates.start_date== null  ?  "Start-Date" : (dates.start_date.day).toString() + "/"+
                                                                                               (dates.start_date.month).toString() + "/"+
                                                                                              (dates.start_date.year).toString() ),
                                    onPressed: (){ 
                                      if(group_id == 2){
                                        showDatePicker(context: context, 
                                            initialDate: DateTime.now(),
                                            firstDate: DateTime(2001),
                                            lastDate: DateTime(2050)
                                        ).then((date){
                                          setState(() {
                                            dates.start_date= date;
                                          });
                                        });
                                      }
                                      else{
                                        
                                        Fluttertoast.showToast(
                                        msg:   "Only for limited history"  ,
                                        toastLength: Toast.LENGTH_SHORT,
                                        gravity: ToastGravity.BOTTOM,
                                        timeInSecForIos: 1,
                                        backgroundColor: Colors.white,
                                        textColor: ( Colors.red[700]),
                                        fontSize: 18.0 );
                                      }
                                  },
                                )
                              )
                            ],
                          ),

                         Column(
                          children: <Widget>[
                                Text("To (Date)"),
                                SizedBox(
                                  width: 150,  
                                  child: RaisedButton(
                                    child: Text( dates.end_date == null  ?  "End-Date" : (dates.end_date.day).toString() + "/"+
                                                                                               (dates.end_date.month).toString() + "/"+
                                                                                              (dates.end_date.year).toString() ),
                                    onPressed: (){ 
                                      if(group_id == 2 && dates.start_date != null){
                                        showDatePicker(context: context, 
                                            initialDate: dates.start_date,
                                            firstDate: dates.start_date,
                                            lastDate: DateTime(2050)
                                        ).then((date){
                                          setState(() {
                                            dates.end_date= date;
                                          });
                                        });
                                      }
                                      else{
                                        if (dates.start_date == null ) {
                                          message= "First, choose Start Date !";
                                        } else {
                                          message= "Only for limited History !";                                          
                                        }
                                        Fluttertoast.showToast(
                                        msg:  "$message"  ,
                                        toastLength: Toast.LENGTH_SHORT,
                                        gravity: ToastGravity.BOTTOM,
                                        timeInSecForIos: 1,
                                        backgroundColor: Colors.white,
                                        textColor: ( Colors.red[700]),
                                        fontSize: 18.0 );
                                      }
                                  },
                                )
                                )
                            ],
                          ),

                      ],
                  ),   
              ),
        ],
        
    );
  }


  
  Widget select_subject(){ 
    return Padding(
                padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
                child:Column(
                    children:<Widget>[ 
                      Row(
                        mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
                        children: <Widget>[ 
                          new Text(subject_id=="" ? "Select Subject": subject_id , style: TextStyle(fontSize: 15)),
                          new DropdownButton<String>(
                                hint: Text( "Subjects"), 
                                items: <String>['subject-A', 'subject-B', 'subject-C', 'subject-D'].map((String value) {
                                  return new DropdownMenuItem<String>(
                                    value: value,
                                    child: new Text(value, style: TextStyle(color: Colors.blue)),
                                  );
                                }).toList(),
                                onChanged: (String val) {  
                                    subject_id = val; 
                                    print(subject_id);
                                },
                        ),
                      ],
                    ), 
                ]
        ),
    );
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Class History'
        ), 
        actions: <Widget>[
        history_symbol(),
        FlatButton(
          onPressed: () {              
            Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => MainPage()), (Route<dynamic> route) => false);
          },
          // child: Text("<1>Main", style: TextStyle(color: Colors.white, fontSize: 20),),
          child: Icon( Icons.home,  color: Colors.yellow, size: 50.0, semanticLabel: 'Main', ),
        ),
      ],
      ),   
      
      body: Container(
          child: Column( 
            children: <Widget>[ 
              Padding(
                // left,top,right,bottom
                padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
                child: select_subject(),
              ),
              Padding(
                padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
                child: filter(),
              ),
               
              Padding(
                padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
                child: Row(
                  mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
                  children: <Widget>[
                    RaisedButton(
                      onPressed: () {
                        if(validate_entry()== false)
                          show_student_history(subject_id);
                        else
                            show_message(context);
                      },
                      child: Row(
                          children : [
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
                      onPressed:() {
                        if(validate_entry()== false)
                          // show_class_history(subject_id); 
                           Navigator.push(
                              context,
                              MaterialPageRoute(builder: (context) => DetailScreen2()),
                            );  
                        else
                            show_message(context);
                      },
                      child:  Row(
                        children : [
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


  bool validate_entry()
  {
     if (subject_id != "") {
       if (group_id==2 && (dates.start_date==null || dates.end_date== null) ) { 
            message ="select start and end date, both !";
            return false;
        } else {
            return true;
       }
     } else {
            message ="select a subject, both !";
            return false; 
     }
  }
   
  Future<void>  show_class_history( String  subject_id  ){
    return showDialog(context: context, builder:(BuildContext context){
      return AlertDialog(
        title: Text("Alert"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[ Text("Message: Showing Class history"), 
            ],
          ),
        ),
      );
    });
  }
  
  Future<void> show_student_history( String  subject_id  ){
    return showDialog(context: context, builder:(BuildContext context){
      return AlertDialog(
        title: Text("Alert"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[ Text("Choose Student of course_id ABC"),
              new DropdownButton<String>(
                                hint: Text( "Student_id + Name"), 
                                items: studentsList.map((student_class value) {
                                  return new DropdownMenuItem<String>(
                                    value: value.student_id,
                                    child: new Text(value.student_id +"-" + value.student_name , style: TextStyle(color: Colors.blue)),
                                  );
                                }).toList(),
                                onChanged: (String val) {  
                                    student_id = val; 
                                    Fluttertoast.showToast(
                                        msg: ("$student_id is Selected ,Go BAak!"),
                                        toastLength: Toast.LENGTH_SHORT,
                                        gravity: ToastGravity.TOP,
                                        timeInSecForIos: 1,
                                        backgroundColor: Colors.yellow[200],
                                        textColor: Colors.blue[700],
                                        fontSize: 20.0
                                    );
                                    // refer to new page
                                     Navigator.push(
                                          context,
                                          MaterialPageRoute(builder: (context) => DetailScreen1()),
                                        );
                                      print(student_id);
                                },
                        ),

            ],
          ),
        ),
      );
    });
  }

}

class dates{
  static DateTime start_date;
  static DateTime end_date; 
}

class NumberList {
  String type;
  int index;
  NumberList({this.type, this.index});  

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




