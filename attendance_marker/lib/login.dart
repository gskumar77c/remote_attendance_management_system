import 'package:attendance_marker/main.dart';
import 'package:flutter/material.dart';
import 'home.dart';
import 'dart:convert';  
import 'package:flutter/material.dart';
import 'package:flutter/services.dart'; 
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';  
 

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  
   String _email;
   String _password_1;
   String _password_2;
   bool _isLoading = false;

 

  @override
  Widget build(BuildContext context) {
    // SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle.light.copyWith(statusBarColor: Colors.transparent));
    return new Scaffold( 

      appBar: AppBar(
        title: Text("MYNA : login page", style: TextStyle(color: Colors.white)),
        actions: <Widget>[
          FlatButton(
            onPressed: () {              
              Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => MainPage()), (Route<dynamic> route) => false);
            },
            child: Text("<1>Main", style: TextStyle(color: Colors.white, fontSize: 20),),
          ),
        ],
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

  
//  TextEditingController emailController = new TextEditingController();
//  TextEditingController passwordController = new TextEditingController();

  final _formKey = GlobalKey<FormState>();
  
  Widget _showForm() {
    return new Container(
        padding: EdgeInsets.all(16.0),
        child: new Form(
          key: _formKey,
          child: new ListView(
            shrinkWrap: true,
            children: <Widget>[
              // showLogo(),
              showEmailInput(),
              showPasswordInput(1),
              showPasswordInput(2),
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

  Widget showPasswordInput(int password_num) {  
    if(password_num ==1)

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
            _password_1= val;
          },

        ),
      );

    else  

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
              _password_2= val;
            },
          ),
        );
  }

 Widget showLogo() {
    return new Hero(
      tag: 'hero',
      child: Padding(
        padding: EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 0.0),
        child: CircleAvatar(
          backgroundColor: Colors.orange[300],
          radius: 150.0, 
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
  

  List match_password (String password_1, String password_2)
  {
      if (password_verification(password_1)[0] ==  true && password_verification(password_2)[0] ==  true ){
        if (password_1 == password_2)
          return [true, "Acceptable Password"];
        else 
          return [false,"non-matching passwords !! "]; 
      }
      else if( password_verification(password_1)[0] ==  false ){
        String reason = password_verification(password_1)[1];
        return [false,  reason];
      }
      else{
        String reason = password_verification(password_2)[1];
        return [false,  reason];
      }

  }

  void validateAndSubmit(){
    if (_formKey.currentState.validate()) {
      _formKey.currentState.save();
      print('valid');
    }

    String userId = _email;
    print('Signed in: $userId, with password $_password_1 .');

    if (validateEmail(_email) == null  && match_password (_password_1, _password_2)[0] == true )
    {
      setState(() {
        _isLoading = true;
      });
      signIn(_email, _password_1); 
    }
    else{
        if ( validateEmail(_email) != null ){
          print("Invalid Email Address !!");
        }
      else{
          String reason = match_password (_password_1, _password_2)[1];
          print("$reason");
        }
    } 
  }
 


  signIn(String email , String pass) async {
    SharedPreferences sharedPreferences = await SharedPreferences.getInstance();
    Map<String, dynamic> data = {
      'email': email,
      'password': pass
    };
    
    String jasonStringLogin = json.encode(data); 
    Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => Homepage()), (Route<dynamic> route) => false);

    // String url_login = "http://127.0.0.1:8000/login/" ;
    // var response = await http.post(url_login , body: jasonStringLogin);
    
    
    // var jsonResponse;
    // if(response.statusCode == 200) {
    //   jsonResponse = json.decode(response.body);

    //   if(jsonResponse != null) {
    //     setState(() {
    //       _isLoading = false;
    //     });
    //     sharedPreferences.setString("token", jsonResponse['token']);
    //     Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => Homepage()), (Route<dynamic> route) => false);
    //   }
    // }
    // else {
    //   setState(() {
    //     _isLoading = false;
    //   });
    //   print(response.body);
    // }
  }




  Widget showPrimaryButton() {
    return new Padding(
        padding: EdgeInsets.fromLTRB(40.0, 45.0, 40.0, 0.0),
        child: SizedBox(
          height: 40.0,
          child: new RaisedButton(
            elevation: 5.0,
            shape: new RoundedRectangleBorder(
                borderRadius: new BorderRadius.circular(30.0)),
            color: Colors.blue,
            child: new Text('Login',
                style: new TextStyle(fontSize: 20.0, color: Colors.white)),
            onPressed: validateAndSubmit,
          ),  
        ));
  }
}