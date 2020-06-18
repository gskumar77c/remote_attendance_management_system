import 'dart:io';

class SharedList {
  static List<File> resultList;

  static add(File value) {
    resultList = List<File>();
    resultList.add(value);
  }
}

String urlIP = "http://192.168.43.178:8000/";

String urlApiTokenAuth =  urlIP + "api-token-auth/";
String urlStudentDetail = urlIP +  "student_wise/";
String urlTeacherDetail =  urlIP + "teacher_profile/";
String urlClassDetail =  urlIP +  "class_history/";