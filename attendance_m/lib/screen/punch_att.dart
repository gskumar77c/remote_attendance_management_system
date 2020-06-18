import 'dart:convert';
import 'dart:io';
import 'dart:ui';
import 'package:async/async.dart';
import 'package:path/path.dart' as Path;
import 'package:archive/archive_io.dart';
import 'package:file_picker/file_picker.dart';
import 'package:path_provider/path_provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'ImageCarousel.dart';
import '../component/jason_prac.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;
import 'profile.dart';
import '../component/shared_data.dart';
import '../model/actionsBeforeApiCall.dart';

class LandingScreen extends StatefulWidget {
  @override
  _LandingScreenState createState() => _LandingScreenState();
}

class _LandingScreenState extends State<LandingScreen>
    with SingleTickerProviderStateMixin {
  Animation<double> animation;
  AnimationController controller;
  String choosed_subject_id = "";
  List<Subject> subject_list;

  reset() {
    SharedList.resultList = null;
  }

  _LandingScreenState() {
    subject_list = new List<Subject>();
    for (var item in TeacherDetails.subjectDetailList) {
      subject_list.add(new Subject(item.subjectId, item.subjectName));
    }
  }

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
    SharedList.resultList = null;

    try {
      // var cam = await MultiImagePicker.pickImages(
      //   maxImages: 10,
      //   enableCamera: true,
      // );
      var cam = await FilePicker.getMultiFile();
      print(cam[0].path);
      this.setState(() {
        SharedList.resultList = cam;
      });
    } on Exception catch (e) {
      error = e.toString();
      print(error);
    }
    Navigator.of(context).pop();
  }

  _openCamera(BuildContext context) async {
    SharedList.resultList = null;
    File cam = await ImagePicker.pickImage(source: ImageSource.camera);
    this.setState(() {
      SharedList.add(cam);
    });
    Navigator.of(context).pop();
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
              hint: choosed_subject_id == ""
                  ? Text("Subjects")
                  : Text(choosed_subject_id),
              items: subject_list.map((Subject sub) {
                return new DropdownMenuItem<String>(
                  value: sub.subId,
                  child: new Text(sub.subName + " (" + sub.subId + ") ",
                      style: TextStyle(color: Colors.blue)),
                );
              }).toList(),
              // items: subject_list ,
              onChanged: (String val) {
                choosed_subject_id = val;
                this.setState(() {
                  this.choosed_subject_id = val;
                });
                print(choosed_subject_id);
              },
            ),
          ],
        ),
      ]),
    );
  }

  Future<void> _showChoiceDialog(BuildContext context) {
    return showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text("Make a Choice"),
            content: SingleChildScrollView(
              child: ListBody(
                children: <Widget>[
                  GestureDetector(
                    child: Text("Gallery"),
                    onTap: () {
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

  Widget _decideImageView() {
    if (SharedList.resultList == null) {
      return Icon(
        Icons.add_a_photo,
        color: Colors.pink,
        size: 50.0,
        semanticLabel: 'select an Image',
      );
      //return Text(" No image selected yet.!");
    } else {
      return new Padding(
          padding: EdgeInsets.fromLTRB(30.0, 40.0, 30.0, 0.0),
          child: SizedBox(
            height: 40.0,
            child: new RaisedButton(
              elevation: 5.0,
              shape: new RoundedRectangleBorder(
                  borderRadius: new BorderRadius.circular(30.0)),
              color: Colors.blue,
              child: new Text('Veiw Selected Pics',
                  style: new TextStyle(fontSize: 20.0, color: Colors.white)),
              onPressed: () {
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
        title: Text('     Images  Upload'),
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
      body: Container(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            _decideImageView(),
            selectSubject(),
            Padding(
              padding: const EdgeInsets.fromLTRB(10.0, 20.0, 10.0, 30.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  RaisedButton(
                    onPressed: () {
                      _showChoiceDialog(context);
                    },
                    child: Text("Select Image"),
                  ),
                  RaisedButton(
                    onPressed: () async {
                      if (SharedList.resultList != null) _sendImage();

                      Fluttertoast.showToast(
                          msg: (SharedList.resultList != null)
                              ? "Image Uploaded and Processing..!"
                              : "Select an Image first.!",
                          toastLength: Toast.LENGTH_SHORT,
                          gravity: ToastGravity.BOTTOM,
                          timeInSecForIos: 1,
                          backgroundColor: Colors.yellow[200],
                          textColor: (SharedList.resultList != null)
                              ? Colors.green[700]
                              : Colors.red[700],
                          fontSize: 18.0);
                      setState(() {});
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

  _sendImage() async {
    SharedPreferences sharedPreferences = await SharedPreferences.getInstance();
    Map<String, String> headers = {
      'Authorization': ('Token ' + sharedPreferences.getString('token')),
    };
    Uri uri = Uri.parse("http://192.168.43.178:8080/images_upload/");
    http.MultipartRequest request = new http.MultipartRequest('POST', uri);
    request.headers.addAll(headers);

    for (var imageFile in SharedList.resultList) {
      var stream =
          new http.ByteStream(DelegatingStream.typed(imageFile.openRead()));
      var length = await imageFile.length();
      request.files.add(new http.MultipartFile(
          Path.basename(imageFile.path), stream, length,
          filename: Path.basename(imageFile.path)));
    }

    var response = await request.send();

    if (response.statusCode == 204) {
      print("Images successfully uploaded");
      setState(() {
        SharedList.resultList = null;
      });
    }
    response.stream.transform(utf8.decoder).listen((value) {
      print(value);
    });
  }
}
//
