import 'dart:io';
import 'package:archive/archive_io.dart';
import 'package:path_provider/path_provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../component/shared_data.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import '../component/jason_prac.dart';
import '../component/shared_data.dart';

formZip() async {
  Directory appDocDirectory = await getExternalStorageDirectory();
  var encoder = ZipFileEncoder();
  var _path = appDocDirectory.path + "/" + 'jay.zip';
  encoder.create(_path);
  for (var item in SharedList.resultList) encoder.addFile(item);
  encoder.close();
  return _path;
}

getClassDetails(String subjectId, SharedPreferences sharedPreferences) async {
  String urlData =  urlClassDetail;
  var credentials = {
    'Authorization': ('Token ' + sharedPreferences.getString('token')),
  };
  var response2 = await http.post(urlData, headers: credentials);
  var jsonResponse;
  if (response2.statusCode == 200) {
    jsonResponse = json.decode(response2.body);
    if (jsonResponse != null) {
      print(jsonResponse[0]["message"]);
      ClassHistDateWise.subjectId = jsonResponse[1]["subject_id"];
      List<DateAttendance> list_date_wise = new List<DateAttendance>();

      var listHistory = jsonResponse[1]["list_date_wise"];
      for (var item in listHistory) {
        list_date_wise.add(DateAttendance(item["date"], item["slot"],
            item["extra_class"], item["present"], item["total"]));
      }

      ClassHistDateWise.attendanceList = list_date_wise;
    }
  } else {
    print(response2.body);
  }
}

getStudentDetails(String subjectId, String studentId) async {
  SharedPreferences sharedPreferences = await SharedPreferences.getInstance();
  print("hi=-=--------------------------");
  String urlData =  urlStudentDetail;
  var credentials = {
    'Authorization': ('Token ' + sharedPreferences.getString('token')),
  };
  var response2 = await http.post(urlData, headers: credentials);
  var jsonResponse;
  print("hi=-=--------------------------");
  if (response2.statusCode == 200) {
    jsonResponse = json.decode(response2.body);
    if (jsonResponse != null) {
      print(jsonResponse[0]["message"]);
      print("hi=-=--------------------------");
      StudentHist.courseId = jsonResponse[1]["subject_id"];
      print(StudentHist.courseId);
      StudentHist.courseName = jsonResponse[1]["subject_name"];
      print(StudentHist.courseName);
      StudentHist.studentId = jsonResponse[1]["student_id"];
      print(StudentHist.studentId);
      StudentHist.studentName = jsonResponse[1]["student_name"];
      print("hi=-=--------------------------");
      List<StudentDailyEntry> detailList = new List<StudentDailyEntry>();

      var subjList = jsonResponse[1]["list"];
      for (var item in subjList) {
        detailList.add(StudentDailyEntry(item["date"], item["slot"],
            item["extra_class"], item["Attendance"]));
      }
      print("hi=-=--------------------------");
      StudentHist.attendanceList = detailList;
    }
  } else {
    print(response2.body);
  }
}

getTeacherDetails(SharedPreferences sharedPreferences) async {
  String urlData =  urlTeacherDetail;
  var credentials = {
    'Authorization': ('Token ' + sharedPreferences.getString('token')),
  };

  var data = {'message': 'hello'};
  var bodyData = json.encode(data);
  var response2 =
      await http.post(urlData, headers: credentials, body: bodyData);
  var jsonResponse;

  if (response2.statusCode == 200) {
    jsonResponse = json.decode(response2.body);
    if (jsonResponse != null) {
      print(jsonResponse[0]["message"]);
      TeacherDetails.name = jsonResponse[1]["name"];
      TeacherDetails.id = jsonResponse[2]["id"];
      List<SubjectWiseDetail> subjDetailList =
          new List<SubjectWiseDetail>();
      var subjList = jsonResponse[3]["detail"];

      for (var item in subjList) {
        List<StudentClass> studList = new List<StudentClass>();
        for (var entry in item["students_list"]) {
          studList
              .add(StudentClass(entry["student_name"], entry["student_id"]));
        }
        subjDetailList.add(SubjectWiseDetail(
            item["subject_name"], item["subject_id"], studList));
      }

      TeacherDetails.subjectDetailList = subjDetailList;
    }
  } else {
    print(response2.body);
  }
}
