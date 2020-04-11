import 'dart:convert';  
import 'package:shared_preferences/shared_preferences.dart';  
import 'package:flutter/material.dart';
import 'home.dart';
import 'login.dart';
import 'jason_prac.dart';

class ProfilePage extends StatefulWidget {
  @override
  _PageState createState() => _PageState();
}

class _PageState extends State<ProfilePage> {
  SharedPreferences sharedPreferences;  
   void initState() {
    super.initState();
    checkLoginStatus(); 
  }
  checkLoginStatus() async {
    sharedPreferences = await SharedPreferences.getInstance();   
  }

  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("FaceScan App", style: TextStyle(color: Colors.white)),
        actions: <Widget>[ 
          FlatButton(
            onPressed: () {              
              Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => Homepage(sharedPreferences)), (Route<dynamic> route) => false);
            },
             child: Icon( Icons.home,  color: Colors.yellowAccent, size: 50.0, semanticLabel: 'Profile', ),
          ),
        ],
      ),

      body: Padding(
        padding: EdgeInsets.fromLTRB(140.0, 10.0, 20.0, 20.0),
        child:  new Row( 
            children: <Widget>[
              Text("Profile",style: TextStyle(color: Colors.blue , fontWeight: FontWeight.bold,fontSize: 30)),
              Icon( Icons.person_pin,  color: Colors.blue, size: 50.0, semanticLabel: 'Profile', ),
              // showLogo(), 
            ],
          ),
        ),

      drawer: Drawer(
                child: ListView(
          children: <Widget>[
            UserAccountsDrawerHeader(
              decoration: BoxDecoration(color: Colors.indigoAccent),
              accountName: Text("${teacher_details.name}"),
              accountEmail: Text("${teacher_details.id}"),
              currentAccountPicture: GestureDetector(
                child: CircleAvatar(
                  child: Text(
                    "AM",
                    style: TextStyle(
                        color: Colors.indigoAccent,
                        fontSize: 20.0,
                        fontWeight: FontWeight.bold),
                  ),
                  backgroundColor: Colors.white,
                ),
              ),
            ),
            InkWell(
              onTap: (){},
              child: ListTile(
                onTap: (){Navigator.popAndPushNamed(context, "/home");},
                leading: Icon(Icons.home, color: Colors.indigoAccent),
                title: Text("Home Page"),
              ),
            ),
            InkWell(
              onTap: null,
              child: ListTile(
                onTap: (){Navigator.popAndPushNamed(context, "/profile");},
                leading: Icon(Icons.person, color: Colors.indigoAccent),
                title: Text("Course Teaching"),
              ),
            ),
            InkWell(
              onTap: null,
              child: ListTile(
                onTap: (){Navigator.pushNamed(context, "/news");},
                leading: Icon(Icons.history, color: Colors.indigoAccent),
                title: Text("History"),
              ),
            ),
            InkWell(
              onTap: null,
              child: ListTile(
                onTap: (){Navigator.pushNamed(context, "/news");},
                leading: Icon(Icons.edit, color: Colors.indigoAccent),
                title: Text("Edit Profile"),
              ),
            ),
            Divider(),
            InkWell(
              onTap: null,
              child: ListTile(
                leading: Icon(Icons.help, color: Colors.indigoAccent),
                title: Text("IT cell"),
              ),
            ),
            InkWell(
              onTap:  (){
                
              sharedPreferences.clear();
              sharedPreferences.commit();
              Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => LoginPage()), (Route<dynamic> route) => false);
            
              },
              child: ListTile(
                leading: Icon(
                  Icons.power_settings_new,
                  color: Colors.indigoAccent,
                ),
                title: Text("Log out"),
              ),
            )
          ],  
                ),
      ),
    );
  }
}