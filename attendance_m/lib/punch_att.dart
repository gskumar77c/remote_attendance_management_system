import 'dart:convert';
import 'dart:io';
import 'dart:ui';
import 'package:archive/archive_io.dart';
import 'package:file_picker/file_picker.dart';
import 'package:http_parser/http_parser.dart';
import 'package:path_provider/path_provider.dart';
import 'package:shared_preferences/shared_preferences.dart'; 
import 'ImageCarousel.dart';   
import 'jason_prac.dart';   
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart'; 
import 'profile.dart';
import 'package:mime/mime.dart';
import 'package:archive/archive.dart';
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
  String  choosed_subject_id="";
  List<subject> subject_list ;

  reset()
  {
      shared_list.resultList = null;
  }
  _LandingScreenState()
  {
    subject_list = new List<subject> ();    
    for (var item in teacher_details.subject_detail_list) {
      subject_list.add( new subject(item.subject_id , item.subject_name) );
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
      shared_list.resultList= null;

      try {
        // var cam = await MultiImagePicker.pickImages(
        //   maxImages: 10,
        //   enableCamera: true, 
        // ); 
        var cam = await FilePicker.getMultiFile();
        print(cam[0].path);
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

  
  Widget select_subject(){ 
    return Padding(
                padding: const EdgeInsets.fromLTRB(2.0, 2.0, 2.0, 2.0),
                child:Column(
                    children:<Widget>[ 
                      Row(
                        mainAxisAlignment:  MainAxisAlignment.spaceEvenly,
                        children: <Widget>[ 
                          new Text( "Select Subject", style: TextStyle(fontSize: 15)),
                          
                          new DropdownButton<String>(
                                hint: choosed_subject_id == "" ? Text( "Subjects") : Text(choosed_subject_id), 
                                items:  subject_list.map((subject sub) {
                                  return new DropdownMenuItem<String>(
                                    value: sub.sub_id,
                                    child: new Text(sub.sub_name + " ("+ sub.sub_id + ") ", style: TextStyle(color: Colors.blue)),
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
                ]
        ),
    );
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
        size: 50.0,
        semanticLabel: 'select an Image',
      );
      //return Text(" No image selected yet.!");
    }
    else { 
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
          '     Images  Upload'
        ),
        actions: <Widget>[
            FlatButton(
              onPressed: () {              
                Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (BuildContext context) => ProfilePage()), (Route<dynamic> route) => false);
              },
                child: Icon( Icons.person_pin,  color: Colors.yellowAccent, size: 50.0, semanticLabel: 'Profile', ),
            ),
         ],
      ),
      body: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              _decideImageView(),
              select_subject(),

              Padding(
                padding: const EdgeInsets.fromLTRB(10.0, 20.0, 10.0, 30.0),
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
                      onPressed: ()async{
                        
                        _asyncFileUpload();
                        Fluttertoast.showToast(
                            msg: ( shared_list.resultList!= null) ? "Image Uploaded and Processing..!" : "Select an Image first.!",
                            toastLength: Toast.LENGTH_SHORT,
                            gravity: ToastGravity.BOTTOM,
                            timeInSecForIos: 1,
                            backgroundColor: Colors.yellow[200],
                            textColor: ( shared_list.resultList!= null) ?Colors.green[700] : Colors.red[700],
                            fontSize: 18.0
                        ); 
                        setState(()  {  
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


_formZip()async{
      Directory appDocDirectory = await getExternalStorageDirectory();
      var encoder = ZipFileEncoder();
      var _path = appDocDirectory.path+"/"+'jay.zip';
      encoder.create(_path);
      for (var item in shared_list.resultList)  
          encoder.addFile(item);
      encoder.close();
      return _path;
}


_asyncFileUpload() async {
    String imagePath= shared_list.resultList[0].path;
    print(shared_list.resultList[0].path);
    //create multipart request for POST or PATCH method
     SharedPreferences sharedPreferences = await SharedPreferences.getInstance(); 
      Map<String, String> headers ={ 'Authorization': ('Token '+ sharedPreferences.getString('token')), };   
    var request = http.MultipartRequest(
      "POST", Uri.parse('http://192.168.43.178:8080/images_upload/'));
    request.headers.addAll(headers);  
    //add text fields
    //create multipart using filepath, string or bytes
    var pic = await http.MultipartFile.fromPath("image", '/storage/emulated/0/WhatsApp/Media/WhatsApp Images/IMG-20200410-WA0017.jpeg');
    //add multipart to request
    request.files.add(pic);
    var response = await request.send();

    //Get the response from the server
    var responseData = await response.stream.toBytes();
    var responseString = String.fromCharCodes(responseData);
    return responseString;
  }

  _send()async{ 
      //archive file   
      // var path = _formZip();  //path of zip file 
      SharedPreferences sharedPreferences = await SharedPreferences.getInstance(); 
      Map<String, String> headers ={ 'Authorization': ('Token '+ sharedPreferences.getString('token')), };   
      Uri uri = Uri.parse("http://192.168.43.178:8080/images_upload/"); 
      http.MultipartRequest request = new http.MultipartRequest('POST', uri);
      request.headers.addAll(headers);  
      final mimeTypeData =  lookupMimeType( shared_list.resultList[0].path, headerBytes: [0xFF, 0xD8]).split('/');
      
      var pic= await http.MultipartFile.fromPath(
          'image_file1', shared_list.resultList[0].path, contentType: MediaType(mimeTypeData[0], mimeTypeData[1]));
      request.files.add(pic); 
      // request.files.add(await http.MultipartFile.fromPath(
      //     'zip_file1', path,contentType: MediaType("application", "zip") ));
      // request.files.add(await http.MultipartFile.fromPath(
      //     'zip_file1', path,contentType: MediaType(mimeTypeData[0], mimeTypeData[1]) ));
 
      try {
          final streamedResponse = await request.send();
            print("------------------------------------");

          // var responseData = await streamedResponse.stream.toBytes(); 
          // final response = String.fromCharCodes(responseData);
          // if (response.statusCode != 200) { 
          //  return null;
          //  } 
        print(  streamedResponse.statusCode);
        reset();
      return streamedResponse;
    } catch (e) {
      print(e);
      return null;
    }
}

}
// 