import 'dart:io';
import 'dart:ui';
import 'package:file_picker/file_picker.dart';

import 'ImageCarousel.dart';   
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:fluttertoast/fluttertoast.dart';
// import 'package:multi_image_picker/multi_image_picker.dart'; 


class shared_list { 
  static List<File> resultList;   
  static add(File value)
  {
    resultList = List<File>();
    resultList.add(value);
  }
}

class LandingScreen extends StatefulWidget {
  @override
  _LandingScreenState createState() => _LandingScreenState();
}

class _LandingScreenState extends State<LandingScreen> with SingleTickerProviderStateMixin {

  Animation<double> animation;
  AnimationController controller;

  initState() {
    super.initState();
    controller = new AnimationController(
        duration: const Duration(milliseconds: 2000), vsync: this);
    animation = new Tween(begin: 0.0, end: 18.0).animate(controller)
      ..addListener(() {
        setState(() {
          // the state that has changed here is the animation object’s value
        });
      });
    controller.forward();
  }

 
  _openGallery(BuildContext context) async { 

      String error; 
      shared_list.resultList= null;

      try {
        // var cam = await MultiImagePicker.pickImages(
        //   maxImages: 10,
        //   enableCamera: true, 
        // ); 
        var cam = await FilePicker.getMultiFile();
        this.setState(() {
          shared_list.resultList = cam; 
        });
      } on Exception catch (e) {
        error = e.toString();
        print(error);
      }
      Navigator.of(context).pop();
  }

  _openCamera(BuildContext context) async{ 
     shared_list.resultList = null;
    File cam = await ImagePicker.pickImage(source: ImageSource.camera);
    this.setState(() { 
       shared_list.add(cam); 
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
    if( shared_list.resultList== null){
      return Icon(
      Icons.add_a_photo,
        color: Colors.pink,
        size: 200.0,
        semanticLabel: 'select an Image',
      );
      //return Text(" No image selected yet.!");
    }
    else { 
           return new Padding(
            padding: EdgeInsets.fromLTRB(30.0, 70.0, 30.0, 0.0),
            child: SizedBox(
              height: 40.0,
              child: new RaisedButton(
                elevation: 5.0,
                shape: new RoundedRectangleBorder(
                    borderRadius: new BorderRadius.circular(30.0)),
                color: Colors.blue,
                child: new Text('Veiw Selected Pics',
                    style: new TextStyle(fontSize: 20.0, color: Colors.white)),
                onPressed: (){
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => ImageCarousel()),
                  );
                  // Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => ImageCarousel()), (Route<dynamic> route) => false);
                },
              ),  
          ));
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
                            msg: ( shared_list.resultList!= null) ? "Image Uploaded and Processing..!" : "Select an Image first.!",
                            toastLength: Toast.LENGTH_SHORT,
                            gravity: ToastGravity.BOTTOM,
                            timeInSecForIos: 1,
                            backgroundColor: Colors.cyanAccent,
                            textColor: Colors.black,
                            fontSize: 16.0
                        );

                        setState(() { 
                          shared_list.resultList = null;
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
// 