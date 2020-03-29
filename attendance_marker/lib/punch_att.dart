import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:fluttertoast/fluttertoast.dart';

class LandingScreen extends StatefulWidget {
  @override
  _LandingScreenState createState() => _LandingScreenState();
}

class _LandingScreenState extends State<LandingScreen> {

  File imageFile;
  _openGallery(BuildContext context) async{
    var picture = await ImagePicker.pickImage(source: ImageSource.gallery);
    this.setState(() {
      imageFile = picture;
    });
    Navigator.of(context).pop();
  }

  _openCamera(BuildContext context) async{
    var cam = await ImagePicker.pickImage(source: ImageSource.camera);
    this.setState(() {
      imageFile = cam;
    });
    Navigator.of(context).pop();
  }


  Future<void> _showChoiceDialog(BuildContext context){
    return showDialog(context: context, builder:(BuildContext context){
      return AlertDialog(
        title: Text("Make a Choice"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[
              GestureDetector(
                child: Text("Gallery"),
                onTap: (){
                  _openGallery(context);
                },
              ),
              Padding(padding: EdgeInsets.all(8.0)),
              GestureDetector(
                child: Text("Camera"),
                onTap: () {
                  _openCamera(context);
                },
              )
            ],
          ),
        ),
      );
    });
  }

  Widget _decideImageView(){
    if(imageFile == null){
      return Icon(
      Icons.add_a_photo,
        color: Colors.pink,
        size: 200.0,
        semanticLabel: 'select an Image',
      );
      //return Text(" No image selected yet.!");
    }
    else {
      return Image.file(imageFile, width: 400, height: 400);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Upload Image For Marking'
        ),
      ),
      body: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              _decideImageView(),

              Padding(
                padding: const EdgeInsets.fromLTRB(10.0, 20.0, 10.0, 70.0),
                child: Row(
                  mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
                  children: <Widget>[
                    RaisedButton(
                      onPressed: () {
                        _showChoiceDialog(context);
                      },
                      child: Text("Select Image"),
                    ),

                    RaisedButton(
                      onPressed: () {
                        Fluttertoast.showToast(
                            msg: imageFile !=null ? "Attendance Marked..!" : "Select an Image first.!",
                            toastLength: Toast.LENGTH_SHORT,
                            gravity: ToastGravity.BOTTOM,
                            timeInSecForIos: 1,
                            backgroundColor: Colors.cyanAccent,
                            textColor: Colors.black,
                            fontSize: 16.0
                        );
                        setState(() {
                          imageFile = null;
                        });
                      },
                      child: Text("Send for Marking"),
                    ),
                  ],
                ),
              )
            ],  
          ),
      ),
    );
  }
}