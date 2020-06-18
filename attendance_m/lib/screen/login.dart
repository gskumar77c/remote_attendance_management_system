import 'package:attendance_marker/main.dart';
import 'package:flutter/material.dart';
import 'home.dart';
import '../model/sms_otp.dart';
import 'dart:convert';  
import 'package:flutter/services.dart'; 
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';   
import 'dart:math';
import '../component/shared_data.dart';

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  
   String _email="";
   FlutterOtp otp= new FlutterOtp();
   String otp_number="";
  String _generated_otp="";
   String password=""; 
   static bool _isLoading = false;
   static  bool _isOTP = false;
    String _enteredOTP = ""; 

 

  @override
  Widget build(BuildContext context) {
    // SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle.light.copyWith(statusBarColor: Colors.transparent));
    return new Scaffold( 

      appBar: AppBar(
        title: Text("       FaceScan :     Login", style: TextStyle(color: Colors.white)), 
      ),

      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
              colors: [Colors.blue, Colors.teal],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter),
        ),
        child: _isLoading ? Center(child: CircularProgressIndicator()) : ListView(
          children: <Widget>[
            _showForm(),
          ],
        ),
      ),
    );
  }

   

  final _formKey = GlobalKey<FormState>();
  final _formKey2 = GlobalKey<FormState>();
  
  Widget _showForm() {
    return new Container(
        padding: EdgeInsets.all(16.0),
        child: new Form(
          key: _formKey,
          child: new ListView(
            shrinkWrap: true,
            children: <Widget>[
              showLogo(),
              showEmailInput(),
              showPasswordInput(1), 
              showPrimaryButton(),
              // buttonSection(),
            ],
          ),
        ));
  }

  String message(String value)
  {
    print("Empty Email address");
    return "Empty";
  }
  String message2(String value)
  {
    print("$value");
    return "Not Empty";
  }

  Widget showEmailInput() { 
    return new Padding(
      padding: const EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 0.0),
      child: new TextFormField(
        maxLines: 1,
        decoration: new InputDecoration(
            hintText: 'Email',
            hintStyle: TextStyle(color: Colors.white),
            icon: new Icon(
              Icons.mail,
              color: Colors.red[400],
            )),
            
        keyboardType: TextInputType.emailAddress,  

        validator: validateEmail,
        onSaved: (String val) {
          print("in onsave of email");
          print("$val");
          _email= val;
        },

      ),
    );
  }
  Widget showMobileOtp() { 
    return new Padding(
      padding: const EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 0.0),
      child: new TextFormField(
        maxLines: 1,
        decoration: new InputDecoration(
            hintText: 'Mobile Number',
            hintStyle: TextStyle(color: Colors.grey),
            icon: new Icon(
              Icons.phone_android,
              color: Colors.blue[900],
            )), 
        keyboardType: TextInputType.phone, 
        onSaved: (String val) { 
          print("$val");
          setState(() {
            otp_number= val;
          });
          
        },

      ),
    );
  }
  

  Widget showOtp() { 
    return new Padding(
      padding: const EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 0.0),
      child: new TextFormField(
        maxLines: 1,
        decoration: new InputDecoration(
            hintText: 'Otp Number',
            hintStyle: TextStyle(color: Colors.grey),
            icon: new Icon(
              Icons.verified_user,
              color: Colors.blue[900],
            )), 
        keyboardType: TextInputType.number, 
        onSaved: (String val) { 
          print("$val");
          setState(() {
            _enteredOTP = val;
          }); 
        }, 
      ),
    );
  }

  Widget showPasswordInput(int password_num) {   

      return new Padding(
        padding: const EdgeInsets.fromLTRB(0.0, 15.0, 0.0, 0.0),
        child: new TextFormField(
          maxLines: 1,
          obscureText: true,
          autofocus: false,
          decoration: new InputDecoration(
              hintText: 'Password',
              hintStyle: TextStyle(color: Colors.white),
              icon: new Icon(
                Icons.lock,
                color: Colors.yellow[200],
              )),

          keyboardType: TextInputType.text, 

          validator: validatePassword,
          onSaved: (String val) {
            password= val;
          },

        ),
      );
  }

 Widget showLogo() {
    return new Hero(
      tag: 'hero',
      child: Padding(
        padding: EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 20.0),
        child: CircleAvatar(
          backgroundColor: Colors.orange[300],
          radius: 130.0, 
          child: Image.asset('assets/iitrpr_logo.jpeg'),
        ),
      ),
    );
  }
 

  String validatePassword(String value) {  
      if (value.length <= 6)
        return 'Password must be of greater that 6 digit size !';
      else
        return null;
  }

  String validateEmail(String value) {
    Pattern pattern =
        r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$';
    RegExp regex = new RegExp(pattern);
    if (!regex.hasMatch(value))
      return 'Enter Valid Email';
    else
      return null;
  }

  List password_verification (String password)
  {
      if (password?.isEmpty ?? true)
        return [false, "Password Required"];
      else if (password.length < 6)
        return [false,"The Password Requires 6 Characters Or More"];
      else
        return [true,"Acceptable Password"];  
  }
  
  void validateAndSubmit(){
    
    // remove later 

    if (_formKey.currentState.validate()) {
      _formKey.currentState.save();
      print('valid');
    } 
    print('Signed in: $_email, with password $password .');  

    if (validateEmail(_email) == null  && password_verification(password)[0]==true )
    {
      setState(() {
        _isLoading = true;
      });
      signIn(_email, password); 
    }
    else if ( validateEmail(_email) != null ) 
          print("Invalid Email Address !!"); 
    else{
        String reason = password_verification (password)[1];
        print("$reason");
      }
    
  }
 


  signIn(String email , String pass) async {
    SharedPreferences sharedPreferences = await SharedPreferences.getInstance();

    var data = 
    {
         'username' : email,
         'password' : pass,
      // 'Authorization': 'Token 88f95c3f76da99c3403e9de1222ab153bee9ecd6', 
    }; 

    String jasonStringLogin = json.encode(data);  
    String url_login = urlApiTokenAuth ;
    var response = await http.post(url_login , body: data);      
    var jsonResponse;
    if(response.statusCode == 200) { 
      jsonResponse = json.decode(response.body); 
      if(jsonResponse != null) {
          setState(() {
            _isLoading = false;
          });         
          sharedPreferences.setString("token", jsonResponse['token']);
          Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => homePage(sharedPreferences)), (Route<dynamic> route) => false);
        }
      }
      else {
        setState(() {
          _isLoading = false;
        });
        print(response.body);
      } 
  }


  Future<void>  show_TandC(){
    return showDialog(context: context, builder:(BuildContext context){
      return AlertDialog(
        title: Text("Terms & condition"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[ Text("This is a attendance management app"), 
            ],
          ),
        ),
      );
    });
  }
  Future<void>  show_forgot_password() async{
    return showDialog(context: context, builder:(BuildContext context){
      return AlertDialog(
        title: Text("Terms & condition"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[ Text("Enter Email Id"), 
            Container(
              padding: EdgeInsets.all(16.0),
              child: new Form(
                key: _formKey2,
                child: new ListView(
                  shrinkWrap: true,
                  children: <Widget>[ 
                    showMobileOtp(), 
                    
                    RaisedButton(
                      elevation: 5.0,
                      shape: new RoundedRectangleBorder(
                          borderRadius: new BorderRadius.circular(30.0)),
                      color: Colors.blue,
                      child: new Text(  'send', style: new TextStyle(fontSize: 20.0, color: Colors.white)),
                      onPressed:(){ 
                         _formKey2.currentState.save();
                             otp.sendOtp(otp_number);  
                      },
                    ), 

                    showOtp() ,

                      RaisedButton(
                      elevation: 5.0,
                      shape: new RoundedRectangleBorder(
                          borderRadius: new BorderRadius.circular(30.0)),
                      color: Colors.blue,
                      child: new Text(  "check" , style: new TextStyle(fontSize: 20.0, color: Colors.white)),
                      onPressed:(){ 
                         _formKey2.currentState.save();
                             if(otp.resultChecker( _enteredOTP)) 
                                 print("otp succesful"); 
                              else
                                print("Retry");  
 
                      },
                    ),
                  ],
                ),
              )),
           ],
          ),
        ),
      );
    });
  }

 
  Widget showPrimaryButton() {
    return new Padding(
        padding: EdgeInsets.fromLTRB(20.0, 25.0, 20.0, 0.0),
        child: SizedBox( 
          child:Column(
            children: <Widget>[
              
                new RaisedButton(
                  elevation: 5.0,
                  shape: new RoundedRectangleBorder(
                      borderRadius: new BorderRadius.circular(30.0)),
                  color: Colors.blue,
                  child: new Text('Login',
                      style: new TextStyle(fontSize: 20.0, color: Colors.white)),
                  onPressed:validateAndSubmit,
                 ),

                MaterialButton(
                  onPressed: show_forgot_password,
                  child: Text("Forgot Password ?",  style: new TextStyle( color: Colors.white)),
                ),
                MaterialButton(
                  onPressed:show_TandC,
                  child: Text("Terms & Conditions ?",   style: new TextStyle( color: Colors.black)),
                ),

             ],
          )   
        ));
  }
}